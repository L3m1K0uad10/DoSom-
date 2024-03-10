from kivy.properties import StringProperty, ListProperty

from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder

Builder.load_file("frontend/src/screens/firstscreen/firstscreen.kv")

class CheckItem(MDBoxLayout):
    text = StringProperty()
    group = StringProperty()
    color = ListProperty([1, 1, 1, 1])

class TextIconButtonItem(MDBoxLayout):
    pass

class FirstScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.busy_days_list = [] 

    def AddToBusyDaysList(self):
        #print(self.ids.mondaycheckbox.ids.checkbox)
        if self.ids.mondayitem.ids.checkbox.active == True:
            self.busy_days_list.append("Monday")
        if self.ids.tuesdayitem.ids.checkbox.active == True:
            self.busy_days_list.append("Tuesday")
        if self.ids.wednesdayitem.ids.checkbox.active == True:
            self.busy_days_list.append("Wednesday")
        if self.ids.thursdayitem.ids.checkbox.active == True:
            self.busy_days_list.append("Thursday")
        if self.ids.fridayitem.ids.checkbox.active == True:
            self.busy_days_list.append("Friday")
        if self.ids.saturdayitem.ids.checkbox.active == True:
            self.busy_days_list.append("Saturday")
        if self.ids.sundayitem.ids.checkbox.active == True:
            self.busy_days_list.append("Sunday")
        
        print(self.busy_days_list)
