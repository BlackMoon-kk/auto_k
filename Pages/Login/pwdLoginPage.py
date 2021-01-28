from Pages.basePage import BasePage
# from Pages.Login.loginPage import LoginPage
from Common import elementsLoc
import mgsConfig
class PwdLoginPage(BasePage):

    def pwd_login(self,mobile,pwd):
        self.find_Element_send('id',elementsLoc.mobile_et,mobile,elementsLoc.view)
        self.find_Element_send('id',elementsLoc.pwd_et,pwd,elementsLoc.view)
        self.find_Element_click('id',elementsLoc.agree_tv,elementsLoc.view)
        self.get_current_view()
        self.take_screenShot(elementsLoc.view)
        self.find_Element_click('id',elementsLoc.comite_tv,elementsLoc.view)

    def pwd_login_fail(self,mobile,pwd,msg):
        self.find_Element_send('id',elementsLoc.mobile_et,mobile,elementsLoc.view)
        self.find_Element_send('id',elementsLoc.pwd_et,pwd,elementsLoc.view)
        self.find_Element_click('id',elementsLoc.agree_tv,elementsLoc.view)
        self.find_Element_click('id',elementsLoc.comite_tv,elementsLoc.view)
        self.get_Toast(msg)

    def get_current_view(self):
        elementsLoc.view = self.get_title('id',elementsLoc.loginTips_tv,None)
        return elementsLoc.view

    def goto_forgetPwd(self):
        self.find_Element_click('id',elementsLoc.forgetPwd_tv,None)





    def run_pwd(self,mobile,pwd,msg):
        self.pwd_login(mobile,pwd)

if __name__ == '__main__':
    PwdLoginPage().run_pwd('02128148037','111111qq',mgsConfig.pwd_error_msg)



