import threading
gLock = threading.Lock()
value = 0
def add_value():
    global value
    gLock.acquire()
    for i in range(1000000):
        value+=1
    gLock.release()
    print(value)

if __name__ == '__main__':

    for i in range(2):

        t = threading.Thread(target=add_value)
        t.start()