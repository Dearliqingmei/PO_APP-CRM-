import sys
import os
sys.path.append(os.getcwd())

from page.page import *
import pytest
from base.get_driver import *
from base.read_login_yaml import *
from base.read_login_txt import *


def get_login_data():
    #yaml
    list_login = []
    login_data=Readlogin("login.yaml").read_login()
    for data in login_data.values():
        list_login.append((data["username"],data["password"]))
    return list_login

    #txt
    # data_list = list()
    # login_data = Readlogintxt("login1.txt").read_login_txt()
    # for read_txt in data_login:
    #     data_list.append(tuple(read_txt.strip().split(",")))
    # return data_list

class Testlogin():

    def setup(self):
        self.login=Page(get_driver())


    def teardown(self):
        self.login.driver.quit()

    @pytest.mark.parametrize("username,password",get_login_data())
    def test_login(self,username,password):
        self.login.page_send_username(username)
        self.login.page_send_password(password)
        self.login.page_click()
        try:#（断言）
            assert self.login.page_on_logintxt("业绩目标")
            print("登陆成功！")
            self.login.base_get_screen()
        except:
            print("%s,%s登陆失败!" %(username, password))
            self.login.base_get_screen()
        # self.login.driver.get_screenshot_as_file("../screenhot/Image01.jpg")

