import requests
from test0325.manage_redis import RedisClient
from test0325.setting import list
import random

class Tester(object):
    def __init__(self):
        self.redis = RedisClient()

    def get_random_header(self):
        headers={
            'User-Agent':random.choice(list),
            'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            'Accept-Encoding':'gzip'
        }
        return headers
    def is_able(self, proxy):
        """
        判断单个代码是否可用
        :param proxy
        :return:
        """
        test_url = 'https://www.zhipin.com/'
        proxies = {
            'http': 'http://' + proxy,
            'https': 'https://' + proxy,
        }

        try:
            response = requests.get(test_url,proxies=proxies,timeout=2)

            if response.status_code == 200:
                return True

            else:
                return False

        except:
            return False
    def test_proxy(self, proxy):
        """
        测试单个代码
        :param proxy
        :return:
        """
        if self.is_able(proxy):
            self.redis.max(proxy)

        else:
            self.redis.decrease(proxy)

    def run(self):
        """
        测试主函数
        :return:
        """
        print('测试器开始运行')
        try:
            count = self.redis.count()
            print('当前剩余', count, '个代理')

            test_proxies = self.redis.all()
            # print(type(test_proxies))
            maps = map(self.test_proxy, test_proxies)
            for map1 in maps:

                print(map1)
            # time.sleep(10)
        except Exception as e:
            print('测试器发生错误', e.args)
if __name__ == '__main__':
    test = Tester()
    # test.test_proxy('62.103.175.8:2')
    test.run()