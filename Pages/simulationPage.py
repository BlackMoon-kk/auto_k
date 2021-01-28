from Pages.basePage import BasePage
from Common import elementsLoc
class SimulationPage(BasePage):
    def run(self):
        Option().run()

class Option(BasePage):

    a = 960/1080
    b = 2020/2076
    def is_appear_option(self):
        result = self.is_element_exist('A. ',None)
        skip_result = self.is_element_exist(elementsLoc.skip_iv,None)
        print('出现跳过按钮：%s 出现选项：%s' %(skip_result,result))
        if result:
            self.option1()

        if skip_result :
           self.wait_little_second(1)
           X, Y = self.get_window_size()
           self.driver.tap([(X / 2, Y - 20)])
           print('点击x:%s 点击y:%s 屏幕x：%s 屏幕y:%s' % (self.a * X, self.b * Y, X, Y))


    def option1(self):
        option_list = self.find_Elements('xpath',elementsLoc.option_loc,elementsLoc.view)
        for option in option_list:
            option.click()

    def run(self):
        i = 0
        while i <100:
            print('循环第%s ' %i)
            self.is_appear_option()
            i = i+1
