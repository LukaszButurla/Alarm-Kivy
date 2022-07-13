from kivy.uix.floatlayout import FloatLayout
from datetime import datetime

class ClockWidget(FloatLayout):
    
    def get_current_time(self):
        
        hour = datetime.now().hour
        minute = datetime.now().minute
        second = datetime.now().second
        
        if len(str(hour)) < 2:
            hour = "0" + str(hour)
            
        if len(str(minute)) < 2:
            minute = "0" + str(minute)
            
        if len(str(second)) < 2:
            second = "0" + str(second)
            
        self.set_label_values(hour, minute, second)
        
    
    def set_label_values(self, hour, minute, second):
        
        print(hour, minute, second)
        
        self.ids.clockLabel.text = "{}:{}.{}".format(hour, minute, second)