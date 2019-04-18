import requests
import threading
from lxml import etree
from urllib import request
import os
import re
from queue import Queue
class Producter(threading.Thread):
    def __init__(self, page_queue, img_queue):
        threading.Thread.__init__(self)
        # super(Producter, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def gethtml(self, url):
        headers ={
            "User_Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
        }

        reponse = requests.get(url, headers=headers)
        data = etree.HTML(reponse.text)
        img_list = data.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
        for img in img_list:
            img_url = img.get('data-original')
            img_name = img.get('alt')

            suffix = os.path.splitext(img_url)[1].replace("!dta","")
            suffix = suffix.replace("null","jpg")

            filename = re.sub(r"[\\s\\\\/:\\*\\?\\\"<>\\|]"," " ,img_name) + suffix
            self.img_queue.put((img_url, filename))
                # return ()

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.gethtml(url)

class Customer(threading.Thread):
    def __init__(self, page_queue, img_queue):
        threading.Thread.__init__(self)
        # super(Customer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue
    def run(self):
        while True:
            if self.page_queue.empty() and self.img_queue.empty():
                break
            img_url, filename = self.img_queue.get(block=True)
            print(filename +"  下载完成……")
            request.urlretrieve(img_url, "images2/"+filename)

def main():
    page_queue = Queue(50)
    img_queue = Queue(1000)
    for x in range(1,7):
        page_url = "https://www.doutula.com/photo/list/?page=%d" % x
        page_queue.put(page_url)


    for i in range(3):
        t1=Producter(page_queue, img_queue)

        t1.start()
    for i in range(5):
        t2 = Customer(page_queue, img_queue)
        t2.start()


if __name__ == '__main__':

    main()