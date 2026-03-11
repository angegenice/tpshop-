from utils import DriverUtils,build_data
from page.admin_login_page import AdminLoginPage
from page.admin_index_page import AdminIndexPage
from page.admin_add_goods_page import AdminAddGoodsPage
from selenium.webdriver.common.by import By
import pytest
import time
class TestAddGoods():

    def setup_class(self):
        self.driver = DriverUtils.get_driver()

    def teardown_class(self):
        DriverUtils.quit_driver()

    def setup_method(self):
        self.driver.get("http://localhost/index.php/Admin/Index/index")

    @pytest.mark.parametrize(("g_name","caregory_one","caregory_two","caregory_three","desc","band","supplier","sell","market_price"),build_data("tp_good_data"))
    def test_add_goods(self,g_name,caregory_one,caregory_two,caregory_three,desc,band,supplier,sell,market_price):
        admin = AdminLoginPage()
        admin.tp_admin_login("admin","123456","8888")
        admin.find_el((By.NAME,"submit")).click()
        # 后台首页点击操作
        admin_index = AdminIndexPage()
        admin_index.tp_admin_click_goodsControll()
        # 添加商品对象操作
        good = AdminAddGoodsPage()
        good.tp_add_good(g_name,caregory_one,caregory_two,caregory_three,desc,band,supplier,sell,market_price)
        time.sleep(1)