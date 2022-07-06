from kivymd.app import MDApp
from kivymd.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file("main.kv")

class MainView(BoxLayout):
    
    pass


class AlarmApp(MDApp):
    
    def build(self):
        Window.size = (500, 1000)
        return MainView()
    
if __name__ == "__main__":
    
    AlarmApp().run()