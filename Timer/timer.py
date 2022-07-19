from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
import time
from math import floor
from kivy.clock import Clock
from kivy.properties import StringProperty


class TimerWidget(FloatLayout):
    
    timerActive = False
    timerStart = None
    timerTime = None
    timerDeltaTime = StringProperty("00:00:00.00")
    timerPause = False
    timerPauseTime = 0
    timerPauseStart = None
    
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
            self.timerPauseTime = 0
            self.timerPause = False
            self.timerDeltaTime = "00:00:00.00"
            
    def pause_timer(self):
        
        if self.timerPause == True:
            self.timerPause = False
            self.timerPauseTime += (time.time() - self.timerPauseStart)
        else:
            self.timerPause = True
            self.timerPauseStart = time.time()
        
            
    def count_time(self, dt):
        
        if self.timerActive == True and self.timerPause == False:
            
            self.timerTime = time.time() - (self.timerStart + self.timerPauseTime)
            
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
            
            if len(str(second)) < 2:
                second = "0" + str(second)
            
            milisecond = str(self.timerTime)[secondsDot+1:secondsDot+3]
            
            print(hour, minute, second, milisecond)
            
            self.timerDeltaTime = "{}:{}:{}.{}".format(hour, minute, second, milisecond)
            
        
