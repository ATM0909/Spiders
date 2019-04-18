import threading
import random
import time


gLock = threading.Lock()
TotalMoney=1000
TotalTime = 10
times = 0

class Producter(threading.Thread):
    def run(self):
        global TotalMoney, times, TotalTime
        while True:
            gLock.acquire()
            money = random.randint(100, 1000)
            if times>=TotalTime:
                gLock.release()
                break
            TotalMoney +=money
            print("%s生产了%d元钱，剩余%d元钱" %(threading.current_thread(), money, TotalMoney))
            times+=1
            gLock.release()
            time.sleep(0.5)


class Customer(threading.Thread):
    def run(self):
        global TotalMoney, times, TotalTime
        while True:
            gLock.acquire()
            money = random.randint(100, 1000)
            if TotalMoney>=money:
                TotalMoney -=money
                print("%s消费了%d元钱，剩余%d元钱" %(threading.current_thread(), money, TotalMoney))
            else:
                if times>=TotalTime:
                    gLock.release()
                    break
                print("%s准备消费%d元钱，剩余%d元钱， 不足！" %(threading.current_thread(), money, TotalMoney))


            gLock.release()
            time.sleep(0.5)


if __name__ == '__main__':

    for j in range(3):
        t2 = Customer(name="消费者%d" % j)
        t2.start()
    for i in range(5):
        t1 = Producter(name="生产者%d" % i)
        t1.start()

