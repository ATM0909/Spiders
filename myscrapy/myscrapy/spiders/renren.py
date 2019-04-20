# -*- coding: utf-8 -*-
import scrapy

import re
class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/970315833']
    """
    第一种方法，携带cookies
    start_urls = ['http://www.renren.com/970315833']
    """
    def start_requests(self):
        cookies="anonymid=ju3p5z63-gbqf4v; depovince=GW; _r01_=1; JSESSIONID=abc7CYfbaAHQEehz4nSNw; ick_login=3bf51c68-6d01-4bd7-8808-a533a4b8f95c; XNESSESSIONID=5381b2574241; wp=0; vip=1; ick=e4ad37e2-8b3a-424f-8142-c56f68237553; first_login_flag=1; ln_uact=18252587523; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=37061a36-3c1b-4ca1-9cd8-1b377cefaa30%7Cb2187808ca9125ca9bda4e9db8333a2b%7C1554457389243%7C1%7C1554457388214; jebecookies=f7bdf6e6-2a37-45d5-9f68-87de7c447c14|||||; _de=99E0E7E410C907E00E1F3341B155F40B; p=5e24d850bdf49781c393173852e6251a3; t=cbefb373e5e8baf89a95ac44a284fb703; societyguester=cbefb373e5e8baf89a95ac44a284fb703; id=970315833; xnsid=11e1fd39; ver=7.0; loginfrom=null; wp_fold=0"

        cookies = {i.split('=')[0]:i.split('=')[1] for i in cookies.split('; ')}
        # print(cookies)
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies= cookies,
        )
    def parse(self, response):
        print(response.body.decode())
        # name = re.findall("144", response.body.decode())
        # print(name)
    # """
    # 第二种方法，post请求
        start_urls = ['http://www.renren.com']
    # """
    # def parse(self, response):
    #     yield scrapy.FormRequest.from_response(
    #
    #         response,
    #         formdata={"email":"18252587523", "password":"zhang1996925"},
    #         callback= self.start,
    #
    #
    #     )
    # def start(self, response):
    #     print(response.body.decode())
    #     # name = re.findall("144", response.body.decode())
    #     # print(name)
