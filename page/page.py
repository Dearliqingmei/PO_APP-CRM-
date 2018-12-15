from base.base import *
import page
from base.read_login_yaml import *

class Page(Base):

    def page_send_username(self,username):
        self.base_send_keys(page.loc_username,username)

    def page_send_password(self,password):
        self.base_send_keys(page.loc_password,password)

    def page_click(self):
        self.base_click(page.loc_click)

    def page_on_logintxt(self,success_txt):
        return success_txt in self.base_find_element(page.loc_login_txt).text
