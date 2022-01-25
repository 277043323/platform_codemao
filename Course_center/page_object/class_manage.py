import sys

from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Course_center.base.base_page import BasePage
import time

# sys.path.append()


class ClassManage(BasePage):
    def create_grade(self,b):
        #方法一：失败
        # self._driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",element,"border:2px solid red")
        # action = ActionChains(self._driver).move_to_element(element).move_by_offset(5,5).click().perform()
        #方法二：使用selenium原生的api无发顶级生效，就用js，进行点击
        ele = self.find(By.XPATH,'//*[@class="card-head"]//i')
        self._driver.execute_script("arguments[0].click();", ele)
        # # ele = self.find(By.CSS_SELECTOR,'.el-icon-circle-plus')
        #使用下面的方法可以给元素添加样式
        # self._driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",ele,"border:2px solid red")
        # action = ActionChains(self._driver)
        # # time.sleep(3)
        # # action.move_to_element(ele).move_by_offset(5,5).click().perform()
        # # action.click_and_hold(ele).perform()
        self.find(By.XPATH,'//*[@class="modal-body"]//input').send_keys("满员班级")
        # print(self._driver.window_handles)
        collo= self.find(By.XPATH,'//*[@class="modal-content"]//button')
        self._driver.execute_script("arguments[0].click();",collo)

        no = self.find(By.XPATH,'//*[@class="foot"]/button[2]')
        self._driver.execute_script("arguments[0].click()",no)

        to=self.find(By.XPATH,'//*[@class="el-button el-button--primary el-button--small"]')
        self._driver.execute_script("arguments[0].click()", to)

        self.find(By.XPATH,'//*[@class="el-textarea el-input--mini"]/textarea').send_keys(b)

        kk=self.find(By.XPATH,'//*[@class="foot"]//button')
        self._driver.execute_script("arguments[0].click()", kk)

        self._driver.refresh()






