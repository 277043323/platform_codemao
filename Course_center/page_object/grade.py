from selenium.webdriver.common.by import By

from Course_center.base.base_page import BasePage
from Course_center.page_object.class_manage import ClassManage


class Grade(BasePage):
    def grade_ture(self):
        self.find(By.XPATH,'//*[@class="menu"]/div[1]').click()

        return ClassManage(self._driver)


