from base.base_page import BasePage
from utils import DriverUtils
from selenium.webdriver.common.by import By
class AdminIndexPage(BasePage):
    def __init__(self):
        self.driver = DriverUtils.get_driver()
        # //*[@class='commfunc-con']/a
        self.goodControll = (By.XPATH,"//*[text()='商城']")
        # 商品列表子菜单按钮
        self.goodlist = (By.XPATH,"//a[@data-param='goodsList|Goods']")

    def tp_admin_click_goodsControll(self):
        """点击商品操作"""
        """TOUD: 切换frame? 要找到元素才能切换 self.switch_frame(self.find_el(self.iframe))"""
        self.find_el(self.goodControll).click()
        self.find_el(self.goodlist).click()

