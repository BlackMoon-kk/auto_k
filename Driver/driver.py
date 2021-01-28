from appium import webdriver
from selenium.common.exceptions import WebDriverException

import logging
logger = logging.getLogger("StreamLogger")
logger.setLevel("DEBUG")
android_driver = webdriver.Remote

class AndroidDriver():
    # 这边改成单例模式，调用实例的时候用AndroidDriver.instance.方法名
    # 单例模式的话可以保证每次实例话这个实例，都是同一个对象，节省资源
    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(AndroidDriver, "_instance"):
            AndroidDriver._instance = AndroidDriver(*args, **kwargs)
        return AndroidDriver._instance

    def __init__(self):
        # self.device = device
        # 设置一个flag只需要connect 一次
        self.connect_flag = False
        self.desired_caps = {
            "platformName": "Android",
            "deviceName": '988ed533434b574537',
            "appPackage": "com.liulishuo.kion",
            "appActivity": "com.liulishuo.kion.SplashActivity",
            # 'platformVersion':'10.0',
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'noReset':True,
            'newCommandTimeout':'6000',
            # 'app':'/Users/qiannanli/Documents/kion_student_dev_1.8.3_20200403103639.apk'
        }


    def connect(self, port):
        if self.connect_flag:
            logger.info("connect already")
            return
        url = 'http://localhost:%s/wd/hub' % str(port)
        logger.debug(url)
        try:
            global android_driver
            android_driver = webdriver.Remote(url, self.desired_caps)
            android_driver.implicitly_wait(20)
            logger.debug("启动接口为：%s,手机ID为：" % (str(port)))
            self.connect_flag = True
        except Exception:
            logger.info("appium 启动失败")
            raise


    def get_driver(self):
        return android_driver
    #
    # def quit(self):
    #     android_driver.quit()
