from Pages.basePage import BasePage

from Common import elementsLoc

class SettingPage(BasePage):

    def goto_logout(self):
        self.find_Element_click('id', elementsLoc.logout_tv,elementsLoc.view)
        self.find_Element_click('id',elementsLoc.again_report_tv,elementsLoc.view)

    def cancel(self):
        self.find_Element_click('id',elementsLoc.exit_report_tv,elementsLoc.view)


    def get_current_view(self):
        elementsLoc.view = self.get_title('id',elementsLoc.loginTips_tv,None)
        return elementsLoc.view

