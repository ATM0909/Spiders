from selenium import webdriver
import time
from lxml import etree
from selenium.webdriver.common.by import By
import requests

class Boss(object):
    driver_path = r"E:\chromedriver_win32\chromedriver.exe"

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Boss.driver_path)
        self.url = 'https://www.zhipin.com/job_detail/?query=java&city=101190100&industry=&position='
        self.position = {}
        self.headers = {
            "user-agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
        }
    def run(self):
        """
        运行
        """
        self.driver.get(self.url)

        while True:

            source = self.driver.page_source
            # print(source)
            # break
            self.parse_list_page(source)

            # 解析完当页页面所有数据之后，点击下一页

            page_next_btn= self.driver.find_element(By.CLASS_NAME,"next")


            if "next" not in page_next_btn.get_attribute("class"):
                break  # 如果下一页的按钮不能点击，break结束
            else:
                page_next_btn.click()


    def parse_list_page(self, source):
        """
        解析页面，获取每个职位的data
        :param source 首页的页面资源
        :return data
        """
        html = etree.HTML(source)
        li_list = html.xpath("//div[@class='job-list']/ul/li")
        for li in li_list:

            href = li.xpath(".//div[@class='info-primary']/h3/a/@href")[0]
            href = "https://www.zhipin.com" + href
            job_info = li.xpath(".//div[@class='info-primary']/p//text()")

            company = li.xpath(".//div[@class='info-company']/div[@class='company-text']//a/text()")[0]
            company_info = li.xpath(".//div[@class='info-company']/div[@class='company-text']/p//text()")

            job_title = li.xpath(".//div[@class='job-title']/text()")[0]
            salary = li.xpath(".//span[@class='red']/text()")[0]


            data_jid = li.xpath("./div/div[@class='info-primary']/h3/a/@data-jid")[0]
            data_lid = li.xpath("./div/div[@class='info-primary']/h3/a/@data-lid")[0]
            desc_url = "https://www.zhipin.com/wapi/zpgeek/view/job/card.json?jid={}&lid={}".format(data_jid, data_lid)


            self.position["name"] = job_title
            self.position["salary"] =salary
            self.position["job_info"] =job_info
            self.position["company"] =company
            self.position["company_info"] =company_info
            self.position["href"] =href

            self.position["desc"]= self.desc_detail(desc_url)
            # self.desc_detail(desc_url)
            print(self.position)
            break
            time.sleep(2)

    def desc_detail(self,url):
        self.driver.execute_script("window.open('%s')" % url)
        self.driver.switch_to.window(self.driver.window_handles[1])
        # source = self.driver.page_source
        # print(source)
        # html = etree.HTML(source)
        # print(html)
        r = requests.get(url, headers=self.headers,timeout=5)
        data = r.json()["zpData"]["html"]
        data = etree.HTML(data)
        e = data.xpath("//div[@class='detail-bottom-text']/text()")


        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        return e
if __name__ == '__main__':
    spider = Boss()
    spider.run()