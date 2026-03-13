from utils import DriverUtils,el_is_exist_by_text
from selenium.webdriver.common.by import By
from page.login_page import LoginPage
from page.search_page import SearchPage
import time
class TestAddCat():

    def setup_class(self):
        self.driver = DriverUtils.get_driver()

    def setup_method(self):
        """每个方法的起点-回到首页开始"""
        self.driver.get("http://localhost/index.php/Home/index/index")

    def teardown_class(self):
        DriverUtils.quit_driver()

    def test_add_cat(self):
        # 先登录
        login = LoginPage()
        # 找到登录按钮
        DriverUtils.get_driver().find_element(By.XPATH,"//*[text()='登录']").click()
        login.tp_login("15801010201","123456","8888")
        # 搜索加入购物车
        search = SearchPage()
        msg = search.tp_search_to_add("手机")
        time.sleep(0.5)
        assert "添加成功" in msg