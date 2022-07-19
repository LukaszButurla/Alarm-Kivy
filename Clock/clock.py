from kivy.uix.floatlayout import FloatLayout
from datetime import datetime
from kivy.properties import StringProperty
from kivy.clock import Clock


class ClockWidget(FloatLayout):
    
    currentTime = StringProperty("0")
    
    def __init__(self, **kwargs):
        Clock.schedule_interval(self.get_current_time, 1)
        super().__init__(**kwargs)
    
    def get_current_time(self, dt):
        
        hour = datetime.now().hour
        minute = datetime.now().minute
        second = datetime.now().second
        
        if len(str(hour)) < 2:
            hour = "0" + str(hour)
            
        if len(str(minute)) < 2:
            minute = "0" + str(minute)
            
        if len(str(second)) < 2:
            second = "0" + str(second)
            
        self.currentTime = "{}:{}.{}".format(hour, minute, second)
        
        
            
        

            
        
    
