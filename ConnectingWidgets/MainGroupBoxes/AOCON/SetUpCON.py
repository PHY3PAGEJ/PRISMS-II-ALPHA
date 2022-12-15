'''
NAME: SetUpCON.py
AUTHOR: John Archibald Page
DATE CREATED: 13/12/2022 
DATE LAST UPDATED: 13/12/2022

PURPOSE:
connect the buttons for the advanced options interfacing

UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up
'''
import logging as log ##troubleshooting
log.info(__file__)  ##troubleshooting
from GUI.MainWindow.PRISMSIIGUI import PRISMSIIGUI_class
from GUI.AdditionalWindows.savediropen import savopendir_class
from ConnectingWidgets.ConnectFunctions import ConnectFunctions_class as cf
from Interfacing.CSV.SaveCSV import Save_class
from Interfacing.CSV.ReadCSV import Read_class
sc = Save_class()
rc = Read_class()

class AOICON_SetUp_class():
    """Read and write to widgets"""
    def __init__(self):
        super(AOICON_SetUp_class,self).__init__() 
        #self.PRISMSIIwindow = PRISMSIIGUI_class()#call in GUI
        #connect the buttons

####set-up: save setup button, open setup button

    def setupsaveFUNC(self):
        """Functionality of save current set-up button"""
        widgetlist = self.setupwidgets() # call in refernce ot widgets
        vals = cf.readvaluesofwidget(widgetlist)
        filename = savopendir_class(savediropen="save",filepurpose= "Current Set-up", filepath = "/InputFiles/Setup/", filetype="csv") # get the file name
        sc.filesave("setup",vals,filename)

    def setupopenFUNC(self):
        """Functionality of save current set-up button"""
        widgetlist = self.setupwidgets(self) # call in refernce ot widgets
        filename = savopendir_class(savediropen="open",filepurpose= "Set-up", filepath = "/InputFiles/Setup/", filetype="csv") # get the file name
        newvals = rc.readcol(filename) # call in new values from the folder
        cf.setvaluesofwidget(widgetlist,newvals)#update values
         
    ##run the following functions using the new values IF coms for that are connected
        #position abs
        #set filter
        #focus position abs
        #exposure
        #1:1
        #ROI
        #RGB
        #Setdark

#get references for the widgets
    def setupwidgets(self):
        """Get references to the widgets used for setup"""
        #widgets = ["ONETOONE","ROI","RGB","DARKSET","AZIMUTH","ALTITUDE","EXPOSURE","FOCUS","FILTER"]
        Camera = self.PRISMSIIwindow.Camera.MaingroupBox,
        Position = self.PRISMSIIwindow.Position.MaingroupBox
        Filter = self.PRISMSIIwindow.Filter.MaingroupBox
        CameraSettings = self.PRISMSIIwindow.CameraSettings.MaingroupBox
        ONETOONE,ROI,RGB,DARKSET=cf.checkboxrefences(Camera)
        AZIMUTH = cf.Textboxrefences(Position)[1]
        ALTITUDE = cf.Textboxrefences(Position)[2]
        FOCUS = cf.Textboxrefences(CameraSettings)[1]
        EXPOSURE = cf.Textboxrefences(CameraSettings)[3]
        FILTER = cf.spinboxrefences(Filter)[0]
        return(ONETOONE,ROI,RGB,DARKSET,AZIMUTH,ALTITUDE,EXPOSURE,FOCUS,FILTER)
