'''
NAME: a_CameraGUI.py
AUTHOR: John Archibald Page
DATE CREATED: 17/11/2022 
DATE LAST UPDATED: 01/12/2022

PURPOSE:
To create the buttons Camera GUI, with format shown below:

 __Camera_______________________
|SAVE_IMAGE|______Label_________|
|		                        |                   
|                               |  
|  DISPLAY  FRAME               |
|                               |          
|_______________________________|
|__Toggles______________________|               
| ___  ___  ___ |Dark Correction|          
||   ||   ||   |||   ||Set Dark||
| ROI  1:1  RGB | Show '''''''' |
|---------------|---------------| 
UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up

'''
from PyQt5 import QtWidgets, QtGui, QtCore
import pandas as pd
from SaveReadFunction.SaveReadCSV import Read_class

class EquipmentEnabledCheck_class():
    """Build the GUI for the camera settings, contating controls for Focus and Exposure"""
    def __init__(self):
        super(EquipmentEnabledCheck_class,self).__init__()
    
    def CheckConnected(self):
        """Read the COMS Config File and output whether connected or not"""
        connectedvalue = Read_class.read_file(filename="COMS_Config.csv",savepath="InputFiles\SerialPorts")
        

    def PlaceHolder(self):
        """This is a place holder for when the serial for a device is not connected"""
        dFramewidget = QtWidgets.QLabel()
        pixmax = QtGui.QPixmap('GUI/Images/PlaceHolder.png')
        myScaledPixmap = pixmax.scaled(dFramewidget.size(), QtCore.Qt.KeepAspectRatio)
        dFramewidget.setPixmap(myScaledPixmap)
        return(dFramewidget)

   