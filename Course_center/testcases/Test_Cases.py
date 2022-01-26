import sys
import yaml
from Course_center.page_object.debug import Index
from Course_center.page_object.index_cmp import CMP
from Course_center.base.base_page import BasePage
from selenium.webdriver.common.by import By
import pytest
import allure
import pytest_assume

print(sys.path)


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
        # pytest-assume这是一个第三方的插件
        pytest.assume(element is not None)
        # assert register.register_true("15813816319","567890","123456a")

    @allure.step("课程中心")
    def test_index_course(self):
        courseManage = self.cmp_test.goto_cmp().cmp_true().goto_courseManage()
        # print(courseManage)
        element = courseManage._driver.execute_script("return location.href")
        assert "courseManage" in element

    @pytest.mark.skip
    @pytest.mark.parametrize("a",yaml.safe_load(open("../config/class.yaml","rb")))
    def test_create_class(self,a):
        self.cmp_test.goto_cmp().cmp_true().goto_courseManage().grade_ture().create_grade(a)
        # print(el)

    # 批量添加学生，含生僻字的学生
    @pytest.mark.skip(reason='no way of currently testing this')
    @pytest.mark.parametrize("b",[str(yaml.safe_load(open("../config/class_student.yaml","rb"))).replace(' ','\n')])
    def test_add_student(self,b):
        self.cmp_test.goto_cmp().cmp_true().goto_courseManage().grade_ture().create_grade(b)

    # 设置测试用例的执行顺序
    @pytest.mark.skip
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a", yaml.safe_load(open("../config/num_class.yaml","rb")))
    def test_search_class(self,a):
        self.cmp_test.goto_cmp().cmp_true().goto_courseManage().grade_ture().create_grade().search(a)
















