from test0325.get_IP import GetProxies
from test0325.test_ip import Tester
import time


if __name__ == '__main__':
    while True:
        get = GetProxies()
        test = Tester()
        get.run()
        # test.run()
        time.sleep(15*60)