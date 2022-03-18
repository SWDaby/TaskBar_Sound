import ctypes
import backstage
import threading
import volume_control

# pyinstaller --icon=res/sound-waves.ico -F .\main.py
# 隐藏控制台
whnd = ctypes.windll.kernel32.GetConsoleWindow()
if whnd != 0:
    ctypes.windll.user32.ShowWindow(whnd, 0)
    ctypes.windll.kernel32.CloseHandle(whnd)




def on_run():
    app = backstage.MyApp()
    t1 = threading.Thread(target=volume_control.on_listen)
    t1.daemon = True
    t1.start()
    # print('开始监听鼠标')
    app.MainLoop()


if __name__ == '__main__':
    # print('开始运行程序')
    on_run()
    # print('程序结束')
