
from Course_center.page_object.debug import Index
from Course_center.page_object.index_cmp import CMP
from Course_center.base.base_page import BasePage
from selenium.webdriver.common.by import By
import pytest
import allure
import pytest_assume



class TestRegister:
    def setup(self):
        # self.index = Index()
        self.cmp_test= CMP()

    @allure.testcase("进入点猫编程平台")
    # @pytest.mark.skip
    def test_index(self):
        # self.index.goto_login().goto_register().register()
        # self.index.goto_register().register()
        cmp = self.cmp_test.goto_cmp()
        element = cmp.cmp_true().find(By.XPATH,'//*[@class="entry el-row"]')
        # print(element)
        #pytest-assume这是一个第三方的插件
        pytest.assume(element is not None)
        # assert register.register_true("15813816319","567890","123456a")

    @allure.step("课程中心")
    def test_index_course(self):
        courseManage = self.cmp_test.goto_cmp().cmp_true().goto_courseManage()
        print(courseManage)
        assert "courseManage" in courseManage

    # @pytest.mark.parametrize("a",["班级一"])
    def test_create_class(self):
        self.cmp_test.goto_cmp().cmp_true().goto_courseManage().grade_ture().create_grade()






