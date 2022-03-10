import threading
import time
from tkinter import *


def run(thread_title):
    '''


    :param thread_title:
    :return:
     time.sleep(1)
    print(thread_title, '2s')
    time.sleep(1)
    print(thread_title, '1s')
    time.sleep(1)
    print(thread_title, '0s')
    time.sleep(1)
    print(thread_title, '完成')
    print('kjhoidejf')
    '''
    i=0
    while True:
        i=i+1
        print(i)
        time.sleep(1)

def xc_1():
    ct = Tk()
    ct.title("Demo")
    pmk = ct.winfo_screenwidth()
    pmg = ct.winfo_screenheight()
    ctk = 400
    ctg = 400
    ctx = (pmk - ctk) // 2
    cty = (pmg - ctg) // 2
    ct.geometry("%ax%a+%a+%a" % (ctk, ctg, ctx, cty))
    ct.resizable(0, 0)

    t1 = threading.Thread(target=run, args=['work1'])
    t1.start()
    t2 = threading.Thread(target=run, args=['work2'])
    t2.start()
    ct.mainloop()


if __name__ == '__main__':
    xc_1()

