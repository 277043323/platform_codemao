from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


class Demo():
    driver = None

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            options = Options()
            options.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=options)
            self.driver.get("https://test-edu.codemao.cn/")
            self.cookies = self.driver.get_cookies()

        return self.driver


class Test_demo(Demo):
    # driver=None
    # def __init__(self,driver:WebDriver = None):
    #     if driver is None:
    #         options = Options()
    #         options.debugger_address="127.0.0.1:9222"
    #         self.driver=webdriver.Chrome(options=options)
    #         self.driver.get("https://test-edu.codemao.cn/")
    #         self.cookies = self.driver.get_cookies()
    def setup(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)

        self.driver.get("https://test-edu.codemao.cn/")
        self.cookies = self.driver.get_cookies()
        # self.cookie = cookies["cookie"]

    @pytest.fixture(scope="module")
    def login(self):
        # print(type(self.cookies))
        print("你好啊")
        self.driver.add_cookie(cookie_dict=self.cookies)

    def test_platform(self, login):
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="app"]/main/div[1]/div[2]/div[1]/div/span[1]/button').click()
        sleep(3)
        element = self.driver.find_element_by_xpath('//*[@class="title"]')
        print(element)
        ele = self.driver.find_element_by_xpath('//*[@class="icon"]')
        print(ele)
        assert element is not None
        pytest.assume(ele is not None)
