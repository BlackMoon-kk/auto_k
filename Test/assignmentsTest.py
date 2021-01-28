
import unittest
import logging
from Driver.driver import AndroidDriver
from Pages import alertPage
from Pages.assignmentsPage import AssignmentsPage
from Pages.exercisePage import ExercisePage
from Pages.basePage import BasePage
from Common import elementsLoc
logger = logging.getLogger("StreamLogger")
logger.setLevel("INFO")

import warnings
class AssignmentsTest(unittest.TestCase):
    '''完成练习'''
    assgin_type = ''

    def setUp(self) :
        warnings.simplefilter('ignore',ResourceWarning)
        AndroidDriver().instance().connect(4723)
        #检查各种弹窗

    # def test01_check_window(self):
    #     privacy = alertPage.PrivacyWindow()
    #     if privacy.is_appear():
    #         logger.info('点击隐私协议')
    #         privacy.allow_privacy()
    #     else:
    #         logger.info('没有隐私协议')
    #
    #     update = alertPage.UpdateApp()
    #     if update.is_appear():
    #         logger.info('APP需要更新')
    #         update.update_app_winodw()
    #     return True

    def test02_goto_assignments(self):
        '''点击第一个练习判断页面'''
        AssignmentsPage().is_exercise_simulation()
        self.assertTrue(BasePage().success_into(elementsLoc.navtitle_tv,'我的练习'),'进入试卷')

    def test03_do_assignments(self):
        self.assertTrue(ExercisePage().do_exercise(),'做题过程')

    def test04_generate_report(self):
        self.assertTrue(ExercisePage().generate_report(), '生成报告过程')


if __name__ == '__main__':
    unittest.main()




