from selenium.webdriver.common.by import By

from Course_center.base.base_page import BasePage
from Course_center.page_object.class_manage import ClassManage


class Grade(BasePage):
    def grade_ture(self):
        # print(self._driver.window_handles)
        # print(self._driver.current_window_handle)
        self.find(By.XPATH,'//*[@class="menu"]/div[1]').click()
        # self._driver.switch_to_window(self._driver.window_handles[0])
        # print(self._driver.current_window_handle)

        return ClassManage(self._driver)


