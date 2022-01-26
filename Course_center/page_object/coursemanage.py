import time
from selenium.webdriver.common.by import By
from Course_center.base.base_page import BasePage
from Course_center.page_object.grade import Grade


class CourseManage(BasePage):
    def goto_courseManage(self):
        # num=self._driver.window_handles
        # print(num)
        self.find(By.XPATH, '//*[@class="menu"]/div[4]').click()
        print(2)
        # self._driver.switch_to_window(num[0])
        right = self.find(By.XPATH, '//*[@class="el-icon el-icon-arrow-right"]')
        self._driver.execute_script("arguments[0].click()",right)
        element = self._driver.execute_script("return location.href")
        return Grade(self._driver)
