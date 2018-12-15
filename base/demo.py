import sys

def base_screen():  # 截图
    aa = sys._getframe(0).f_code.co_name
    print(aa)


base_screen()

