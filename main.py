from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.core.window import Window

from frontend.src.screens.firstscreen.firstscreen import FirstScreen


Window.size = (300, 600)

class Dosom(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"  # "Purple", "Red"

        self.screenmanager = MDScreenManager()

        first_screen = FirstScreen(name = "firstscreen")
        self.screenmanager.add_widget(first_screen)

        return self.screenmanager
    
if __name__ == "__main__":
    app = Dosom()
    app.run()
