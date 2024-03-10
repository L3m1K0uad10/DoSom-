from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.lang import Builder

KV = '''
BoxLayout:
    orientation: 'vertical'

    MDLabel:
        text: "Hello, KivyMD!"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
'''

class MyApp(MDApp):
    def build(self):
        # Set the primary color to a custom color (e.g., 'Red')
        self.theme_cls.primary_palette = 'Red'
        return Builder.load_string(KV)

MyApp().run()
