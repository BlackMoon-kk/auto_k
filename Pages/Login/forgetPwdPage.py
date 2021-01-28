
from Common import elementsLoc
from Pages.basePage import BasePage

from Pages.Login.loginPage import LoginPage
from Pages.Login.pwdLoginPage import PwdLoginPage
from Pages.Login.codePage import CodePage
from Driver.driver import AndroidDriver
from Pages.Profile.setNewPwdPage import SetNewPwdPage
class ForgetPwdPage(BasePage):




    def goto_forget01(self,mobile):
        LoginPage().pwd_login()
        PwdLoginPage().goto_forgetPwd()
        self.get_current_view()
        self.find_Element_send('id',elementsLoc.mobile_et,mobile,None)
        self.find_Element_click('id',elementsLoc.agree_tv,elementsLoc.view)
        self.find_Element_click('id',elementsLoc.comite_tv,elementsLoc.view)
        self.take_screenShot(elementsLoc.view)


    def goto_forget02(self,code):
        CodePage().run_code_page(code)


    def get_current_view(self):
        elementsLoc.view = self.get_title('id',elementsLoc.loginTips_tv,None)
        return elementsLoc.view

    def run_forgetPwd(self,mobile,code):
        self.goto_forget01(mobile)
        self.goto_forget02(code)
        # return SetNewPwdPage()

if __name__ == '__main__':
    ForgetPwdPage().run_forgetPwd('02128148038','123456')

