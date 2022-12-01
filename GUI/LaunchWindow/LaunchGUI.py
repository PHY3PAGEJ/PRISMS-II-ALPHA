'''
NAME: LaunchGUI.py
AUTHOR: John Archibald Page
DATE CREATED: 22/11/2022 
DATE LAST UPDATED: 01/12/2022

PURPOSE:
To create the launch pop-up that assigns the coms for each component, with format shown below:
 _________________________________
|_PRISMS_II:Connect_COMS________|X|
| __Available_COMS_______________ |
||		                         ||                    
||_______________________________||            
||_________________________|_..._||<--- Pop -up of full names
| __Main_Camera__________________ |
||  _                 COMS #     ||
|| |_|Connected?     |    |<>|	 ||
||                   ''''''      ||
||_______________________________||
| __Positional_Stand_____________ |
||  _                 COMS #     ||
|| |_|Connected?     |    |<>|	 ||
||                   ''''''      ||
||_______________________________||
| __Filter_______________________ |
||  _                 COMS #     ||
|| |_|Connected?     |    |<>|	 ||
||                   ''''''      ||
||_______________________________||
| __Focuser______________________ |
||  _                 COMS #     ||
|| |_|Connected?     |    |<>|	 ||
||                   ''''''      ||
||_______________________________||
| __RGB_Camera___________________ |
||  _                 COMS #     ||
|| |_|Connected?     |    |<>|	 ||
||                   ''''''      ||
||_______________________________||
| |CANCEL|              |CONFIRM| |
'''''''''''''''''''''''''''''''''''' 
UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up
'''
from PyQt5 import QtWidgets, QtCore, QtGui
import logging as log
from SelfDefinedWidgets.PushButton_popupMessage import moreinfoPushButton

class LaunchGUI_class(QtWidgets.QWidget):
    """Build the GUI for the launch pop up which makes a config file for the COMS"""
    messagefile = "GUI/AdditionalWindows/Messages/COMS_moreinfo.csv"
    def __init__(self):
        super(LaunchGUI_class,self).__init__()
        log.info("Launch Window initiating...")
        self.BuildMainLayout() 
        self.setWindowIcon(QtGui.QIcon('GUI/Images/Logo.png'))
        self.setGeometry(500, 50,400,500) 
        log.info("Launch Window initiated Successfully!")
        
    def BuildMainLayout(self):
        """Build the main layout, stacking the sublayouts"""
        #call in all widgets
        self.textbox = self.terminalScript()
        cancelButton,self.confirmButton,infoButton = self.Buttons()
        SubgroupBoxs = self.BuildSubLayout()
        ##make avaliable serial port group
        acgroupBox = QtWidgets.QGroupBox("Available Serial Ports")
        #build serial port area
        acVLayout = QtWidgets.QVBoxLayout() 
        acVLayout.addWidget(self.textbox)
        acVLayout.addWidget(infoButton, alignment=QtCore.Qt.AlignRight)
        acgroupBox.setLayout(acVLayout)
        ##make button area
        HLayout = QtWidgets.QHBoxLayout()
        HLayout.addWidget(cancelButton, alignment=QtCore.Qt.AlignLeft)
        HLayout.addWidget(self.confirmButton, alignment=QtCore.Qt.AlignRight)
        ##main vertical layout
        VLayout = QtWidgets.QVBoxLayout() 
        VLayout.addWidget(acgroupBox) # serial port
        for i in range(len(SubgroupBoxs)): #oomponents
            VLayout.addWidget(SubgroupBoxs[i])
        VLayout.addLayout(HLayout)
        #set margins
        VLayout.setContentsMargins(20, 20, 20, 20)
        ##make and set layout to central widget
        self.setLayout(VLayout)
        #set the title
        self.setWindowTitle("PRISMS II: Set serial ports")
    
    def BuildSubLayout(self):
        """ Create a sublayout of each compoent in the following form:
        __component__________________________________
        |                                    COMS    |
        |		        _                    _____   |
        |		       |_|Connected?        |#|<> |  |
        |____________________________________'''''___|                    
        """
        title = ["Main Camera","Azimuth/Altitude Stand","Filter","Focuser","RGB Camera"]
        SubgroupBoxs = []
        for i in range(len(title)):
            ##Call in widgets
            #toggle connected
            Toggle = QtWidgets.QCheckBox("Connected?")	
            #spinwheel
            spinWheel = QtWidgets.QSpinBox()
            spinWheel.setRange (0, 10)
            #COMS Label
            comLabel = QtWidgets.QLabel("COMS Port")
            #make groupbox for widgets to sit in
            SubgroupBox = QtWidgets.QGroupBox(title[i])
            # vertical orientation
            HLayout = QtWidgets.QHBoxLayout()
            VLayout = QtWidgets.QVBoxLayout() 
            #add the vertical widgets
            VLayout.addWidget(comLabel)
            VLayout.addWidget(spinWheel)   
            #add the horizontal widgets 
            HLayout.addWidget(Toggle)
            HLayout.addLayout(VLayout)
            SubgroupBox.setLayout(HLayout)
            SubgroupBoxs.append(SubgroupBox)
        return(SubgroupBoxs)

    def Buttons(self):
        """Define the buttons"""
        #Cancel button
        cancelButton = QtWidgets.QPushButton("Cancel")
        cancelButton.setToolTip("Closes PRISMS II")
        cancelButton.setStyleSheet("background-color: red")
        cancelButton.clicked.connect(self.close)
        #Confirm button
        confirmButton = QtWidgets.QPushButton("Confirm")
        confirmButton.setToolTip("Confirm choice of serial ports")
        confirmButton.setStyleSheet("background-color: green")
        #info button
        infoButton = moreinfoPushButton(self.messagefile)
        infoButton.setToolTip("Full serial port name")
        return(cancelButton,confirmButton,infoButton)

    def terminalScript(self):
        """Create a scrollable area that automatically grows to use as terminal"""
        #text edit box properties and location---
        textbox = QtWidgets.QTextEdit()
        textbox.setMinimumHeight(50)
        textbox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff) #switch off automatic vertical box for textedit
        #settextboxproperties
        textbox.setTextInteractionFlags(QtCore.Qt.NoTextInteraction) 
        return(textbox)


      
