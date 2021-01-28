import unittest
import logging
from Pages.Login.pwdLoginPage import PwdLoginPage
from Driver.driver import AndroidDriver
from Pages.Login.codePage import CodePage
from Pages.assignmentsPage import ExercisePage
from Pages.Login.loginPage import LoginPage
from Pages.Profile.profilePage import ProfilePage
import mgsConfig
from Pages.basePage import BasePage
from Common import elementsLoc
from Pages.Login.forgetPwdPage import ForgetPwdPage
from Pages.Profile.setNewPwdPage import SetNewPwdPage
from Pages.assignmentsPage import AssignmentsPage
from Pages.Profile.settingPage import SettingPage
logger = logging.getLogger("StreamLogger")
logger.setLevel("INFO")

class LoginTest(unittest.TestCase):
    '''短信登录-账号登录-忘记密码'''
    def setUp(self) :
        AndroidDriver().instance().connect(4723)

    def test01_sms_login(self):
        LoginPage().run_sms_login('02128148035')
        self.assertTrue(BasePage().success_into(elementsLoc.mobile_tv,'短信验证码注册登录'),'短信验证码登录页')

    def test02_sms_login(self,):
        CodePage().run_code_page('123456')
        self.assertTrue(BasePage().success_into(elementsLoc.navtitle_tv,'短信验证码注册登录'),'短信验证码登录页')

    def test03_sms_login(self):
        AssignmentsPage().goto_profilePage()
        ProfilePage().goto_settingPage()
        SettingPage().goto_logout()
        self.assertTrue(BasePage().success_into(elementsLoc.loginTips_tv,'设置'),'点击退出')

    def test04_pwd_login(self):
        LoginPage().pwd_login()
        self.assertTrue(BasePage().success_into(elementsLoc.loginTips_tv,'账号登录'),'进入账号登录页面')

    def test05_pwd_login(self):
        PwdLoginPage().run_pwd('14764367743', '111111qq', None)
        self.assertTrue(BasePage().success_into(elementsLoc.navtitle_tv,'密码登录'),'账号密码登录')

    def test06_pwd_login(self):
        AssignmentsPage().goto_profilePage()
        ProfilePage().goto_settingPage()
        SettingPage().goto_logout()
        self.assertTrue(BasePage().success_into(elementsLoc.loginTips_tv,'设置'),'点击退出')

    def test07_forgetPwd(self):
        ForgetPwdPage().run_forgetPwd('02128148033', '123456')
        self.assertTrue(BasePage().success_into(elementsLoc.setNewPwd_TV, '忘记密码'), '进入忘记密码页面')


    def test08_forgetPwd(self):
        SetNewPwdPage().run_setNewPwd('111111qq')
        self.assertTrue(BasePage().success_into(elementsLoc.navtitle_tv, '设置新密码'), '设置新密码登录')

    def test09_forgetPwd(self):
        AssignmentsPage().goto_profilePage()
        ProfilePage().goto_settingPage()
        SettingPage().goto_logout()
        self.assertTrue(BasePage().success_into(elementsLoc.loginTips_tv,'设置'),'点击退出')

if __name__ == '__main__':
    unittest.main()
    login_testsuite = unittest.TestSuite()
    # login_testsuite.addTest(LoginTest('test01_sms_login'))
    # login_testsuite.addTest(LoginTest('test02_sms_login'))
    # login_testsuite.addTest(LoginTest('test03_sms_login'))
    # login_testsuite.addTest(LoginTest('test01_pwd_login'))
    # login_testsuite.addTest(LoginTest('test02_pwd_login'))

    # login_testsuite.addTest(ForgetPwdTest('test01_forgetPwd'))
    # login_testsuite.addTest(ForgetPwdTest('test02_forgetPwd'))
    runner = unittest.TextTestRunner()
    runner.run(login_testsuite)
