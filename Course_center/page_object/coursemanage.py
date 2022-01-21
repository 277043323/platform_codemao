from selenium.webdriver.common.by import By

from Course_center.base.base_page import BasePage

from Course_center.page_object.grade import Grade

class CourseManage(BasePage):
    def goto_courseManage(self):
        self.find(By.XPATH, '//*[@class="menu"]/div[4]').click()
        self.find(By.XPATH, '//*[@class="el-icon el-icon-arrow-left"]').click()
        element = self._driver.execute_script("return location.href")
        return Grade(self._driver)
