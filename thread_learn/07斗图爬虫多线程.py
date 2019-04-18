import requests
import threading
from lxml import etree
import urllib.request
import os
import re
from queue import Queue

def gethtml(url, img_queue):
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
        img_queue.put((img_url, filename))
            # return ()

def producter(page_queue, img_queue):
    while True:
        if page_queue.empty():
            break
        url = page_queue.get()
        gethtml(url, img_queue)


def customer(page_queue, img_queue):
    while True:
        if page_queue.empty() and img_queue.empty():
            break
        img_url, filename = img_queue.get()
        print(filename +"  下载完成……")
        urllib.request.urlretrieve(img_url, "images2/"+filename)

def main():
    page_queue = Queue(50)
    img_queue = Queue(1000)
    for x in range(1,7):
        page_url = "https://www.doutula.com/photo/list/?page=%d" % x
        page_queue.put(page_url)


    for i in range(3):
        threading1 = threading.Thread(target=producter, args=(page_queue, img_queue))
        threading1.start()
    for i in range(5):
        threading2 = threading.Thread(target=customer, args=(page_queue, img_queue))
        threading2.start()


if __name__ == '__main__':

    main()