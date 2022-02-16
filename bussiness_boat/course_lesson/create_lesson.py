from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Test_create_lession():
    def setup(self):
        options=Options()
        options.debugger_address="127.0.0.1:9222"
        self.driver=webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://test-boat.codemao.cn/codeMaoLesson")

    @pytest.mark.parametrize("a,b",[("郭的测试课包one","one的简介"),("郭的测试课包two","two的简介"),("郭的测试课包three","three的简介")])
    def test_one(self, a, b):
        sleep(3)
        self.driver.find_element_by_id("tab-1").click()
        self.driver.find_element_by_xpath("//*[@class='btnWarp']/button[1]").click()
        self.driver.find_element_by_xpath("//*[@class='el-form el-form--label-left']//input").send_keys(a)
        self.driver.find_element_by_xpath("//*[@class='el-form el-form--label-left']//textarea").send_keys(b)
        self.driver.find_element_by_xpath("//*[@class='el-form el-form--label-left']//button").click()
        self.driver.find_element_by_xpath("//*[@class='default_avatar_div']/div[1]/img").click()
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/span/button").click()
        self.driver.find_element_by_xpath('//*[@id="pane-1"]/div/div[7]/div/div[3]/span/button[2]').click()

    # 把产生的测试脏数据删除。
    @pytest.mark.skip
    @pytest.mark.parametrize("a",["郭的测试课包one","郭的测试课包two","郭的测试课包three"])
    def test_delete(self,a):
        sleep(3)
        self.driver.find_element_by_id("tab-1").click()
        self.driver.find_element_by_xpath('//*[@id="pane-1"]/div/div[2]/div[1]/input').send_keys(a)
        self.driver.find_element_by_xpath('//*[@id="pane-1"]/div/div[2]/div[1]/div/button').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="pane-1"]/div/div[4]/div[3]/table/tbody/tr/td[6]/div/button[3]').click()
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()

    # fixture，module用法
    def test_search(self):
        pass

