from Common import elementsLoc
from Pages.basePage import BasePage


class SetNewPwdPage(BasePage):


    def get_current_view(self):
        elementsLoc.view = self.get_title('id',elementsLoc.setNewPwd_TV,None)
        return elementsLoc.view

    def setNewPwd01(self,pwd):
        self.find_Element_send('id',elementsLoc.newPwd_et,pwd,elementsLoc.view)
        self.find_Element_click('id',elementsLoc.newPwd_login_tv,elementsLoc.view)
        self.take_screenShot(elementsLoc.view)

    def run_setNewPwd(self,pwd):
        self.get_current_view()
        self.setNewPwd01(pwd)


