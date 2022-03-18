import pywinauto as auto
import ctypes
from pynput import mouse
import logging
import threading


WM_APPCOMMAND = 0x319
APPCOMMAND_VOLUME_UP = 0x0a  # 1010
APPCOMMAND_VOLUME_DOWN = 0x09  # 1001
APPCOMMAND_VOLUME_MUTE = 0x08  # 1000

user32 = ctypes.windll.user32
hwnd = user32.GetForegroundWindow()

desktop = auto.Desktop()
UI_CLASSNAME = 'ReBarWindow32'

# 配置日志
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename="taskbar.log", level=logging.ERROR, format=LOG_FORMAT, datefmt=DATE_FORMAT)

# 进程锁
lock = threading.Lock()


def GetInfo_from_point(adesktop,x, y):
    """Get wrapper object for element at specified screen coordinates (x, y)"""
    element_info = adesktop.backend.element_info_class.from_point(x, y)
    return element_info


def GetInfo_top_from_point(adesktop, x, y):
    """Get wrapper object for top level element at specified screen coordinates (x, y)"""
    top_element_info = adesktop.backend.element_info_class.top_from_point(x, y)
    return top_element_info


def on_scroll(x, y, dx, dy):
    try:
        a_element_info = GetInfo_from_point(desktop,x, y)
        # print(type(a_element_info))
        # print("类名:", a_element_info.class_name)
        # print("父类类名:", a_element_info.parent.class_name, '\n')

        if dy < 0 and a_element_info.class_name == UI_CLASSNAME:
            user32.PostMessageA(hwnd, WM_APPCOMMAND, 0, APPCOMMAND_VOLUME_DOWN * 0x10000)

        elif a_element_info.class_name == UI_CLASSNAME:
            user32.PostMessageA(hwnd, WM_APPCOMMAND, 0, APPCOMMAND_VOLUME_UP * 0x10000)

    except Exception as e:
        if type(e) != AttributeError:
            # print(e)
            logging.error(e)


def on_listen():
    lock.acquire()
    with mouse.Listener(on_scroll=on_scroll) as listener:
        listener.join()
    lock.release()


# if __name__ == '__main__':

