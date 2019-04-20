from test0325.get_html import get_page
from bs4 import BeautifulSoup
from test0325.manage_redis import RedisClient
from test0325.test_ip import Tester


class GetProxies(object):
    """
    获取代理并进行测试，存储至redis数据库
    """
    def __init__(self):
        self.redis = RedisClient()
        self.test = Tester()

    def get_proxies_66ip(self, page_count=7):
        """
        获取代理66
        :param page_count: 页码
        :return: 代理
        """
        start_url = 'http://www.66ip.cn/{}.html'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            print('正在爬取', url)
            html = get_page(url)
            if html:
                soup = BeautifulSoup(html, 'html.parser')
                divs = soup('div', class_="containerbox boxindex")
                for div in divs:
                    trs = div.find_all('tr')
                    for tr in trs[1:]:
                        ip = tr.find_all('td')[0].text
                        port = tr.find_all('td')[1].text

                        # print(':'.join([ip, port]))
                        yield ':'.join([ip, port])
                        # yield {
                        #     'style': 'http',
                        #     'proxy': ':'.join([ip, port]),
                        # }

    def get_proxies_xicidaili(self, page_count=7):
        """
        爬取西刺代理
        :param page_count: 页码
        :return: 代理
        """
        start_url="https://www.xicidaili.com/nn/{}.html"
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            print('正在爬取', url)
            html = get_page(url)
            if html:
                soup = BeautifulSoup(html, 'lxml')
                trs = soup.select_one("#ip_list").select("tr")[1:]
                for tr in trs:
                    tds = tr.select('td')
                    ip = tds[1].string
                    port = tds[2].string
                    # type = tds[5].string
                    # print([ip, port])
                    yield ':'.join([ip, port])

    def run(self):
        """
        获取代理并存储到redis,score为10
        """
        for proxy in self.get_proxies_66ip():
            if self.test.is_able(proxy):
                self.redis.add(proxy)
        for proxy in self.get_proxies_xicidaili():
            if self.test.is_able(proxy):
                self.redis.add(proxy)


if __name__ == '__main__':
    getip = GetProxies()
    getip.run()

