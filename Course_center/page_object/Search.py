from selenium.webdriver.common.by import By

from Course_center.base.base_page import BasePage


class Search_OP(BasePage):
    def search(self,a):
        self.find(By.XPATH,'//*[@class="el-input el-input--mini el-input--suffix"]/input').send_keys(a)
        em = self.find(By.XPATH,'//*[@class="button-div"]//button[1]')
        self._driver.execute_script("arguments[0].click()",em)