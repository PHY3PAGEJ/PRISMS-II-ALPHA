"""
NAME: a_CameraFUNC.py
AUTHOR: John Archibald Page
DATE CREATED: 29/11/2022 
DATE LAST UPDATED: 29/11/2022

PURPOSE:
To write functionality to the camera GUI, with focus on the main camera and RGB.
this funcitonality will be set to buttons in seperate document

 __Camera_______________________
|SAVE_IMAGE|______Label_________|
|		                |                   
|                               |  
|  DISPLAY                      |
|                               |          
|_______________________________|
|__Toggles______________________|               
| ___  ___  ___ |Dark Correction|          
||   ||   ||   |||   ||Set Dark||
| ROI  1:1  RGB | Show '''''''' |
|---------------|---------------| 
DISPLAY: show main camera feed
ROI: put flashing shape on camera equal to the calculation of the focus
1:1: show just ROI
RGB: swich the display to the RGB camera instead

"""
from ConnectSerial import ConnectSerial_class as cs
import andor3

class CameraFUNC_class():
    """Build the functionality for the Camera controls"""
    def __init__(self):
        super(CameraFUNC_class,self).__init__()
        
    

            
