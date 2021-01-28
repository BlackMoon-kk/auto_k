
from Pages.basePage import BasePage


class ReportPage(BasePage):
    #  顶部固定元素
    back_iv = 'com.liulishuo.kion:id/iv_nav_left'
    navtitle_tv = 'com.liulishuo.kion:id/tv_nav_center'

    def successful_report(self):
        return self.is_element_exist('教材练习报告总览',None)

    def back_assignmentsPage(self):
        self.find_Element_click('id',self.back_iv,'报告页')
