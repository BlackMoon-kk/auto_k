

from Pages.basePage import BasePage
from Pages.exercisePage import ExercisePage
from Common import elementsLoc

class AgainAssignmentsPage(BasePage):
    def is_appear(self):
        return self.is_element_exist(elementsLoc.goon_answer,None)

    def goto_new_answer(self):
        self.find_Element_click('id',elementsLoc.new_answer,None)

    def goto_old_answer(self):
        self.find_Element_click('id',elementsLoc.goon_answer,None)

