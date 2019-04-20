import requests
from test0325.setting import list
from test0325.manage_redis import RedisClient
import random
def get_proxy():
    redis = RedisClient()
    return redis.random()

def get_page(url, options={}):
    base_headers = {
            "user-agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
        }
    headers = dict(base_headers, **options)
    proxies = {
            'http': 'http://' + get_proxy(),
            'https': 'https://' + get_proxy(),
        }
    try:
        response = requests.get(url, headers=headers, proxies =proxies, timeout=5)
        response.encoding = 'utf8'
        if 200 == response.status_code:
            print('抓取成功', url)
            # print(response.text)

            return response.text
    except :
        print('抓取' + url+'失败')
        return None

if __name__ == '__main__':
    while True:
        get_page('https://weixin.sogou.com/')