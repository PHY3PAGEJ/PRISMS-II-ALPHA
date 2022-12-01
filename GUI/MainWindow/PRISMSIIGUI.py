'''
NAME: PRISMSIIGUI.py
AUTHOR: John Archibald Page
DATE CREATED: 18/11/2022 
DATE LAST UPDATED: 01/12/2022

PURPOSE:
To inset the PRISMS II with the grouping files Mock-up images and below.
If certain components are not connected to serial, then the buttons are replaced with blank widgets

_______________________________
|_______________________________|  a_Camera
| a             ||b            ||  b_Terminal
|               ||_____________||  c_Position  
|               || c  ||  d    ||  d_Filter
|               ||    ||_______||  e_CameraSettings
|               ||____||  f    ||  f_AdvancedOptions
|               || e  ||_______||
|               ||____||_STOP__||
|_______________|_______________|

UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up

'''
#PYQT modules
from PyQt5 import QtWidgets
import os
import logging as log
#self-made GUI clases
from a_CameraGUI import CameraGUI_class
from b_TerminalGUI import TerminalGUI_class
from c_PositionGUI import PositionGUI_class
from d_FilterGUI import FilterGUI_class
from e_CameraSettingsGUI import CameraSettingsGUI_class
from f_AOGUI import AOGUI_class
#mainwindow
from SelfDefinedWidgets.MainWindow import MainWindow_class
#check what is connected
from EquipmentEnabledCheck import EquipmentEnabledCheck_class as EEC


class PRISMSIIGUI_class():
    """Build the GUI for PRISMSII"""
    def __init__(self):
        super(PRISMSIIGUI_class,self).__init__()
        #OS Options
        os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0"  
        os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"
        log.info("Initiating Main window...")
        self.cWidget = self.BuildLayout()
        # Frame Customisation
        FrameShape = QtWidgets.QFrame.Box
        FrameShadow = QtWidgets.QFrame.Raised
        self.MainWindow = MainWindow_class(0.5,0.5,"paw_icon.png")
        #set central widget and the layout to this
        self.MainWindow.setCentralWidget(self.cWidget)
        log.info("Main window initiated successfully!")
        
    
    def BuildLayout(self):
        """Build the layout of PRISMS II Main Window"""
        ##call in components
        #components that alway exist
        self.Terminal = TerminalGUI_class()
        self.AO = AOGUI_class()
        self.STOP = self.StopButton()
        #components that need to be enabled
        self.Camera = CameraGUI_class() #need to unenable rgb button
        self.Position = PositionGUI_class()
        self.Filter = FilterGUI_class()
        self.CameraSettings = CameraSettingsGUI_class() # split into it's two parts
        ##Build up the layout piecewise
        #Vertical orientation c,e : [1]
        VLayout_1 = QtWidgets.QVBoxLayout()
        VLayout_1.addWidget(self.Position.MaingroupBox)
        VLayout_1.addWidget(self.CameraSettings.MaingroupBox)
        #vertical orientation d,f,STOP : [2]
        VLayout_2 = QtWidgets.QVBoxLayout()
        VLayout_2.addWidget(self.Filter.MaingroupBox)
        VLayout_2.addWidget(self.AO.MaingroupBox)
        VLayout_2.addWidget(self.STOP)
        #Horizontal orientation [1] and [2] : [3]
        HLayout_3 = QtWidgets.QHBoxLayout()
        HLayout_3.addLayout(VLayout_1)
        HLayout_3.addLayout(VLayout_2)
        #Vertical orientation b and [3]: [4]
        VLayout_4 = QtWidgets.QVBoxLayout()
        VLayout_4.addWidget(self.Terminal.MaingroupBox)
        VLayout_4.addLayout(HLayout_3)
        #Horizontal orientation a and [4]: [5]
        HLayout_5 = QtWidgets.QHBoxLayout()
        HLayout_5.addWidget(self.Camera.MaingroupBox)
        HLayout_5.addLayout(VLayout_4)
        ##assign main layout to central widget
        cWidget = QtWidgets.QWidget()
        cWidget.setLayout(HLayout_5)
        return(cWidget)

    def StopButton(self):
        """Define the emergency stop button"""
        stopButton = QtWidgets.QPushButton()
        stopButton.setStyleSheet("background-color: red")
        stopButton.setText("STOP")
        stopButton.setToolTip("Stops all running functions and movement")
        return(stopButton)


      
