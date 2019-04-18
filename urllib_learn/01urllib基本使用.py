from urllib import request


# urlopen的使用
# resp = request.urlopen("http://www.baidu.com")  # 默认为get请求，如果添加了data=,则为post请求
# print(resp.read().decode())  # read()读取句柄  decode()解码
# print(resp.readline())  # 只读取一行
# print(resp.readlines())  # 读取多行列表形式
# print(resp.getcode())  # 显示状态码

# urlretrieve的使用
# url = "http://www.baidu.com"
# path = "./img01.html"
# request.urlretrieve(url, path)  # 网址，路径与文件名

# urlencode与parse_qs  编码与解码
# from urllib import parse
# data = {
#     "name":"张科选",
#     "age":18,
#     "sex":"男"
# }
# qs = parse.urlencode(data)
# qs = parse.parse_qs("sex=%E7%94%B7&name=%E5%BC%A0%E7%A7%91%E9%80%89&age=18")
# print(qs)

from urllib import parse
#  urlparse 与urlsplit  网址分割 用途基本相似。区别：urlparse多了一个params属性
url = "https://www.baidu.com/s?word=%E5%88%98%E5%BE%B7%E5%8D%8E&tn=99669880_hao_pg"
result1 = parse.urlparse(url)
print(result1)
print(result1.netloc)
result2 = parse.urlsplit(url)
print(result2)