from urllib import request
from urllib import parse


#  增加请求头和代理
headers = {
    "User_Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
    "Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
    "Cookie":"_ga=GA1.2.299507108.1552549186; user_trace_token=20190314153949-58a721a6-462c-11e9-953c-5254005c3644; LGUID=20190314153949-58a7265d-462c-11e9-953c-5254005c3644; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221698ee6ee90721-002656d84e263c-3d644601-2073600-1698ee6ee911c1%22%2C%22%24device_id%22%3A%221698ee6ee90721-002656d84e263c-3d644601-2073600-1698ee6ee911c1%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; JSESSIONID=ABAAABAAAGFABEFE209E92281CBD0F08B72BCFB8552A21E; WEBTJ-ID=20190401162753-169d803125370-0ae4d18ec3705d-3d644601-2073600-169d80312544ca; index_location_city=%E6%B1%9F%E8%8B%8F; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=28; _gid=GA1.2.153100207.1555575007; LGSID=20190418172856-6381893d-61bc-11e9-93c4-5254005c3644; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dkii287EVUvKRm7bgJSuNSgArb_GumePQ79rHnjLyt8m%26wd%3D%26eqid%3Dc5b94da70005313a000000055cb84352; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=index_search; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1555323369,1555575013,1555579730,1555579873; X_HTTP_TOKEN=329d9a6d35f5bf805120855551a6a5138969e7b333; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1555580209; LGRID=20190418173655-811d60a3-61bd-11e9-8b61-525400f775ce; SEARCH_ID=55979e6a660a4ef0b9e39511c8cf853f",
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'X-Anit-Forge-Code':'0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With':'XMLHttpRequest',
    'Host':'www.lagou.com',
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Length": "25",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://www.lagou.com",
    "Pragma": "no-cache",

}
url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"

data = {
    "first":"true" ,
    "pn": 1,
    "kd": "python",
}

req= request.Request(url, headers= headers, data=parse.urlencode(data).encode("utf-8"), method="POST")
result = request.urlopen(req)
print(result.read().decode())