'''
NAME: e_CameraSettings.py
AUTHOR: John Archibald Page
DATE CREATED: 25/11/2022 
DATE LAST UPDATED: 01/12/2022

PURPOSE:
Python call in the relevent directories as stated in the savepath folder:

__Camera_Settings_________________
| __Focus________________________ |
||		                |Auto |  ||   
|| ______  _____  ______  _____  ||            
|||__Nr__||_____||__Fr__||_____| ||
||_______________________________||
| __Exposure_____________________ |
||		                |Auto |  ||   
|| ______  _____  ______  _____  ||            
|||__Nr__||_____||__Fr__||_____| ||
||_______________________________||
|_________________________________|

UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up

'''
from PyQt5 import QtWidgets, QtGui

class CameraSettingsGUI_class():
    """Build the GUI for the camera settings, contating controls for Focus and Exposure"""
    def __init__(self):
        super(CameraSettingsGUI_class,self).__init__()
        self.MaingroupBox = self.BuildMainLayout()
        
    def BuildMainLayout(self):
        """Build the main layout, stacking the sublayouts:
        _____________
        |           |
        |===========|
        |___________|
        """
        #make main groupbox
        MaingroupBox = QtWidgets.QGroupBox("Camera Settings")
        VLayout = QtWidgets.QVBoxLayout() 
        MaingroupBox.setLayout(VLayout)
        #initiate the sub groups
        focuslayout = self.BuildSubLayout("f")
        exposurelayout = self.BuildSubLayout("e")
        #set subgroups into the maingroup
        VLayout.addWidget(focuslayout, 1)
        VLayout.addWidget(exposurelayout, 1)
        #set margins
        VLayout.setContentsMargins(20, 20, 20, 20)
        return(MaingroupBox)
    
    def BuildSubLayout(self,func):
        """ Create a sublayout of the Focus and exposure interfaces:
         __Focus________________________ 
        |		                |Auto | |   
        | ______  _____  ______  _____  |            
        ||__Nr__||_____||__Fr__||_____| |
        |_______________________________|
        """
        #call in widgets
        leftButton,rightButton,AutoButton = self.Buttons(func)
        StepSize,Value = self.TextInputs(func)
        title = self.Title(func)
        #make groupbox for widgets to sit in
        SubgroupBox = QtWidgets.QGroupBox(title)
        # vertical orientation, as shown in the diagram
        HLayout = QtWidgets.QHBoxLayout()
        VLayout = QtWidgets.QVBoxLayout() 
        #add the vertical widgets
        VLayout.addWidget(AutoButton, 4)#|Auto-Foc|
        VLayout.addWidget(Value, 6)     #|        |
        #add the horizontal widgets |  Nr  |     |  Fr  |vertical widgets|
        HLayout.addWidget(leftButton, 1)
        HLayout.addWidget(StepSize, 1)
        HLayout.addWidget(rightButton, 1)
        HLayout.addLayout(VLayout, 1)
        SubgroupBox.setLayout(HLayout)
        return(SubgroupBox)

    def Buttons(self,func):
        """Define the buttons for the focuser and exposure subgroups"""
        Buttonsdict = {"f":[["Nr","Send focus in, towards Camera"],["Fr","send focus out, away from Camera"],["Auto-Foc","Automatically focus for all filters"]],
                        "e":[[u"\u25C0","Lower Exposure"],[u"\u25B6","Increase Exposure"],["Auto-Exp","Automatically calculates exposure for filter 5, then config filter exposure ratios define the rest"]]}
        #left button
        leftButton = QtWidgets.QPushButton()
        leftButton.setText(Buttonsdict[func][0][0])
        leftButton.setToolTip(Buttonsdict[func][0][1])
        #right button
        rightButton = QtWidgets.QPushButton()
        rightButton.setText(Buttonsdict[func][1][0])
        rightButton.setToolTip(Buttonsdict[func][1][1])
        #auto button
        autoButton = QtWidgets.QPushButton()
        autoButton.setText(Buttonsdict[func][2][0])
        autoButton.setToolTip(Buttonsdict[func][2][1])
        #connect button functionality to clicked and enter button
        return(leftButton,rightButton,autoButton)

    def TextInputs(self, func):
        """define the input text boxes"""
        infodict = {"f":["Focus step increments","Focus value (Unitless)"],
                        "e":["Exposure value increments","Exposure value (Unitless)"]}
        #initalise float inputs
        StepSize = QtWidgets.QLineEdit()
        Value = QtWidgets.QLineEdit()
        #make only accept numbers by making validator
        dv = QtGui.QDoubleValidator(0.0, 1000000.0, 2) # [0, 5] with 2 decimals of precision
        dv.setNotation(QtGui.QDoubleValidator.StandardNotation) # no scientifc notation accepted
        #apply validator
        StepSize.setValidator(dv)
        Value.setValidator(dv)
        ##Add tool tips
        StepSize.setToolTip(infodict[func][0])
        Value.setToolTip(infodict[func][1])
        return(StepSize,Value)

    def Title(self,func):
        """Titles of the subgroups for the camera settings"""
        if func == "f":
            title = "Focus"
        if func == "e":
            title = "Exposure"
        return(title)

      
