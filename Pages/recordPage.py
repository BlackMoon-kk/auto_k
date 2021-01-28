from Pages.basePage import BasePage
from Pages.alertPage import AlertPage
from Pages.simulationPage import SimulationPage,Option
from Common import elementsLoc
class RecordPage(BasePage):

    # 设定系数
    a = 540.0 / 1080
    b = 2030 / 2076
    def get_elements_text(self):
        title_msg = self.find_Element('id',elementsLoc.navtitle_tv,elementsLoc.view).text

    def into_recording(self):
        #这里要判断权限弹窗
        # AlertPage().allow_recording()
        self.find_Element_click('id',elementsLoc.record_btn,elementsLoc.view)

    def back_click(self):
        self.find_Element_click('id',elementsLoc.back_iv,elementsLoc.view)

    def stop_recording(self):
        # 获取当前手机屏幕大小X,Y
        X, Y = self.get_window_size()
        self.driver.tap([(self.a * X, self.b * Y)])
        # print('点击x:%s 点击y:%s 屏幕x：%s 屏幕y:%s' % (self.a * X, self.b * Y, X, Y))

    def yes_click(self):
        self.find_Element_click('id',elementsLoc.yes_btn,elementsLoc.view)
        SimulationPage().run()

    def run_record(self):
        self.into_recording()
        self.wait_little_second(2)
        self.stop_recording()
        self.yes_click()


if __name__ == '__main__':
    RecordPage().run_record()
