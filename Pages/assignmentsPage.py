from Pages.basePage import BasePage
from Pages.exercisePage import ExercisePage
from Pages.simulationPage import SimulationPage
from Pages.recordPage import RecordPage
from Pages.againAssignPage import AgainAssignmentsPage
from Common import elementsLoc


class AssignmentsPage(BasePage):

    def goto_learningPage(self):
        self.find_Element_click('id', elementsLoc.learing_tv, elementsLoc.view)

    def goto_profilePage(self):
        self.find_Element_click('id', elementsLoc.profile_tv, elementsLoc.view)

    def get_current_assignments(self):
        return self.find_Elements('id', elementsLoc.tag_tv, None)

    def is_exercise_simulation(self):
        assign_list = self.get_current_assignments()
        if assign_list[0].text == '教材练习':
            assign_list[0].click()
            if AgainAssignmentsPage().is_appear():
                AgainAssignmentsPage().goto_old_answer()
            return ExercisePage()
        elif assign_list[0].text == '模拟诊断':
            assign_list[0].click()
            if AgainAssignmentsPage().is_appear():
                AgainAssignmentsPage().goto_old_answer()
            return RecordPage().run_record()


if __name__ == '__main__':
    AssignmentsPage().is_exercise_simulation()
