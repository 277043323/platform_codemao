from selenium.webdriver.common.by import By

from Course_center.base.base_page import BasePage


class course_Teaching(BasePage):
    def add_class(self):
        self.find(By.XPATH,'//*[@class="class-content"]/li[1]//button').click()
        # self.find(By.XPATH,'//*[@class="select-empty"]//button').click()
