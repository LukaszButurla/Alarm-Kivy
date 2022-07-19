from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


class TimerWidget(FloatLayout):
    
    timerActive = False
    
    def start_stop_timer(self):
        
        if self.timerActive == False:
            self.timerActive = True
            self.ids.btnStartStopId.pos_hint = {"x": 0.6, "y": 0.4}
            self.ids.btnPauseId.opacity = 1
            
        else:
            self.timerActive = False
            self.ids.btnStartStopId.pos_hint = {"x": 0.4, "y": 0.4}
            self.ids.btnPauseId.opacity = 0
            
        
