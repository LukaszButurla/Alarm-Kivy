from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
import time
from math import floor
from kivy.clock import Clock


class TimerWidget(FloatLayout):
    
    timerActive = False
    timerStart = None
    timerTime = None
    
    def __init__(self, **kwargs):
        Clock.schedule_interval(self.count_time, 0.05)
        super().__init__(**kwargs)
    
    def start_stop_timer(self):
        
        if self.timerActive == False:
            self.timerActive = True
            self.ids.btnStartStopId.pos_hint = {"x": 0.6, "y": 0.4}
            self.ids.btnPauseId.opacity = 1
            self.timerStart = time.time()
            
        else:
            self.timerActive = False
            self.ids.btnStartStopId.pos_hint = {"x": 0.4, "y": 0.4}
            self.ids.btnPauseId.opacity = 0
            
    def count_time(self, dt):
        
        if self.timerActive == True:
            
            self.timerTime = time.time() - self.timerStart
            
            hour = self.timerTime / 3600
            hour = floor(hour)
            self.timerTime -= hour * 3600
            
            if len(str(hour)) < 2:
                hour = "0" + str(hour)
            
            minute = self.timerTime / 60
            minute = floor(minute)
            self.timerTime -= minute * 60
            
            if len(str(minute)) < 2:
                minute = "0" + str(minute)
                
            secondsDot = str(self.timerTime).find(".")
            second = str(self.timerTime)[:secondsDot]
            
            milisecond = str(self.timerTime)[secondsDot+1:secondsDot+3]
            
            print(hour, minute, second, milisecond)
            
        
