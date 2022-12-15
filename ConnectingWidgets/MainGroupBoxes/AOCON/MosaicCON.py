'''
NAME: MosaicCON.py
AUTHOR: John Archibald Page
DATE CREATED: 13/12/2022 
DATE LAST UPDATED: 13/12/2022

PURPOSE:
attach functionality to the advanced option interface mosaic buttons

UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up
'''
import logging as log ##troubleshooting
log.info(__file__)  ##troubleshooting
from GUI.AdditionalWindows.AdvancedOptions_MosaicCreate import MosaicCreate_class
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
        self.mosaicwindow = MosaicCreate_class()
        #connect buttons

####mosaic: open mosaic->create, create mosaic: save mosaic, RUN

    def mosaicsaveFUNC(self):
        """Functionality of save current set-up button"""
        widgetlist = self.Mosaicwidgets() # call in refernce ot widgets
        vals = cf.readvaluesofwidget(widgetlist)
        filename = savopendir_class(savediropen="save",filepurpose= "Mosaic file", filepath = "/InputFiles/Mosaics/", filetype="csv") # get the file name
        sc.filesave("mosaic",vals,filename)

    def mosaicopenFUNC(self):
        """Functionality of save current set-up button"""
        filename = savopendir_class(savediropen="open",filepurpose= "Mosaic file", filepath = "/InputFiles/Mosaics/", filetype="csv") # get the file name
        newvals = rc.readcol(filename) # call in new values from the folder
        widgetlist = self.Mosaicwidgets() # call in refernce ot widgets
        cf.setvaluesofwidget(widgetlist,newvals)#update values
        self.mosaicwindow.show()

#get references for the widgets
 
    def Mosaicwidgets(self):
        """Get references to the widgets used for setup"""
        EXP0,EXP1,EXP2,EXP3,EXP4,EXP5,EXP6,EXP7,EXP8,EXP9,AziInc,AltInc,Rows,Columns,Name,Location = cf.Textboxrefences(self.mosaicwindow)
        return(EXP0,EXP1,EXP2,EXP3,EXP4,EXP5,EXP6,EXP7,EXP8,EXP9,AziInc,AltInc,Rows,Columns,Name,Location)


