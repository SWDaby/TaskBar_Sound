import backstage
import threading
import soundctrl


def on_run():
    app = backstage.MyApp()
    t1 = threading.Thread(target=soundctrl.on_listen, name="监听")
    t1.daemon = True
    t1.start()
    print('开始监听鼠标')
    app.MainLoop()


if __name__ == '__main__':

    print('开始运行程序')
    on_run()
    print('程序结束')

