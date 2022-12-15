'''
NAME: EquipmentEnabledCheck.py
AUTHOR: John Archibald Page
DATE CREATED: 01/12/2022 
DATE LAST UPDATED: 05/12/2022

PURPOSE:
To check the connected is equal to true, if not a placeholder widget is put into place and widgets are not connected.
UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up

'''
import logging as log ##troubleshooting
log.info(__file__)  ##troubleshooting
from PyQt5 import QtWidgets
from Interfacing.CSV.ReadCSV import Read_class
rc = Read_class()

class EquipmentEnabledCheck_class():
    """Build the GUI for the camera settings, contating controls for Focus and Exposure"""
    def __init__(self,position,filter,camera,camerasettings):
        super(EquipmentEnabledCheck_class,self).__init__()
        self.widgetstoDisable(position,filter,camera,camerasettings)

    def widgetstoDisable(self,position,filter,camera,camerasettings):
        """Assign component widgets to disable"""
        connectedvalue = self.CheckConnected()
        #filter: just filter groupbox
        if connectedvalue[3]==False:
            self.switchtoPlaceHolder(filter)
        #position: just position groupbox
        if connectedvalue[2]==False:
            self.switchtoPlaceHolder(position)
        #just Focus: Focus
        if connectedvalue[4]==False:
            self.switchtoPlaceHolder(camerasettings.currentWidget().findChildren(QtWidgets.QStackedWidget)[0])
        #Just Main camera: toggles, exposure
        if connectedvalue[1]==False and connectedvalue[5]==True:
            self.switchtoPlaceHolder(camera.currentWidget().findChild(QtWidgets.QStackedWidget))
            self.switchtoPlaceHolder(camerasettings.currentWidget().findChildren(QtWidgets.QStackedWidget)[1])
        #Just RGB Camera: RGB toggle
        if connectedvalue[1]==True and connectedvalue[5]==False:
            self.switchtoPlaceHolder(camera.currentWidget().findChild(QtWidgets.QStackedWidget).findChild(QtWidgets.QStackedWidget))
        #Both Cameras: Camera, Exposure
        if connectedvalue[1]==False and connectedvalue[5]==False:
            self.switchtoPlaceHolder(camera)
            self.switchtoPlaceHolder(camerasettings.currentWidget().findChildren(QtWidgets.QStackedWidget)[1])
        #focus and main camera: groupbox for camerasettings
        if connectedvalue[1]==False and connectedvalue[4]==False:
            self.switchtoPlaceHolder(camerasettings)

    def CheckConnected(self):
        """Read the COMS Config File and output whether connected or not"""
        connectedvalue = rc.readcol(filename="InputFiles\SerialPorts\COMS_Config.csv")
        connectedvalue = [ True if x == "True" else False for x in connectedvalue ] # convert to boolean
        return(connectedvalue)

    def switchtoPlaceHolder(self,stackwidget):
        """Effectively disables the widget while putting in a place holder to hsow where it was"""
        stackwidget.setCurrentIndex(1)
   