import os

class Readlogintxt():

    def __init__(self,filename_txt):
        self.path=os.getcwd()+os.sep+"data"+os.sep+filename_txt

    def read_login_txt(self):
        with open(self.path,'r',encoding='utf-8') as f:
            data_login = f.readlines()
            return data_login