
from Driver.driver import AndroidDriver
from Pages.basePage import BasePage
from Pages.assignmentsPage import ExercisePage
from Common import elementsLoc
class CodePage(BasePage):
    def check_code(self,code):
        self.find_Element_send('id',elementsLoc.code_et,code,elementsLoc.view)
        self.take_screenShot(elementsLoc.view)

    def click_back(self):
        self.find_Element_click('id',elementsLoc.back_iv,elementsLoc.view)

    def get_mobile_msg(self):
        return self.find_Element('id',elementsLoc.mobile_tv,elementsLoc.view).text

    def get_current_view(self):
        elementsLoc.view = '验证码页面'
        return elementsLoc.view

    def run_code_page(self,code):
        self.check_code(code)

if __name__ == '__main__':
    CodePage().run_code_page('123456')