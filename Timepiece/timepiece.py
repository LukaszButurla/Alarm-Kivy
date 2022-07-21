from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty
from kivy.clock import Clock
import time
from math import floor

class TimepieceWidget(FloatLayout):
    
    selectedHour = 0
    selectedMinute = 0
    selectedSecond = 0
    hourToEnd = None
    minuteToEnd = None
    secondToEnd = None
    selectedTime = StringProperty("00:00.00")
    timepieceActive = False
    timepiecePause = False
    timepieceStartTime = None
    timepieceEndTime = None
    timepieceTimeToEnd = 0
    
    def __init__(self, **kwargs):
        Clock.schedule_interval(self.count_timepiece, 1)
        super().__init__(**kwargs)
    
    def start_stop_timepiece(self):
        
        if self.timepieceActive == False:
            
            if int(self.selectedHour) > 0 or int(self.selectedMinute) > 0 or int(self.selectedSecond) > 0:
            
                self.timepieceStartTime = time.time()
                self.lastDelta = time.time()
                self.timepieceTimeToEnd = int(self.selectedHour) * 3600 + int(self.selectedMinute) * 60 + int(self.selectedSecond)
                self.timepieceEndTime = self.timepieceStartTime + self.timepieceTimeToEnd
                
                self.timepieceActive = True
                self.ids.btnStartId.pos_hint = {"x" : 0.55, "y" : 0.6}
                self.ids.btnPauseId.opacity = 1
                self.ids.btnPauseId.disabled = False
                self.enable_disable_buttons(True)
                
            else:
                print('n start')
            
        else:
            self.timepieceActive = False
            self.ids.btnStartId.pos_hint = {"x" : 0.4, "y" : 0.6}
            self.ids.btnPauseId.opacity = 0
            self.ids.btnPauseId.disabled = True
            self.timepiecePause = False
            self.enable_disable_buttons(False)
            
    def count_timepiece(self, dt):
        
        if self.timepieceActive == True and self.timepiecePause == False and self.timepieceTimeToEnd > 1:
            
            delta = time.time() - self.lastDelta
            
            self.timepieceTimeToEnd -= delta
                        
            print(self.timepieceTimeToEnd, "to end")
                    
            self.hourToEnd = floor(self.timepieceTimeToEnd/3600)
            self.minuteToEnd = floor((self.timepieceTimeToEnd - self.hourToEnd * 3600) / 60)
            self.secondToEnd = (self.timepieceTimeToEnd - self.hourToEnd * 3600 - self.minuteToEnd * 60)
            
            dot = str(self.secondToEnd).find(".")
            self.secondToEnd = str(self.secondToEnd)[:dot]
            
            print(self.hourToEnd, "h")
            print(self.minuteToEnd, "m")
            print(self.secondToEnd, "s")
            
            self.check_len(self.hourToEnd, self.minuteToEnd, self.secondToEnd)
            
            self.lastDelta = time.time()
            
    def enable_disable_buttons(self, disableBool):
        
        self.ids.btnAddHourId.disabled = disableBool
        self.ids.btnAddMinuteId.disabled = disableBool
        self.ids.btnAddSecondId.disabled = disableBool
        self.ids.btnMinusHourId.disabled = disableBool
        self.ids.btnMinusMinuteId.disabled = disableBool
        self.ids.btnMinusSecondId.disabled = disableBool
            
        if disableBool == True:
            disableBool = 0
        else:
            disableBool = 1
            
        self.ids.btnAddHourId.opacity = disableBool
        self.ids.btnAddMinuteId.opacity = disableBool
        self.ids.btnAddSecondId.opacity = disableBool
        self.ids.btnMinusHourId.opacity = disableBool
        self.ids.btnMinusMinuteId.opacity = disableBool
        self.ids.btnMinusSecondId.opacity = disableBool
            
    def pause_timepiece(self):
        
        if self.timepiecePause == True:
            self.timepiecePause = False
            
        else:
            self.timepiecePause = True        
    
    def add(self, time):
        
        match time:
            case "hour":
                self.selectedHour = int(self.selectedHour) + 1
            case "minute":
                if int(self.selectedMinute) == 59:
                    self.selectedMinute = 0
                else:
                    self.selectedMinute = int(self.selectedMinute) + 1
            case "second":
                if int(self.selectedSecond) == 59:
                    self.selectedSecond = 0
                else:
                    self.selectedSecond = int(self.selectedSecond) + 1
                    
        self.check_len(self.selectedHour, self.selectedMinute, self.selectedSecond)                    
                    
    def minus(self, time):
        
        match time:
            case "hour":
                if int(self.selectedHour) > 0:
                    self.selectedHour = int(self.selectedHour) - 1
            case "minute":
                if int(self.selectedMinute) == 0:
                    self.selectedMinute = 59
                else:
                    self.selectedMinute = int(self.selectedMinute) - 1
            case "second":
                if int(self.selectedSecond) == 0:
                    self.selectedSecond = 59
                else:
                    self.selectedSecond = int(self.selectedSecond) - 1
                    
        self.check_len(self.selectedHour, self.selectedMinute, self.selectedSecond)          
        
    def check_len(self, hour, minute, second):
                
        if len(str(hour)) < 2:
            hour = "0" + str(hour)
            
        if len(str(minute)) < 2:
            minute = "0" + str(minute)
            
        if len(str(second)) < 2:
            second = "0" + str(second)
            
        self.edit_timepiece_label(hour, minute, second)
            
    def edit_timepiece_label(self, hour, minute, second):
        self.selectedTime = "{}:{}.{}".format(hour, minute, second)
                    
                    