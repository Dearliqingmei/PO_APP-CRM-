from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import sys
import os
import time
# from selenium import webdriver

class Base(object):

    def __init__(self, driver):
        self.driver = driver


    def base_find_element(self,loc,timeout=30, poll=0.5):
        try:
            WebDriverWait(self.driver,timeout,poll_frequency=poll).until(EC.visibility_of_element_located(loc))
            # return WebDriverWait(self.driver, timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))
            return self.driver.find_element(*loc)
        except:
            print(u"%s页面中未能找到%s元素" % (self, loc))

    # def base_send_keys(self, loc, value, clear_first=True, click_first=True):
    #     try:
    #         loc = getattr(self, "_%s" % loc)  # getattr相当于实现self.loc
    #         if click_first:
    #             self.base_find_element(*loc).click()
    #         if clear_first:
    #             self.base_find_element(*loc).clear()
    #             self.base_find_element(*loc).send_keys(value)
    #     except AttributeError:
    #         print(u"%s页面中未能找到%s元素" % (self, loc))

    def base_send_keys(self, loc, value,first_send=True,first_clear=True):
        try:
            if first_send:
                self.base_find_element(loc).send_keys(value)
            elif first_clear:
                self.base_find_element(loc).clear()
                self.base_find_element(loc).send_keys(value)
        except AttributeError:
            print(u"%s页面中未能找到%s元素" % (self, loc))

    def base_click(self,loc):
        self.base_find_element(loc).click()

    def base_get_screen(self):#截图
         # self.base_screen = sys._getframe(0).f_code.co_name
         self.path_screen = os.getcwd() + os.sep + "screenhot" + os.sep+("%s.jpg"%time.strftime("%Y-%m-%d %H_%M_%S"))
         self.driver.get_screenshot_as_file(self.path_screen)





