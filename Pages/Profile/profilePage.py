from Pages.basePage import BasePage
from Pages.assignmentsPage import ExercisePage
from Pages.Profile.settingPage import SettingPage
from Pages.alertPage import AlertPage
from Common import elementsLoc
class ProfilePage(BasePage):
    view = u'个人中心'



    def goto_classPage(self):
        self.find_Element_click('id',elementsLoc.myclass,elementsLoc.view)

    def goto_skuPage(self):
        self.find_Element_click('id',elementsLoc.sku_card,elementsLoc.view)

    def goto_cityPage(self):
        self.find_Element_click('id',elementsLoc.student_city,elementsLoc.view)

    def goto_studentcodePage(self):
        self.find_Element_click('id',elementsLoc.student_code,elementsLoc.view)

    def goto_settingPage(self):
        self.find_Element_click('id',elementsLoc.setting_ll,elementsLoc.view)

    def get_current_view(self):
        elementsLoc.view = self.get_title('id',elementsLoc.loginTips_tv,None)
        return elementsLoc.view

if __name__ == '__main__':
    ProfilePage().goto_settingPage()