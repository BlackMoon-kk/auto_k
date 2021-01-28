
from Pages.basePage import BasePage
from Common import elementsLoc

from Pages import alertPage

class ExercisePage(BasePage):

    def do_exercise(self):
        i = 1
        while i < 100:
            result = self.is_element_exist('生成报告',None)
            print('生成报告 :%s' % result)
            if result:
                self.find_Element_click('id',elementsLoc.end_submit_tv,None)
                alertPage.CommitExercise().again_commit()
                return True
            else:
                title = self.get_title('id', elementsLoc.navtitle_tv, None)
                elementsLoc.view = title
                if title == '听长音频判断正误':
                    Option().run_opntion(1,title)

                if title == '听音频选图片':
                    Option().run_opntion(2,title)

                if title == '听音频选答语':
                    Option().run_opntion(3,title)

                if title == '听音频看图片判断':
                    Option().run_opntion(1,title)

                if title == '听音频选文本':
                    Option().run_opntion(3,title)

#or and 为什么不行呢？
                if title == '看图说话':
                    Audio().run_audio(title)

                if title == '话题简述':
                    Audio().run_audio(title)

                if title == '看音标读单词':
                    Audio().run_audio(title)

                if title == '看文本朗读单词':
                    Audio().run_audio(title)

                if title == '看图片说单词':
                    Audio().run_audio(title)
                if title == '看文本朗读短语':
                    Audio().run_audio(title)
                if title == '模仿朗读':
                    Audio().run_audio(title)
                if title == '看文本朗读句子':
                    Audio().run_audio(title)
                if title == '听后记录':
                    WordHole().run_wordHole(title)
                i = i + 1


    def generate_report(self):
        self.wait_little_second(4)
        result_report = alertPage.ReportError().is_appear()
        result_back = self.is_element_exist('教材练习报告总览', None)
        if result_report:
            alertPage.ReportError().again_report()
            i = 1
            while i < 4:
                result_report = alertPage.ReportError().is_appear()
                result_back = self.is_element_exist('教材练习报告总览', None)
                print('------第%s循环 result_report：%s result_back：%s ' %(i,result_report,result_back))
                if result_report:
                    alertPage.ReportError().again_report()
                if result_back:
                    self.wait_little_second(1)
                    self.take_screenShot('报告总览页')
                    self.find_Element_click('id', elementsLoc.back_iv, None)
                    return True
                i = i + 1
            alertPage.ReportError().exit_get_report()
            return False

        if result_back:
            self.wait_little_second(1)
            self.take_screenShot('报告总览页')
            self.find_Element_click('id', elementsLoc.back_iv, None)
            return True

class Option(BasePage):


    #听长音频判断正误
    def option1(self):
        # childs = self.find_Elements('id',self.match_tv,None)
        childs = self.find_Elements('xpath','//*[@text="Match"]',None)
        for i in childs:
            i.click()

    #听音频选图片
    def option2(self):
        self.find_Element_click('xpath','//*[@text="A"]/preceding-sibling::android.widget.ImageView',None)

    def option3(self):
        self.find_Element_click('id',elementsLoc.option3_tv,None)

    def submit_answer(self,view):
        result = self.is_element_exist(elementsLoc.submit_tv,None)
        if result:
            self.wait_little_second(1)
            self.take_screenShot(view)
            self.find_Element_click('id',elementsLoc.submit_tv,None)
        else:
            self.swipe_up(1000,1)
            self.option1()

    def run_opntion(self,type,view):
        if type ==1:
            self.option1()
        if type ==2:
            self.option2()
        if type ==3:
            self.option3()
        self.submit_answer(view)



class Audio(BasePage):

    def start_record(self):
        self.find_Element_click('id',elementsLoc.start_record_iv,None)

    def again_record(self):
        self.find_Element_click('id',elementsLoc.rerecord_btn,None)

    def commit_record(self,view):
        self.wait_little_second(1)
        self.take_screenShot(view)

        self.find_Element_click('id',elementsLoc.commit_btn,None)

    def play_my_record(self):
        self.find_Element_click('id',elementsLoc.my_audio_iv,None)

    def stop_record(self):
        w, h = self.get_window_size()
        self.driver.tap([(w / 2, h - 20)])
        # self.find_Element_click('id',elementsLoc.stop_record_iv,None)


    def run_audio(self,view):
        start_result = self.is_element_exist(elementsLoc.start_record_iv,None)
        again_result = self.is_element_exist(elementsLoc.rerecord_btn,None)

        if start_result:
            print('第一次录音')
            self.start_record()
            self.wait_little_second(2)
            self.stop_record()
            # 进入录音状态后，等待2秒 执行点击波纹结束录音
            # 但是这个方法并没有实现，只能等待录音自己结束才开始，这个元素也是存在的
            self.play_my_record()
            # self.again_record()
            self.commit_record(view)

        if again_result:
            print('有录音记录')
            # self.again_record()
            self.commit_record(view)


class WordHole(BasePage):

    def wordHole(self):
        childs = self.find_Elements('class',elementsLoc.hole_et,None)
        for i in childs:
            i.send_keys('autoTest')

    def submit_answer(self,view):
        result = self.is_element_exist(elementsLoc.submit_tv,None)
        if result:
            self.wait_little_second(1)
            self.take_screenShot(view)
            self.find_Element_click('id',elementsLoc.submit_tv,None)
        else:
            self.swipe_up(1000,1)
            self.wordHole()

    def run_wordHole(self,view):
        self.wordHole()
        self.submit_answer(view)


if __name__ == '__main__':
    Audio().run_audio("话题简述")