import shelve

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from Course_center.page_object.cmp import Cmp

from Course_center.base.base_page import BasePage

#codemaoplatform

class CMP(BasePage):
    _base_url = "https://test-edu.codemao.cn/"

    def goto_cmp(self):
        # cookie = self._driver.get_cookies()
        #保存获取的cookie
        db = shelve.open("cookies")
        # db["cookie"]=cookie
        cookies = db["cookie"]
        # # # # print(cookies)
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self._driver.add_cookie(cookie)
        self._driver.get("https://test-edu.codemao.cn/")
        return Cmp(self._driver)





