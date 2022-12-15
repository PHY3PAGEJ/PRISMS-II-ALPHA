"""
NAME: MainConnecting.py
AUTHOR: John Archibald Page
DATE CREATED: 05/12/2022 
DATE LAST UPDATED: 05/12/2022

PURPOSE:

Connect all the GUI buttons to the interfaces.

UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up

"""
import logging as log ##troubleshooting
log.info(__file__)  ##troubleshooting
from GUI.MainWindow.PRISMSIIGUI import PRISMSIIGUI_class
from ConnectingWidgets.MainGroupBoxes.PositionCON import PositionCON_class
from ConnectingWidgets.MainGroupBoxes.FilterCON import FilterCON_class
from ConnectingWidgets.MainGroupBoxes.FocusCON import FocusCON_class
from Interfacing.CSV.ReadCSV import Read_class
rc = Read_class()

class MainConnecting_class():
    """Calls in the buttons, then connects each grouping individually."""
    def __init__(self):
        super(MainConnecting_class,self).__init__()

        Camera,Terminal,Position,Filter,CameraSettings,AOI, STOP = self.GUICall() #call in the widgets to assign to
        #connect functionality to the buttons that are connected
        #self.CheckConnect(Position.widget(0),Filter.widget(0),Camera.widget(0),CameraSettings.widget(0))
        self.RunMainWindow()
    
    def GUICall(self):
        """Call in all the GUI to assign the buttons to."""
        self.PRISMSII = PRISMSIIGUI_class()
        #find each of the GUI
        Terminal =  self.PRISMSII.Terminal.MaingroupBox
        AOI = self.PRISMSII.AO.MaingroupBox
        STOP = self.PRISMSII.STOP
        Camera = self.PRISMSII.Camera.MaingroupBox
        Position = self.PRISMSII.Position.MaingroupBox
        Filter = self.PRISMSII.Filter.MaingroupBox
        CameraSettings = self.PRISMSII.CameraSettings.MaingroupBox
        return(Camera,Terminal,Position,Filter,CameraSettings,AOI, STOP)

    def RunMainWindow(self):
        """Launches the main window after the buttons have been connected"""
        self.PRISMSII.MainWindow.show()

    def CheckConnect(self,Position,Filter,Camera,CameraSettings):
        """Checks whether they are connected, if not then do not connect the buttons"""
        connectedvalue = rc.readcol(filename="InputFiles\SerialPorts\COMS_Config.csv")
        connectedvalue = [ True if x == "True" else False for x in connectedvalue ] # convert to boolean
        #position: just position groupbox
        if connectedvalue[2]==True:
            self.posCON = PositionCON_class(Position)
        #filter: just filter groupbox
        if connectedvalue[3]==True:
            self.FilCON = FilterCON_class(Filter,Camera)
        #focus: just focus groupbox
        if connectedvalue[4]==True:
            self.FocCON = FocusCON_class(CameraSettings)

