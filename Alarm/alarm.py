from kivy.uix.boxlayout import BoxLayout
import os

class AlarmWidget(BoxLayout):
    
    filePath = r"C:\kivygui\Alarm\Alarm\files\alarms.txt"
    
    def __init__(self, **kwargs):
        self.show_alarms()
        super().__init__(**kwargs)
    
    def show_alarms(self):
        
        dirExist = os.path.exists(self.filePath)
                
        if dirExist:
            with open(self.filePath, "r", encoding="utf-8") as fileOpen:
                lines = fileOpen.readlines()
                
                for line in lines:
                    line = line.split(";")
                    alarmHour = line[0]
                    alarmMinute = line[1]
                    alarmDays = line[2]
                    alarmColor = line[3]
                    alarmDescription = line[4]
                    
                    print("hour - {}\nminute - {}\ndays - {}\ncolor - {}\ndes - {}\n".format(alarmHour, alarmMinute, alarmDays, alarmColor, alarmDescription))
                    