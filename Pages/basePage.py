import logging
from Driver.driver import AndroidDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
import os
import time, datetime
from selenium.webdriver.common.by import By
import re
logger = logging.getLogger("StreamLogger")
logger.setLevel("INFO")


class BasePage:

    def __init__(self):
        AndroidDriver().instance().connect(4723)
        self.driver = AndroidDriver.instance().get_driver()

    '''封装查找元素方法，并且返回页面元素'''
    '''如果有弹窗之类的找不到元素，则关闭弹窗再查找元素'''

    def get_title(self,type,loc,view):
        string = self.find_Element(type, loc, view).text
        result = ''.join(re.findall('[\u4e00-\u9fa5]', string))
        print(result)
        return result

    def success_into(self,loc,title):
        if self.get_title('id', loc, None) != title:
            return True
        else:
            return False

    def find_Element(self, type, loc , view):
        '''
        method explain:查找某个元素
        parameter explain: 【type】 取值的类型包括：id\name\class_name...   【loc】根据type的类型给值
        Usage:
            device.find_Element('name',"我的認證")
        '''
        logging.info("执行--------find_Element-------方法")
        try:
            i = 1
            while i < 10:
                try:
                    if type == 'id':
                        return self.driver.find_element(By.ID, loc)

                    elif type == 'name':
                        return self.driver.find_element(By.NAME, loc)

                    elif type == 'xpath':
                        return self.driver.find_element(By.XPATH,loc)
                except Exception as e:
                    logging.info("第%s没有定位到元素，type:%s--loc:%s" % (str(i), type, loc))
                    logging.warning("第%s没有定位到元素，定位方式: " + format(loc) + "_errmsg: %s" % (str(i)), e)
                    self.swipe_up(1000, i)
                    i = i + 1
        except Exception as e:
            logging.error("此处已抛异常---------------find_Element")
            self.take_screenShot(view)
            assert 'find_Element'

    def find_Elements(self, type, loc , view):
        '''
        method explain:查找某个元素
        parameter explain: 【type】 取值的类型包括：id\name\class_name...   【loc】根据type的类型给值
        Usage:
            device.find_Element('name',"我的認證")
        '''
        logging.info("执行--------find_Element-------方法")
        try:
            i = 1
            while i < 10:
                try:
                    if type == 'id':
                        return self.driver.find_elements(By.ID, loc)

                    elif type == 'name':
                        return self.driver.find_elements(By.NAME, loc)

                    elif type == 'xpath':
                        return self.driver.find_elements(By.XPATH,loc)

                    elif type == 'class':
                        return self.driver.find_elements(By.CLASS_NAME, loc)

                except Exception as e:
                    logging.info("第%s没有定位到元素，type:%s--loc:%s" % (str(i), type, loc))
                    logging.warning("第%s没有定位到元素，定位方式: " + format(loc) + " errmsg: %s" % (str(i)), e)
                    self.swipe_up(1000, i)
                    i = i + 1
        except Exception as e:
            logging.error("此处已抛异常---------------find_Element")
            self.take_screenShot(view)
            assert 'find_Element'

    def take_screenShot(self, name="takeShot"):
        '''
        method explain:获取当前屏幕的截图
        parameter explain：【name】 截图的名称
        Usage:
            device.take_screenShot(u"个人主页")   #实际截图保存的结果为：2018-01-13_17_10_58_个人主页.png
            device.take_screenShot("profile") 截图名称为英文，则不需添加U
        '''

        # 截图

        day = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        screenShots_path =  os.getcwd().split('Pages')[0]
        screenShots_path = os.path.join(screenShots_path+'/Resource/ScreenShots',day)
        # fq =os.getcwd()[:-5] +'ScreenShots\\'+day  #根据获取的路径，然后截取路径保存到自己想存放的目录下
        # print(fq)
        tm = time.strftime("_%H_%M_%S", time.localtime(time.time()))
        type = '.png'
        filename = ""
        if os.path.exists(screenShots_path):
            filename = os.path.join(screenShots_path,day+ tm + "_" + name + type)

        else:
            os.makedirs(screenShots_path)
            filename = os.path.join(screenShots_path,day + tm + "_" + name + type)
        print('截图---'+filename)
        self.driver.get_screenshot_as_file(filename)

    def get_Toast(self, message):  # 查找toast值
        '''
        method explain:查找toast的值,与find_Toast实现方法一样，只是不同的2种写法
        parameter explain：【text】查找的toast值
        Usage:
            device.get_Toast('再按一次退出iBer')
        '''
        logging.info("查找toast值---'%s'" % (message))
        try:
            message = '//*[@text=\'{}\']'.format(message)
            WebDriverWait(self.driver, 5, 0.5).until(
                expected_conditions.presence_of_element_located((By.XPATH, message)))
            logging.info("查找到toast----%s" % message)
            return True
        except:
            logging.error("未查找到toast----%s" % message)
            return False

    def find_Element_click(self, type, loc,view):
        '''
        method explain:查找某个元素
        parameter explain: 【type】 取值的类型包括：id\name\class_name...   【loc】根据type的类型给值
        Usage:
            device.find_Element('name',"我的認證")
        '''
        logging.info("执行--------find_Element_click-------方法")
        try:
            i = 1
            while i < 10:
                try:
                    if type == 'id':
                        return self.driver.find_element(By.ID, loc).click()

                    elif type == 'name':
                        return self.driver.find_element(By.NAME, loc).click()

                    elif type == 'xpath':
                        return self.driver.find_element(By.XPATH, loc).click()
                except Exception as e:
                    print('滑动查找' + str(i))
                    logging.info("第%s没有定位到元素，type:%s--loc:%s" % (str(i), type, loc))
                    self.swipe_up(1000, i)
                    logging.warning("第%s没有定位到元素，定位方式: " + format(loc) + "_errmsg: %s" % (str(i)), e)
                    i = i + 1
        except Exception as  e:
            logging.error("此处已抛异常---------------find_Element_click")
            self.take_screenShot(view)
            assert 'find_Element_click'

    def find_Element_send(self, type, loc, msg,view):
        '''
        method explain:查找某个元素
        parameter explain: 【type】 取值的类型包括：id\name\class_name...   【loc】根据type的类型给值
        Usage:
            device.find_Element('name',"我的認證")
        '''
        logging.info("执行--------find_element_send_key-------方法")
        try:
            i = 1
            while i < 10:
                try:
                    if type == 'id':
                        ele = self.driver.find_element(By.ID, loc).clear()
                        ele.send_keys(msg)
                        return ele

                    elif type == 'name':
                        ele = self.driver.find_element(By.NAME, loc).clear()
                        ele.send_keys(msg)
                        return ele

                    elif type == 'xpath':
                        ele = self.driver.find_element(By.XPATH, loc).clear()
                        ele.send_keys(msg)
                        return ele
                except Exception as e:
                    logging.info("第%s没有定位到元素，type:%s--loc:%s" % (str(i), type, loc))
                    logging.warning("第%s没有定位到元素，定位方式: " + format(loc) + "_errmsg: %s" % (str(i)), e)
                    self.swipe_up(1000, i)
                    i = i + 1
        except Exception as  e:
            logging.error("此处已抛异常---------------find_Element_send")
            self.take_screenShot(view)
            assert 'find_Element_send'





    def swipe_up(self, t=500, n=1):
        s = self.driver.get_window_size()
        x1 = s['width'] * 0.5  # x坐标
        y1 = s['height'] * 0.75  # 起点y坐标
        y2 = s['height'] * 0.25  # 终点y坐标
        print('手机的尺寸是： ', s)
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    # 向下滑动
    def swipe_down(self, t=500, n=1):
        s = self.driver.get_window_size()
        x1 = s['width'] * 0.5  # x坐标
        y1 = s['height'] * 0.25  # 起点y坐标
        y2 = s['height'] * 0.75  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    # 向左滑动
    def swipe_left(self, t=500, n=1):
        s = self.driver.get_window_size()
        x1 = s['width'] * 0.75
        y1 = s['height'] * 0.5
        x2 = s['width'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    # 向右
    def swipe_right(self, t=500, n=1):
        s = self.driver.get_window_size()
        x1 = s['width'] * 0.25
        y1 = s['height'] * 0.5
        x2 = s['width'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def get_window_size(self):
        # logger.info("正在准备获取当前屏幕的大小")
        try:
            size = self.driver.get_window_size()
            width = size["width"]
            height = size["height"]
            logger.info("获取当前屏幕大小成功:宽：{}   高：{}".format(width, height))
            return width, height
        except Exception as e:
            logging.info('获取当前屏幕大小失败')

    def is_element_exist(self, element,view):
        # self.wait_little_second(1)
        source = self.driver.page_source
        # print(source)
        if element in source:
            if view != None:
                self.take_screenShot(view)
            return True
        else:
            return False

    def get_chinese(self,string):
        res1 = ''.join(re.findall('[\u4e00-\u9fa5]', string))

    def get_english(self,string):
        result = ''.join(re.findall(r'[A-Za-z]', string))


    def wait_little_second(self,some_seconds):
        time.sleep(some_seconds)
        # def wrapper(func):
        #     def deco(*args, **kwargs):
        #         logger.debug("调用进入装饰器")
        #         time.sleep(some_seconds)
        #         func(*args, **kwargs)
        #         logger.debug("结束函数调用")
        #
        #     return deco
        #
        # return wrapper

if __name__ == '__main__':
    BasePage().take_screenShot("find_Element")
