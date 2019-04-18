from selenium import webdriver
import time
from lxml import etree
from selenium.webdriver.common.by import By



class LaGou(object):
    driver_path = r"E:\chromedriver_win32\chromedriver.exe"

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=LaGou.driver_path)
        self.url = 'https://www.lagou.com/jobs/list_java?labelWords=&fromSearch=true&suginput=/'

    def run(self):
        """
        运行
        """
        self.driver.get(self.url)
        while True:

            source = self.driver.page_source
            self.parse_list_page(source)
            # 解析完当页页面所有数据之后，点击下一页


            page_next_btn = self.driver.find_element(By.CLASS_NAME,"pager_next ")
            if "pager_next pager_next_disabled" in page_next_btn.get_attribute("class"):
                break  # 如果下一页的按钮不能点击，break结束
            else:
                page_next_btn.click()

    def parse_list_page(self, source):
        """
        解析页面，获取每个职位的link
        :param source 首页的页面资源
        :return data
        """
        html = etree.HTML(source)
        link_list = html.xpath("//a[@class='position_link']/@href")
        for link in link_list:
            self.request_detail_page(link)

            time.sleep(2)

    def request_detail_page(self, url):
        """
        获取详情页数据 打开新的页面
        :param url
        :return data
        """
        # self.driver.get(url)
        self.driver.execute_script("window.open('%s')" % url)
        self.driver.switch_to.window(self.driver.window_handles[1])
        source = self.driver.page_source
        self.parse_detail_page(source)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def parse_detail_page(self, source):
        """
        解析详情页
        :param source
        :return 详情页数据
        """
        html = etree.HTML(source)
        job_name = html.xpath("//div[@class='job-name']/@title")[0]
        salary = html.xpath("//dd[@class='job_request']/p[1]/span[1]/text()")[0]
        job_addr = html.xpath("//dd[@class='job_request']/p[1]/span[2]/text()")[0]
        work_year = html.xpath("//dd[@class='job_request']/p[1]/span[3]/text()")[0]
        education = html.xpath("//dd[@class='job_request']/p[1]/span[4]/text()")[0]
        des = "".join(html.xpath("//dd[@class='job_bt']/div[@class='job-detail']//text()"))

        position = dict(
            name=job_name,
            salary=salary,
            job_addr=job_addr,
            work_year=work_year,
            education=education,
            des=des
        )
        print(position)





if __name__ == '__main__':
    spider = LaGou()
    spider.run()