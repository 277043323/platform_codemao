from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from Course_center.base.base_page import BasePage
from Course_center.page_object.coursemanage import CourseManage

import pytest


class Cmp(BasePage):
    # def __init__(self, driver: WebDriver):
    #     self._driver = driver

    def cmp_true(self):

        self.find(By.XPATH,'//*[@class="go-class-btn"]').click()

        # sleep(5)
        # self._driver.quit()
        #默认选中"平台首页"

        return CourseManage(self._driver)


    #对文件进行上传
