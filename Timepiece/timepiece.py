from kivy.uix.floatlayout import FloatLayout

class TimepieceWidget(FloatLayout):
    
    selectedHour = 0
    selectedMinute = 0
    selectedSecond = 0
    
    def add(self, time):
        
        match time:
            case "hour":
                if self.selectedHour == 23:
                    self.selectedHour = 0
                else:
                    self.selectedHour += 1
            case "minute":
                if self.selectedMinute == 59:
                    self.selectedMinute = 0
                else:
                    self.selectedMinute += 1
            case "second":
                if self.selectedSecond == 59:
                    self.selectedSecond = 0
                else:
                    self.selectedSecond += 1
                    
        print(self.selectedHour, self.selectedMinute, self.selectedSecond)
                    
    def minus(self, time):
        
        match time:
            case "hour":
                if self.selectedHour == 0:
                    self.selectedHour = 23
                else:
                    self.selectedHour -= 1
            case "minute":
                if self.selectedMinute == 0:
                    self.selectedMinute = 59
                else:
                    self.selectedMinute -= 1
            case "second":
                if self.selectedSecond == 0:
                    self.selectedSecond = 59
                else:
                    self.selectedSecond -= 1
                    
        print(self.selectedHour, self.selectedMinute, self.selectedSecond)
                    
                    