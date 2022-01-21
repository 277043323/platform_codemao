import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pytest
import yaml

class Test:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(4)
        self.driver.get(url='https://staging-edu.codemao.cn/')
    # def teardown(self):
    #     pass
    def test01(self):
        self.driver.find_element(By.XPATH,'//*[@class="go-class-btn"]').click()
        # element = self.driver.find_element(By.XPATH,'//*[@id="slideBgWrap"]')
        self.driver.find_element(By.XPATH,'//*[@class="ipt-group"]/input').send_keys("15813816312")
        self.driver.find_element(By.XPATH,'//*[@class="ipt-group psd-group mb40"]/input').send_keys("123456a")
        self.driver.find_element(By.XPATH,'//*[@id="loginCptBtn"]').click()
        # captcha=self.driver.find_element(By.XPATH,'//*[@class="tc-jpp-img unselectable"]')
        # ActionChains(self.driver).drag_and_drop()
        # time.sleep(3)
        # elem = self.driver.find_element(By.XPATH,'//*[@id="tcaptcha_drag_thumb"]')
        # ActionChains(self.driver).click_and_hold(elem).move_by_offset(8,0).perform()
        # ActionChains(self.driver).release(elem).perform()
        self.driver.find_element(By.XPATH,"//*[@class='go-class-btn']").click()
        self.driver.find_element(By.XPATH,'//*[@class="menu"]/div[6]').click()

    def test(self):
        param = yaml.safe_load(open('../../Course_center/config/yaml'))
        # return param
        print(param)


    @pytest.mark.parametrize('a','//*[@class="el-radio-group classWarp"]/label[1]')
    def test02(self,a):
        #课程推荐
        self.driver.find_element(By.XPATH,'//*[@class="rightWarp"]/div[1]/button[1]').click()
        self.driver.find_element(By.XPATH,a).click()
        self.driver.find_element(By.XPATH,'//*[@class="el-radio-group"]/label[1]').click()
        self.driver.find_element(By.XPATH,'//*[@class="el-button confirmBtn el-button--primary el-button--mini"]').click()




