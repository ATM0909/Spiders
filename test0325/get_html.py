import requests
from test0325.setting import list
import random

def get_page(url, options={}):
    """
    抓取页面
    :param url:
    :param options:
    :return:（html页面）
    """
    base_headers = {
            "user-agent": random.choice(list),
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
        }
    headers = dict(base_headers, **options)

    try:
        response = requests.get(url, headers=headers)
        response.encoding = 'utf8'
        if 200 == response.status_code:
            print('抓取成功', url)

            return response.text
    except requests.ConnectionError:
        print('抓取' + url+'失败')
        return None

if __name__ == '__main__':
    get_page('https://wenku.baidu.com/view/be0031313186bceb18e8bba8.html?rec_flag=default&sxts=1551669281597###')