import threading
import time
def sing():
    for i in range(3):
        print("正在唱歌……\n")
        time.sleep(1)
def dance():
    for i in range(3):
        print("正在跳舞……\n")
        time.sleep(1)
if __name__ == '__main__':
    # sing()
    # dance()
    threading1 = threading.Thread(target=sing)
    threading2 = threading.Thread(target=dance)
    threading1.start()
    threading2.start()
    print(threading.enumerate())  # 当前所有的线程， 列表形式
    print(len(threading.enumerate()))  # 线程的数量
    print(threading.current_thread())  # 当前线程的信息