
from Driver.driver import AndroidDriver
from selenium.webdriver.common.by import By
import mgsConfig
from Pages.basePage import BasePage
from Pages.Login.codePage import CodePage
from Pages.Login.pwdLoginPage import PwdLoginPage
from Common import elementsLoc
class LoginPage(BasePage):
    #  driver定义在这里的话，loginTest import这个文件的时候这句话就会执行，也就是早于setup函数，
    # 导致你下面sms_login 获取到的driver是在connect之前的
    # driver = AndroidDriver.instance().get_driver()

    def sms_login(self,mobile):
        self.find_Element_send('id',elementsLoc.mobile_et,mobile,elementsLoc.view)
        self.find_Element_click('id',elementsLoc.agree_tv,elementsLoc.view)
        self.take_screenShot(elementsLoc.view)
        self.find_Element_click('id',elementsLoc.comite_tv,elementsLoc.view)

    def sms_login_fail(self,mobile,msg):
        self.find_Element_send('id',elementsLoc.mobile_et,mobile,elementsLoc.view)
        self.find_Element_click('id',elementsLoc.agree_tv,elementsLoc.view)
        self.find_Element_click('id',elementsLoc.code_tv,elementsLoc.view)
        self.get_Toast(msg)
        self.take_screenShot(u'错误手机号登录失败')

    def pwd_login(self):
        self.find_Element_click('id',elementsLoc.type_tv,elementsLoc.view)

    def get_current_view(self):
        elementsLoc.view = self.get_title('id',elementsLoc.loginTips_tv,None)
        return elementsLoc.view

    def run_sms_login(self, mobile):
        self.get_current_view()
        self.sms_login(mobile)

if __name__ == '__main__':
    LoginPage().run_sms_login('02128148034')