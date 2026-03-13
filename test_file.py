from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class TestFile:

    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def updateFile(self):
        # 找到按钮
        file_btn = self.driver.find_element(By.ID,"file")
        # input-type=file
        file_btn.send_keys(r"C:\Users\lusir\Desktop\软件测试\TpSHOP项目\data\20200309182842_FaPBY.jpeg")

if __name__ == "__main__":
    test = TestFile()
    time.sleep(2)
    test.driver.get(r"file:///C:/Users/lusir/Desktop/%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95/TpSHOP%E9%A1%B9%E7%9B%AE/%E4%B8%8A%E4%BC%A0%E6%96%87%E4%BB%B6%E6%B5%8B%E8%AF%95.html")
    test.updateFile()
    time.sleep(2)
