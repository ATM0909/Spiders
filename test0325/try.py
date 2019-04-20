import requests
from test0325.setting import list
from test0325.manage_redis import RedisClient
import random
def get_proxy():
    redis = RedisClient()
    return redis.random()
def get_page(url, options={}):
    """
    抓取页面
    :param url:
    :param options:
    :return:（html页面）
    """
    base_headers = {
            # "user-agent": random.choice(list),
            "user-agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
        }
    headers = dict(base_headers, **options)

    proxy = get_proxy()
    proxies = {
            'http': 'http://' + proxy,
            'https': 'https://' + proxy,
        }
    try:
        response = requests.get(url, headers=headers, proxies=proxies, timeout=5)
        response.encoding = 'utf8'
        if 200 == response.status_code:
            print('抓取成功', url)
            print(response.text)

            return response.text
    except requests.ConnectionError:
          return None

if __name__ == '__main__':
    # get_page('https://wenku.baidu.com/view/be0031313186bceb18e8bba8.html?rec_flag=default&sxts=1551669281597###')
    while True:
        get_page('http://101.132.127.25/')