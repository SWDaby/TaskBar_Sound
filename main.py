import backstage
import threading
import soundctrl


def on_run():
    app = backstage.MyApp()
    t1 = threading.Thread(target=soundctrl.on_listen, name="监听")  # args=['work1']
    t1.daemon = True
    t1.start()
    print('开始监听鼠标')
    app.MainLoop()


if __name__ == '__main__':
    # app = taskBarIcon.MyApp()
    print('开始运行程序')
    on_run()
    print('程序结束')
   # sys.exit(0)
    # print('thread %s is running...' % threading.current_thread().name)
    # t = threading.Thread(target=on_run, name='runThread')
    # t.start()

    # print('thread %s ended.' % threading.current_thread().name)

    # app.MainLoop()
    # i=i+1
    # time.sleep(1)
