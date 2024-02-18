#驱动工具类

#定义驱动工具
from selenium  import webdriver

class DriverUtil:

    _driver = None   #私有化变量
    #获取浏览器驱动对象，并完成初始化操作
    @classmethod  # 为了使方法方便调用，将他定义为类方法（或者静态方法）
    def get_driver(cls):
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(30)
            cls._driver.get("https://datax-test.health.rabbitpre.com/index.html#/datax/job/jobInfo")
        return cls._driver
    #关闭驱动对象
    # @classmethod   # 为了使方法方便调用，将他定义为类方法
    # def quit_driver(cls):
    #     if cls._driver:
    #         cls._driver.close()
    #         cls._driver = None

if __name__ == '__main__':
    DriverUtil.get_driver()