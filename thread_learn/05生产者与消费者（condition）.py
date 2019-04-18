import threading
import random
import time


condition = threading.Condition()
TotalMoney=1000
TotalTime = 10
times = 0

class Producter(threading.Thread):
    def run(self):
        global TotalMoney, times, TotalTime
        while True:
            condition.acquire()
            money = random.randint(100, 1000)
            if times>=TotalTime:
                condition.release()
                break
            TotalMoney +=money
            print("%s生产了%d元钱，剩余%d元钱" %(threading.current_thread(), money, TotalMoney))
            times+=1
            condition.notify_all() # 通知所有线程 notify()通知一个线程（默认通知第一个）
            condition.release()
            time.sleep(0.5)


class Customer(threading.Thread):
    def run(self):
        global TotalMoney, times, TotalTime
        while True:
            condition.acquire()
            money = random.randint(100, 1000)
            while TotalMoney<money:
                if times>=TotalTime:
                    condition.release()
                    return
                print("%s准备消费%d元钱，剩余%d元钱， 不足！" %(threading.current_thread(), money, TotalMoney))
                condition.wait()  # 等待（线程等待，并且释放锁）

            TotalMoney -=money
            print("%s消费了%d元钱，剩余%d元钱" %(threading.current_thread(), money, TotalMoney))





            condition.release()
            time.sleep(0.5)


if __name__ == '__main__':
    for j in range(3):
        t2 = Customer(name="消费者%d" % j)
        t2.start()
    for i in range(5):
        t1 = Producter(name="生产者%d" % i)
        t1.start()



