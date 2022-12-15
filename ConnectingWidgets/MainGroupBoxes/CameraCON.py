"""
NAME: CameraCON.py
AUTHOR: John Archibald Page
DATE CREATED: 29/11/2022 
DATE LAST UPDATED: 29/11/2022

PURPOSE:
To write functionality to filter.
this funcitonality will be set to buttons in seperate document

 _Filter___________
| | u | <>| | ... ||
''''''''''''''''''''
<>:move the filter to the printed number, update the camera label
u: enter moves the filter to this one, update the label for the camera

"""
import logging as log ##troubleshooting
log.info(__file__)  ##troubleshooting
from Interfacing.AndorCamera.AndorCamera import AndorCamera_class
from Interfacing.ConnectSerial import ConnectSerial_class
from ConnectingWidgets.ConnectFunctions import ConnectFunctions_class 

class CameraCON_class():
    """Build the functionality for the Filter controls"""
    def __init__(self):
        super(CameraCON_class,self).__init__()
        self.camerawidget = AndorCamera_class() # initalise camera widget
        self.cf = ConnectFunctions_class()
        self.cs = ConnectSerial_class()
        
    def insertcamerawidget(self,GUI):
        """replaces placeholder image iwth the stream"""
        labellist = self.cf.labelrefences(GUI)
        placeholder = labellist[1]

    #save image:*****

    #open dark: open what is used to subtract dark***

    


    
        