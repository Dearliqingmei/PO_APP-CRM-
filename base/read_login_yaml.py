import yaml
import os

# path=os.path.dirname(__file__)+'/..'
# print(path)

# path="../"+"data"+os.sep+"login.yaml"
# print(path)

class Readlogin():

    #第一种（标准）(无论键为什么都可以使用)
    def __init__(self,filename):
        self.path=os.getcwd() + os.sep + "data" + os.sep + filename

    def read_login(self):
        with open(self.path, "r", encoding="utf-8") as f:
            data_login = yaml.load(f)
            return data_login

    # 第二种
    def read_login1(self, filename):
        list_login = []
        self.path = os.getcwd() + os.sep + "data" + os.sep + filename
        with open(self.path, "r", encoding="utf-8") as f:
            data_login = yaml.load(f)
            # return data_login
            for data in data_login.values():
                list_login.append((data["username"], data["password"]))
            return list_login
