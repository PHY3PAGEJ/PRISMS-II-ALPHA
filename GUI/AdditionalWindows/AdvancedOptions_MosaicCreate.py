
'''
NAME: AdvancedOptions_MosaicCreate.py
AUTHOR: John Archibald Page
DATE CREATED: 24/11/2022 
DATE LAST UPDATED: 24/11/2022

MosaicCreate_class -> interactive GUI to create a file to run a mosaic, or open file into this folder
________________________________
|@|Create Mosaic              |X| 
|-------------------------------|            
|_Exposure_time________________ |  
||filter: 1 2 3 4 5 6 7 8 9 10 ||  
||Set-exp| | | | | | | | | |  |||
|------------------------------||
|_Positional_increments_________|  
||Azimuth: |    |              ||  
||Altitude:|    |              ||
|------------------------------||
|_Cubes________________________ |  
||rows    Columns        Cubes ||  
|||   | X  |     |   =   |    |||
|------------------------------||
|_File_Name_&_Save_Location____ |  
||file name:     |         |   ||  
||Save location: |         |   ||
|------------------------------||                
|Back|                |SAVE|RUN||
--------------------------------
UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up

'''

from PyQt5 import QtWidgets, QtGui
from SelfDefinedWidgets.PushButton_saveopendir import saveopendirPushButton

class MosaicCreate_class(QtWidgets.QWidget):
    """This is a pop-up class which creates a csv. mosaic file that can be ran or saved"""

    def __init__(self):
       super(MosaicCreate_class,self).__init__()
       self.buildpopup()
       self.setWindowTitle("Create Mosaic") # title of window
       self.setWindowIcon(QtGui.QIcon('GUI/Images/Logo.png'))

    def buildpopup(self):
        """Build the layout of the pop up"""
        #call in widgets to build layout
        etgroupbox = self.Exposuretime()
        pigroupbox = self.PositionalIncrements()
        cgroupbox = self.Cubes()
        flgroupbox = self.filenameandloc() 
        button1, button2, button3 = self.Buttons()
        #define layouts
        VLayout = QtWidgets.QVBoxLayout()
        HLayout = QtWidgets.QHBoxLayout()#buttons
        #build button layout
        HLayout.addWidget(button1)
        HLayout.addWidget(button2)
        HLayout.addWidget(button3)
        #build overall layout
        VLayout.addWidget(etgroupbox)
        VLayout.addWidget(pigroupbox)
        VLayout.addWidget(cgroupbox)
        VLayout.addWidget(flgroupbox)
        VLayout.addLayout(HLayout)
        #put layout to ,main widget
        self.setLayout(VLayout)
 
    def Exposuretime(self):
        """sublayout exposure_time"""   
        #Filter 1 2 3 4 5 6 7 8 9 10
        Filterlabel = QtWidgets.QLabel("Filter: ")
        H1Layout = QtWidgets.QHBoxLayout()
        H1Layout.addWidget(Filterlabel)
        for i in range(10):
            numlabel = QtWidgets.QLabel(str(i+1))
            H1Layout.addWidget(numlabel)
        #Set exposure | | | | | | | | | | |
        setexposurelabel = QtWidgets.QLabel("Set-Exp: ")
        H2Layout = QtWidgets.QHBoxLayout()
        H2Layout.addWidget(setexposurelabel)
        for i in range(10):
            Value = QtWidgets.QLineEdit()
            dv = QtGui.QDoubleValidator(0.0, 1000000.0, 2) # [0, 5] with 2 decimals of precision
            dv.setNotation(QtGui.QDoubleValidator.StandardNotation) # no scientifc notation accepted
            Value.setValidator(dv)
            H2Layout.addWidget(Value)
        # ____________ Vertical alignment
        #|           |
        #|===========|
        #|___________|
        VLayout = QtWidgets.QVBoxLayout()
        VLayout.addLayout(H1Layout)
        VLayout.addLayout(H2Layout)
        #put into groupbox
        exptimegroupbox = QtWidgets.QGroupBox("Exposure Time")
        exptimegroupbox.setLayout(VLayout)
        return(exptimegroupbox)

    def PositionalIncrements(self):
        """sublayout Positional_increments"""   
        labellist = ["Azimuth: ","Altitude: "]
        # ____________ Vertical alignment
        #|           |
        #|===========|
        #|___________|
        VLayout = QtWidgets.QVBoxLayout()
        for i in range(len(labellist)):
            label = QtWidgets.QLabel(labellist[i])
            Value = QtWidgets.QLineEdit()
            dv = QtGui.QDoubleValidator(0.0, 1000000.0, 2) # [0, 5] with 2 decimals of precision
            dv.setNotation(QtGui.QDoubleValidator.StandardNotation) # no scientifc notation accepted
            Value.setValidator(dv)
            HLayout = QtWidgets.QHBoxLayout()
            HLayout.addWidget(label)
            HLayout.addWidget(Value)
            VLayout.addLayout(HLayout)
        #put into groupbox
        groupbox = QtWidgets.QGroupBox("Positional Increments")
        groupbox.setLayout(VLayout)
        return(groupbox)

    def Cubes(self):
        """sublayout Positional_increments"""   
        labellist = ["Rows","Columns","Total Cubes"]
        # _______________  alignment
        #|  |  |  |  |   |
        #|==|X |==|= |===|
        #|__|__|__|__|___|
        HLayout = QtWidgets.QHBoxLayout()
        symbols = [QtWidgets.QLabel("X"),QtWidgets.QLabel("=")]
        x=0
        y=0
        for i in range(5):
            if ((i+1) % 2) != 0: # if odd
                label = QtWidgets.QLabel(labellist[y])
                Value = QtWidgets.QLineEdit()
                dv = QtGui.QDoubleValidator(0.0, 1000000.0, 2) # [0, 5] with 2 decimals of precision
                dv.setNotation(QtGui.QDoubleValidator.StandardNotation) # no scientifc notation accepted
                Value.setValidator(dv)
                VLayout = QtWidgets.QVBoxLayout()
                VLayout.addWidget(label)
                VLayout.addWidget(Value)
                HLayout.addLayout(VLayout)
                y+= 1
            else:
                HLayout.addWidget(symbols[x])
                x += 1
        #put into groupbox
        groupbox = QtWidgets.QGroupBox("Cubes")
        groupbox.setLayout(HLayout)
        return(groupbox)

    def filenameandloc(self):
        """sublayout Positional_increments"""   
        labellist = ["Name: ","Location: "]
        # ____________ Vertical alignment
        #|           |
        #|===========|
        #|___________|
        VLayout = QtWidgets.QVBoxLayout()
        for i in range(len(labellist)):
            label = QtWidgets.QLabel(labellist[i])
            Value = QtWidgets.QLineEdit()
            HLayout = QtWidgets.QHBoxLayout()
            HLayout.addWidget(label)
            HLayout.addWidget(Value)
            VLayout.addLayout(HLayout)
        #put into groupbox
        groupbox = QtWidgets.QGroupBox("File Details")
        groupbox.setLayout(VLayout)
        return(groupbox)

    def Buttons(self):
        """Build the buttons needed for the advanced options. if button already has function then put func# = False"""
        #the back button which closes the current window, in this case the advanced options window
        #back
        button1 = QtWidgets.QPushButton("Back")
        button1.clicked.connect(lambda: self.close())
        #save
        button2 = saveopendirPushButton("Save Mosaic File", savediropen="save",icon=False,filepurpose= "Mosaic File", filepath = "/InputFiles/Mosaics/", filetype="csv")
        #run
        button3 = QtWidgets.QPushButton("Run")
        button3.setStyleSheet("background-color: green")
        return(button1,button2,button3)
            

