
from Pages.basePage import BasePage
from Common import elementsLoc
class AlertPage(BasePage):
    pass

class UnloginError(BasePage):

    def is_appear(self):
        return self.is_element_exist('很抱歉，你将被登出，请重新登录','用户未登录')

    def again_login(self):
        self.find_Element_click('id',elementsLoc.comfirm,'用户未登录')

    def cancel_lgoin(self):
        self.find_Element_click('id',elementsLoc.cancel,'用户未登录')

class AllowPermissions(BasePage):

    def is_appear(self):
        #模糊查询
       # driver.find_element_by_xpath('//*[contains(@text, "注册/登录")]').click()
        return self.is_element_exist('是否允许来言英语学生录制音频？',None)

    def allow_recording(self):
        self.find_Element_click('id',elementsLoc.allow_btn,'音频权限')

    def deny_recording(self):
        self.find_Element_click('id',elementsLoc.deny_btn,'音频权限')


class PrivacyWindow(BasePage):

    def is_appear(self):
        return self.is_element_exist('',None)

    def allow_privacy(self):
        return True


class UpdateApp(BasePage):

    def is_appear(self):
        return self.is_element_exist('','更新')

    def update_app_winodw(self):
        return True

class CommitExercise(BasePage):


    def is_appear(self):
        return self.is_element_exist('报告生成后将无法继续答题，是否确定生成报告？','提交答案')

    def again_commit(self):
        self.find_Element_click('id',elementsLoc.comfirm,'提交练习题答案')



class ReportError(BasePage):

    def is_appear(self):
        return self.is_element_exist('继续生成报告','生成报告中断')

    def again_report(self):
        self.find_Element_click('id',elementsLoc.again_report_tv,'生成报告中断')

    def exit_get_report(self):
        self.find_Element_click('id',elementsLoc.exit_report_tv,'生成报告中断')

