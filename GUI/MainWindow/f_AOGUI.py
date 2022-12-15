'''
NAME: f_AOGUI.py
AUTHOR: John Archibald Page
DATE CREATED: 17/11/2022 
DATE LAST UPDATED: 15/12/2022

PURPOSE:
To create the buttons for Advance Options GUI:

 _Advance_Options_
|   |Mosaic |     |
|    =======      |
|   |Set-Up |     |
|    =======      |
|   |Config.|     |
|-----------------|

UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up
>15/12/2022: remove the first button option, hard code as a back button
'''
import logging as log ##troubleshooting
log.info(__file__)  ##troubleshooting
from PyQt5 import QtWidgets
from GUI.SelfDefinedWidgets.PushButton_AdvancedOptions import AOPushButton
from GUI.SelfDefinedWidgets.PushButton_CreateWindows import MCPushButton, CCPushButton
from GUI.SelfDefinedWidgets.PushButton_saveopendir import saveopendirPushButton

class AOGUI_class():
    """Build the GUI for the Advance Options controls"""
    def __init__(self):
        super(AOGUI_class,self).__init__()
        self.MaingroupBox = self.BuildLayout()

    def BuildLayout(self):
        """Build the Orientation of PRISMS II widgets group"""
        #call in widgets
        mosaicButton,setupButton,configButton=self.Buttons()
        #make groupbox for widgets to sit in
        groupBox = QtWidgets.QGroupBox("Advanced Options")
        #Vertical layout
        Vlayout = QtWidgets.QVBoxLayout()
        Vlayout.addWidget(mosaicButton)
        Vlayout.addWidget(setupButton) 
        Vlayout.addWidget(configButton) 
        #add the layout to the group
        groupBox.setLayout(Vlayout)
        return(groupBox)

    def Buttons(self):
        """Define the buttons"""
        #mosaic
        mosaicopenbutton = saveopendirPushButton("Open Mosaic",savediropen="open",filepurpose= "Mosaic file", filepath = "/InputFiles/Mosaics/", filetype="csv")
        moFunc = False
        mosaicCreatebutton = MCPushButton()
        mcFunc = False
        #setup
        setupsavebutton = saveopendirPushButton("Save Current Set-up",savediropen="save",filepurpose= "Current Set-up", filepath = "/InputFiles/Setup/", filetype="csv")
        ssfunc = False
        setupopenbutton = saveopendirPushButton("Open Previous Set-up",savediropen="open",filepurpose= "Current Set-up", filepath = "/InputFiles/Setup/", filetype="csv")
        sofunc = False
        #Config.
        configopenbutton = saveopendirPushButton("Open Config",savediropen="open",filepurpose= "Config. file", filepath = "/InputFiles/Config/", filetype="csv")
        coFunc = False
        configCreatebutton = CCPushButton() 
        ccFunc = False
        #Mosaic button
        mosaicButton = AOPushButton("Mosaic","Advanced Options: Mosaic","Options", "Open existing Mosaic file or create new file.",mosaicopenbutton,moFunc,mosaicCreatebutton,mcFunc,col=False)
        mosaicButton.setToolTip("Create, open,and/or run Mosaic file")
        #setup button
        setupButton = AOPushButton("Set-Up","Advanced Options: Set-Up","Options", "Open existing set-up or save current set-up.",setupsavebutton,ssfunc,setupopenbutton,sofunc,col=False)
        setupButton.setToolTip("Save or open current display variables")
        #config button
        configButton = AOPushButton("Config","Advanced Options: PRISMS II Config.","Options", "Open existing Config. file or create new file.",configopenbutton,coFunc,configCreatebutton,ccFunc,col=False)
        configButton.setToolTip("Create, open, and/or run Config. file")
        #connect button functionality to clicked and enter button
        return(mosaicButton,setupButton,configButton)

    
      
