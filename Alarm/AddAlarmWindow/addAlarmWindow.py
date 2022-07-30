from kivy.uix.popup import Popup
from kivy.properties import StringProperty

class AddAlarmWindow(Popup):
    
    selectedHour = 0
    selectedMinute = 0
    selectedTime = StringProperty("00:00")
    
    def open_window(self):
        
        self.open()
        
    def add(self, time):
        
        match time:
            case "hour":
                if int(self.selectedHour) == 23:
                    self.selectedHour = 0
                else:               
                    self.selectedHour = int(self.selectedHour) + 1
                    
            case "minute":
                if int(self.selectedMinute) == 59:
                    self.selectedMinute = 0
                else:
                    self.selectedMinute = int(self.selectedMinute) + 1
                    
        self.check_len(self.selectedHour, self.selectedMinute)
        
    def minus(self, time):
        
        match time:
            case "hour":
                if int(self.selectedHour) == 0:
                    self.selectedHour = 23                
                else:
                    self.selectedHour = int(self.selectedHour) - 1
            case "minute":
                if int(self.selectedMinute) == 0:
                    self.selectedMinute = 59
                else:
                    self.selectedMinute = int(self.selectedMinute) - 1
                    
        self.check_len(self.selectedHour, self.selectedMinute)
                    
    def check_len(self, hour, minute):
                
        if len(str(hour)) < 2:
            hour = "0" + str(hour)
            
        if len(str(minute)) < 2:
            minute = "0" + str(minute)
            
        self.edit_time_label(hour, minute)
            
    def edit_time_label(self, hour, minute):
        self.selectedTime = "{}:{}".format(hour, minute)