import ctypes
import pynput.mouse
import task_bar

WM_APPCOMMAND = 0x319
APPCOMMAND_VOLUME_UP = 0x0a  # 1010
APPCOMMAND_VOLUME_DOWN = 0x09  # 1001
APPCOMMAND_VOLUME_MUTE = 0x08  # 1000
user32 = ctypes.windll.user32
Ymin = task_bar.get_Taskbar_dim()[1]
Ymax = task_bar.get_Taskbar_dim()[0]
hwnd = user32.GetForegroundWindow()


def on_scroll(x, y, dx, dy):
    # 监听鼠标滚轮

    if Ymin <= y <= Ymax:

        if dy < 0:
            # print(dy)
            user32.PostMessageA(hwnd, WM_APPCOMMAND, 0, APPCOMMAND_VOLUME_DOWN * 0x10000)

        else:
            # print(dy)
            user32.PostMessageA(hwnd, WM_APPCOMMAND, 0, APPCOMMAND_VOLUME_UP * 0x10000)
    else:
        return False


def on_listen():
    while True:
        with pynput.mouse.Listener(
                on_scroll=on_scroll) as listener:
            listener.join()
