from selenium import webdriver
from selenium.webdriver.common.by import By

from Course_center.page_object.index_cmp import CMP
from Course_center.page_object.cmp import Cmp


class Index:
    def __init__(self):
        self._driver = webdriver.Chrome()
        self._driver.get('https://staging-edu.codemao.cn/')

    def goto_login(self):
        # click login
        self._driver.find_element(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        return CMP(self._driver)

    def goto_register(self):
        # click register
        self._driver.find_element(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()
        return Cmp(self._driver)
