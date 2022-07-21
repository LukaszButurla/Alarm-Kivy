from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty
from kivy.clock import Clock

class TimepieceWidget(FloatLayout):
    
    selectedHour = 0
    selectedMinute = 0
    selectedSecond = 0
    selectedTime = StringProperty("00:00.00")
    timepieceActive = False
    timepiecePause = False
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def start_stop_timepiece(self):
        
        if self.timepieceActive == False:
            
            if int(self.selectedHour) > 0 or int(self.selectedMinute) > 0 or int(self.selectedSecond) > 0:
            
                print("start")
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
                    
        self.check_len()                    
        self.selectedTime = "{}:{}.{}".format(self.selectedHour, self.selectedMinute, self.selectedSecond)
                    
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
                    
        self.check_len()          
        self.selectedTime = "{}:{}.{}".format(self.selectedHour, self.selectedMinute, self.selectedSecond)
        
    def check_len(self):
        
        if len(str(self.selectedHour)) < 2:
            self.selectedHour = "0" + str(self.selectedHour)
            
        if len(str(self.selectedMinute)) < 2:
            self.selectedMinute = "0" + str(self.selectedMinute)
            
        if len(str(self.selectedSecond)) < 2:
            self.selectedSecond = "0" + str(self.selectedSecond)
                    
                    