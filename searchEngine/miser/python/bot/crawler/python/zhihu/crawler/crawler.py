# -*- coding: utf-8 -*- 
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait

BROWSER = webdriver.Chrome()

def request(search_content):
    respond = requests.get(f"https://www.zhihu.com/search?type=content&q={search_content}")
    return respond.text

def browser_request(serch_content):
    BROWSER.get(f"https://www.zhihu.com/search?type=content&q={search_content}")
    print(BROWSER.page_source)


class Crawler:
    def __init__(self):

        self.header = {
        'Host':"www.zhihu.com",
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
        'Accept':"*/*",
        'Accept-Language':"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        'Accept-Encoding':"gzip, deflate",
        'Content-Type':"application/x-www-form-urlencoded; charset=UTF-8"
    }
        self.session = requests.session()
        # self.signin_url = 'http://www.zhihu.com/#signin' #https://www.zhihu.com/signin?next=%2F
        self.signin_url = "https://www.zhihu.com/signin?next=%2F"
        self.captcha_url = "http://www.zhihu.com/captcha.gif"

    def login(self):


        
        xsrf = BeautifulSoup(self.session.get(self.signin_url).content)#.find('input', attrs={'name': '_xsrf'})['value'] # 从源码中获取的表单中的一个字段
        _xsrf=hhTdqvvVIOu8tEVqZzzuBrV2xinb8yua

    
    def _request_captcha(self):
        rst = self.session.get(self.captcha_url, headers = self.header)
        print(rst)



if __name__ == "__main__":
    test_crawler = Crawler()
    rst = test_crawler.login()
    with open("rst.jpg", "wb") as fw:
        fw.write(rst.content)
    print(rst)