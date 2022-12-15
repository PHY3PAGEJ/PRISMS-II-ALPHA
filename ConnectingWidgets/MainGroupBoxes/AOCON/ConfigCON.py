'''
NAME: ConfigCON.py
AUTHOR: John Archibald Page
DATE CREATED: 13/12/2022 
DATE LAST UPDATED: 13/12/2022

PURPOSE:
attach functionality to the advanced options interface config button

UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up
'''
import logging as log ##troubleshooting
log.info(__file__)  ##troubleshooting
from GUI.MainWindow.PRISMSIIGUI import PRISMSIIGUI_class
from ConnectingWidgets.MainConnecting import MainConnecting_class
from GUI.AdditionalWindows.AdvancedOptions_ConfigCreate import ConfigCreate_class
from GUI.AdditionalWindows.savediropen import savopendir_class
from ConnectingWidgets.ConnectFunctions import ConnectFunctions_class as cf
from Interfacing.CSV.SaveCSV import Save_class
from Interfacing.CSV.ReadCSV import Read_class

sc = Save_class()
rc = Read_class()

class AOICON_class():
    """Read and write to widgets"""
    def __init__(self):
        super(AOICON_class,self).__init__() 
        self.currentwindow = PRISMSIIGUI_class()
        self.configwindow = ConfigCreate_class() 
        #connect buttons
####config: open config->create, create config: save config, APPLY-Relaunch the program

    def configsaveFUNC(self):
        """Functionality of save current set-up button"""
        widgetlist = self.configwidgets() # call in refernce ot widgets
        vals = cf.readvaluesofwidget(widgetlist)
        filename = savopendir_class(savediropen="save",filepurpose= "Mosaic file", filepath = "/InputFiles/Mosaics/", filetype="csv") # get the file name
        sc.filesave("mosaic",vals,filename)

    def configopenFUNC(self):
        """Functionality of save current set-up button"""
        filename = savopendir_class(savediropen="open",filepurpose= "Mosaic file", filepath = "/InputFiles/Mosaics/", filetype="csv") # get the file name
        newvals = rc.readcol(filename) # call in new values from the folder
        widgetlist = self.configwidgets() # call in refernce ot widgets
        cf.setvaluesofwidget(widgetlist,newvals)#update values
        self.configwindow.show()

    ##apply button, re-launch PRISMSII
    def configApplyFUNC(self):
        """close current interface and re-launch with the new config"""
        #close current prisms
        self.configwindow.close() # config pop up
        self.currentwindow.close() # current prisms II interface
        self.Mainconnected = MainConnecting_class()  #reconnect, causing new config to be applied


#get references for the widgets

    def Configwidgets(self):
        """Get references to the widgets used for setup"""
        mcPix,mcBits, mcROIX, mcROIY,FoSteps,FoBL,FoSpeed,FiDef,ExpRat0,ExpRat1,ExpRat2,ExpRat3,ExpRat4,ExpRat5,ExpRat6,ExpRat7,ExpRat8,ExpRat9,SAziSteps,SAltSteps,SSpeed,RGBPix,RGBBit,spCOMS,spImg,spMos,spSU,SPCon,COMSmc,COMSFo,COMSFi,COMSS,COMSRGB = cf.Textboxrefences(self.configwindow)
        return(mcPix,mcBits, mcROIX, mcROIY,FoSteps,FoBL,FoSpeed,FiDef,ExpRat0,ExpRat1,ExpRat2,ExpRat3,ExpRat4,ExpRat5,ExpRat6,ExpRat7,ExpRat8,ExpRat9,SAziSteps,SAltSteps,SSpeed,RGBPix,RGBBit,spCOMS,spImg,spMos,spSU,SPCon,COMSmc,COMSFo,COMSFi,COMSS,COMSRGB)

