
'''
NAME: AdvancedOptions_ConfigCreate.py
AUTHOR: John Archibald Page
DATE CREATED: 25/11/2022 
DATE LAST UPDATED: 01/12/2022

MosaicCreate_class -> interactive GUI to create a file to run a mosaic, or open file into this folder
 _________________________________________________
|@|Create Config                                |X| 
|-------------------------------------------------|            
| _Equipment____________________  _____________   |              
|| |Main Camera|      |Focuser| ||  Switch     |  |
|| |Positional Stand| |Filter|  ||    in       |  |
||        |RGB Camera|          ||     widget  |  |
||______________________________||             |  | 
| _Interface____________________ |             |  |  
||                              ||             |  |
|||save paths|  |Coms|          ||             |  |
||______________________________||_____________|  | 
|-------------------------------------------------|                
|Back|                                |SAVE|APPLY||
--------------------------------------------------

when button is clicked there will be a widget switched in the the right side
 with options for changing the values

UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up

'''
from PyQt5 import QtWidgets,QtGui
from SelfDefinedWidgets.PushButton_saveopendir import saveopendirPushButton

class ConfigCreate_class(QtWidgets.QWidget):
    """This is a pop-up class which creates a csv. config file that can be ran or saved"""

    def __init__(self):
       super(ConfigCreate_class,self).__init__()
       self.buildpopup()
       self.setWindowTitle("Create Config file") # title of window
       self.setWindowIcon(QtGui.QIcon('GUI/Images/Logo.png'))

    def buildpopup(self):
        """Build the layout of the pop up"""
        #call in widgets to build layout
        mainbuttonlayout = self.mainButtonsGrouping()
        bottomButtonslayout = self.bottomButtonsGroupings()
        #define layouts
        VLayout = QtWidgets.QVBoxLayout()
        self.HLayout = QtWidgets.QHBoxLayout()#buttons
        #place holder widget
        self.placeholder = QtWidgets.QWidget()
        #build button layout
        self.HLayout.addLayout(mainbuttonlayout)
        self.HLayout.addWidget(self.placeholder)
        #build overall layout
        VLayout.addLayout(self.HLayout)
        VLayout.addLayout(bottomButtonslayout)
        #put layout to ,main widget
        self.setLayout(VLayout)
 
    def mainButtonsGrouping(self):
        mainCamera,Focuser,Filter,pStand,RGBCamera,savePath,COMSb = self.mainButtons()

        #equipment buttons gourp
        #|   |   |
        #|   |   |
        #  |   |
        H1Layout = QtWidgets.QHBoxLayout()#row 1
        H1Layout.addWidget(mainCamera)
        H1Layout.addWidget(Focuser)
        H2Layout = QtWidgets.QHBoxLayout() # row 2
        H2Layout.addWidget(Filter)
        H2Layout.addWidget(pStand)
        V1Layout = QtWidgets.QVBoxLayout()
        V1Layout.addLayout(H1Layout)
        V1Layout.addLayout(H2Layout)
        V1Layout.addWidget(RGBCamera)
        eqgroupbox = QtWidgets.QGroupBox("Equipment")
        eqgroupbox.setLayout(V1Layout)

        #interfacing
        H3Layout = QtWidgets.QHBoxLayout()
        H3Layout.addWidget(savePath)
        H3Layout.addWidget(COMSb)
        intgroupbox = QtWidgets.QGroupBox("Interfacing")
        intgroupbox.setLayout(H3Layout)
        #overall layout
        V2Layout = QtWidgets.QVBoxLayout()
        V2Layout.addWidget(eqgroupbox)
        V2Layout.addWidget(intgroupbox)

        return(V2Layout)

    def mainButtons(self):
        #the back button which closes the current window, in this case the advanced options window
        #equipment
        mainCamera = QtWidgets.QPushButton("Main Camera")
        mainCamera.clicked.connect(lambda: self.formfunc("Main Camera",["Pixels: ","Bits: ", "ROI X:", "ROI Y"]))
        Focuser = QtWidgets.QPushButton("Focuser")
        Focuser.clicked.connect(lambda: self.formfunc("Focuser",["Steps: ","Backlash: ","Speed: "]))
        Filter = QtWidgets.QPushButton("Filter")
        Filter.clicked.connect(lambda: self.formfunc("Filter",["Standard Filter: ","Exposure Ratio Filter 1: ","Exposure Ratio Filter 2: ","Exposure Ratio Filter 3: ","Exposure Ratio Filter 4: ","Exposure Ratio Filter 5: ","Exposure Ratio Filter 6: ","Exposure Ratio Filter 7: ","Exposure Ratio Filter 8: ","Exposure Ratio Filter 9: ","Exposure Ratio Filter 10: "]))
        pStand = QtWidgets.QPushButton("Positional Stand")
        pStand.clicked.connect(lambda: self.formfunc("Positional Stand",["Azi Steps: ","Alt Steps: ","Speed: "]))  
        RGBCamera = QtWidgets.QPushButton("RBG Camera")
        RGBCamera.clicked.connect(lambda: self.formfunc("RGB Camera",["Pixels: ","Bits: "]))       
        
        #interfacing
        savePath = QtWidgets.QPushButton("File Paths")
        savePath.clicked.connect(lambda: self.formfunc("File Paths",["Serial Ports: ","Images: ","Mosaic: ","Set-up: ","Config: "]))  
        COMSb = QtWidgets.QPushButton("Serial Ports")
        COMSb.clicked.connect(lambda: self.formfunc("Serial Ports",["Main Camera: ","Focuser: ","Filter: ","Positional Stand: ","RGB Camera: "]))

        return(mainCamera,Focuser,Filter,pStand,RGBCamera,savePath,COMSb)

    def bottomButtonsGroupings(self):
        """Layout formatting for the "back","save" and "apply" buttons"""
        button1,button2,button3 = self.bottomButtons()
        HLayout = QtWidgets.QHBoxLayout()
        HLayout.addWidget(button1)
        HLayout.addWidget(button2)
        HLayout.addWidget(button3)
        return(HLayout)

    def bottomButtons(self):
        """Build the "back","save" and "apply" buttons"""
        #the back button which closes the current window, in this case the advanced options window
        #back
        button1 = QtWidgets.QPushButton("Back")
        button1.clicked.connect(lambda: self.close())
        #save
        button2 = saveopendirPushButton("Save Config File", savediropen="save",icon=False,filepurpose= "Config. File", filepath = "/InputFiles/Config/", filetype="csv")
        #run
        button3 = QtWidgets.QPushButton("Apply")
        button3.setStyleSheet("background-color: green")
        return(button1,button2,button3)

    def replaceplaceholder(self,inputwidget):
        self.HLayout.removeWidget(self.HLayout.itemAt(1).widget())
        self.HLayout.addWidget(inputwidget)

    def formfunc(self,title,labellist):
        """sublayout for confoig with a form filling format"""   
        #call in current path
        # ____________ Vertical alignment
        #|===========|
        #|===========|
        #|...........|
        VLayout = QtWidgets.QVBoxLayout()
        for i in range(len(labellist)):
            label = QtWidgets.QLabel(labellist[i])
            Value = QtWidgets.QLineEdit()
            HLayout = QtWidgets.QHBoxLayout()
            HLayout.addWidget(label)
            HLayout.addWidget(Value)
            VLayout.addLayout(HLayout)
        #put into groupbox
        groupbox = QtWidgets.QGroupBox(title)
        groupbox.setLayout(VLayout)
        self.HLayout.addWidget(groupbox)
        self.replaceplaceholder(groupbox)

    

 