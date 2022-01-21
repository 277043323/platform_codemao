from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Course_center.base.base_page import BasePage
import time


class ClassManage(BasePage):
    def create_grade(self):
        self.find(By.XPATH,'//*[@class="head-operation"]').click()
        self.find(By.XPATH,'//*[@class="modal-content"]//input').send_keys("班级一")
        self.find(By.XPATH,'//*[@class="modal-content"]//button').click()

