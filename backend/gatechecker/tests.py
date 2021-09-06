from django.test import TestCase

# Create your tests here.
import requests, json


def simple_connect():
    res = requests.post('http://127.0.0.1:8000/api_test/apis/', data={'a': 3, 'b': 4})
    print(res)
    print(res.text)


def simple_connect_2():
    req = {34: 1}
    url = 'http://127.0.0.1:8000/api_test/apis/'
    # params 为发送给服务器的请求
    params = {
          "name": "前端输入参数"
        }
    # 请求头，是浏览器正常的就行
    headers = {"User-agent": "none/ofyourbusiness", "Spam": "Eggs"}
    # 发送请求，返回新数据
    data = requests.post(url, data=params, headers=headers)

    print(data)
    print(data.text)


def index_view_post():
    res = requests.post('http://127.0.0.1:8000/api_test/')
    print(res)
    print(res.text)


def index_view_get():
    res = requests.get('http://127.0.0.1:8000/api_test/')
    print(res)
    print(res.text)


def index_view_put():
    res = requests.put('http://127.0.0.1:8000/api_test/')
    print(res)
    print(res.text)


simple_connect()
simple_connect_2()
index_view_post()
index_view_get()
index_view_put()
