from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty

class TimepieceWidget(FloatLayout):
    
    selectedHour = 0
    selectedMinute = 0
    selectedSecond = 0
    selectedTime = StringProperty("00:00.00")
    
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
                    
                    