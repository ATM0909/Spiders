import threading
import time
class Sing(threading.Thread):
    def run(self):
        for i in range(3):
            print("正在唱歌……%s" % threading.current_thread())
            time.sleep(1)
class Dance(threading.Thread):
    def run(self):
        for i in range(3):
            print("正在唱歌……%s " % threading.current_thread())
            time.sleep(1)
if __name__ == '__main__':
    t1 = Sing()
    t2 = Dance()
    t1.start()
    t2.start()