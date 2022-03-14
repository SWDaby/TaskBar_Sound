import ctypes
import threading
from pynput import mouse
from uiautomation import GetElementFromPoint
import uiautomation as auto
import backstage

lock = threading.Lock()
Amouse = mouse.Controller()
WM_APPCOMMAND = 0x319
APPCOMMAND_VOLUME_UP = 0x0a  # 1010
APPCOMMAND_VOLUME_DOWN = 0x09  # 1001
APPCOMMAND_VOLUME_MUTE = 0x08  # 1000
user32 = ctypes.windll.user32
hwnd = user32.GetForegroundWindow()
UI_CLASSNAME = 'Windows.UI.Input.InputSite.WindowClass'



def GetElementInfo(element):  # gets the property information about an element
    element_info = auto.Control.CreateControlFromElement(element)
    return element_info


def on_scroll(x, y, dx, dy):

    with auto.UIAutomationInitializerInThread(debug=True):
        try:
            #t = ctypes.wintypes.POINT(x, y)
            # 通过鼠标位置获取窗口元素类名
            element_moved = GetElementFromPoint(x, y)
            element_scrolled_info = auto.Control.CreateControlFromElement(element_moved)    # returns info about the element you clicked
            #print("元素类名:" + element_scrolled_info.ClassName)
            if dy < 0 and element_scrolled_info.ClassName == UI_CLASSNAME:
                user32.SendMessageA(hwnd, WM_APPCOMMAND, 0, APPCOMMAND_VOLUME_DOWN * 0x10000)
                #time.sleep()

            elif element_scrolled_info.ClassName == UI_CLASSNAME:
                user32.SendMessageA(hwnd, WM_APPCOMMAND, 0, APPCOMMAND_VOLUME_UP * 0x10000)
                #time.sleep()

        except Exception as e:
            pass
            #print(e)


def on_listen():
    try:
        lock.acquire()
        with mouse.Listener(on_scroll=on_scroll) as listener:
            listener.join()

    finally:
        lock.release()

def on_main():
    app = backstage.MyApp()
    t1 = threading.Thread(target=on_listen, name="监听")
    t1.daemon = True
    t1.start()
    print('开始监听鼠标')
    app.MainLoop()


if __name__ == '__main__':
    print('开始运行程序')
    on_main()
    print('程序结束')

