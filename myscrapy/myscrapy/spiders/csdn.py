# -*- coding: utf-8 -*-
import scrapy

import re
class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    allowed_domains = ['www.csdn.net']
    start_urls = ['https://i.csdn.net/#/uc/profile']

    def start_requests(self):
        cookies="uuid_tt_dd=10_30276391150-1551609550884-264412; smidV2=2019030411192345b5f1368f06cbc802f801d14255f47400b94080ac43a8f30; dc_session_id=10_1551708902539.997303; UM_distinctid=16986e74e5f50-09fc48af5da024-3d644601-1fa400-16986e74e6018e; yidun_tocken=9ca17ae2e6ffcda170e2e6eeaddb79fba88fb5f35386868eb3c54f868a8abab73cb39fa09be7808fb1badaeb2af0feaec3b92aa9a79fa3b16182f0bcb5d95a928b9eb3d54a9ab0ffd0d86aae87c0d6b433f6afee9e; aliyun_webUmidToken=T27A82EF3FB4A6102256DA417F3C51E20F01175E92E5D4338E1680A391E; aliyun_UAToken=115#1b3gP11O1TwqAkS4TCIA1CsoE51GB9A11g2mOh2/JfOcAzCCrO0oB5tuL6JcyzzsAs1Pe1L8yWQsR7BJhUU4AWNcaTpbyW1QOSAyeKT4ukNQi/W5hqz4OkdDGkGEOZPQAylPetT8ukNQi/JRY4U4AWNcaLpXszEQASA9FtB/CEm56Z6O21fCX1OMrDDQwN7lTT1E/gQc3Xp+HI+mmuUwbI+Cg73IhWCHlSom6dkEWmNpyj7oirC9A1hruurmR2HpRZib5C/vyLC4EK5i2UfvVf49cOjJ7Qils0qchMZXDYdtOsomnibq5qSiau2mWs8eOzUZGC+K52Bra67VJrAu62znhmajKgDpNr79Xei71DdA7pMKmrP6g9f9truBBBqWhwLRHP3YFZJ7fPZWmO4jZx0eGrjSKFNYEVUai/1Sp4V/Ux6URams1RniLVaJMA9IMWaGjltfmh0UmB/9QSNLVSk3lV3evWw7TSZwgyy61nC3E4ajDV/x34A8wqGqKz2Y0DCwj4qTX2s57R9zgHJEErOHpOn2N5DgnjwEzvVXpCUlyt/pxOUvN0NDi/rCxTDyPZbbqh7NfIaIC+GKKQxD0dcAd0lmOUUWQVZghdXqYKxxI4gRZksZ/yqyUYg+05uz9Cauqb72Zmu7EXfnqaGjdVi79v1xK8zMwcCcJkVg8VS9KqrdQmUWs2h8AY6HHF2O//7ebfs2WinLFzH+d2xM8deJg1AHVqKrB7s0GBYpm+Exp5XZdtKuXjtL3cQpH0CbdEc=; firstDie=1; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1554449605,1554457847,1554458173,1554458192; SESSION=536761e4-c062-4067-8562-d4166df43f67; UN=qq_43423834; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=5744*1*qq_43423834!1788*1*PC_VC!6525*1*10_30276391150-1551609550884-264412; UserName=qq_43423834; UserInfo=95775411ef484939b311b9d13ddfcf68; UserToken=95775411ef484939b311b9d13ddfcf68; UserNick=qq_43423834; AU=0A9; BT=1554476497979; dc_tos=pphtqy; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1554476506"

        cookies = { i.split('=')[0]:i.split('=')[1] for i in cookies.split('; ')}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies= cookies,
        )
    def parse(self, response):
        # print(response.body.decode())
        name = re.findall(r"qq_43423834", response.body.decode())
        print(name)
