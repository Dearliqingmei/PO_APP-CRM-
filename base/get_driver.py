from appium import webdriver

def get_driver():
    desired_caps={}
    # 必填-且正确
    desired_caps['platformName'] = 'Android'
    # 必填-且正确
    desired_caps['platformVersion'] = '5.1'
    # 必填
    desired_caps['deviceName'] = '192.168.18.101:5555'
    # APP包名
    desired_caps['appPackage'] = 'com.vcooline.aike'
    # 启动名
    desired_caps['appActivity'] = '.umanager.LoginActivity'
    return webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)