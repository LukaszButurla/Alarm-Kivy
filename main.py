from kivymd.app import MDApp
from kivymd.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window
from Clock.clock import ClockWidget
from Timer.timer import TimerWidget
from Timepiece.timepiece import TimepieceWidget
from Alarm.alarm import AlarmWidget

from Menu.menu import Menu

Builder.load_file("main.kv")

class MainView(BoxLayout):
    
    pass


class AlarmApp(MDApp):    
    
    def build(self):
        Window.size = (500, 1000)
        self.theme_cls.theme_style = "Dark"
        self.clockWidget = ClockWidget()
        self.timerWidget = TimerWidget()
        self.timepieceWidget = TimepieceWidget()
        return MainView()
    

    
if __name__ == "__main__":
    
    AlarmApp().run()