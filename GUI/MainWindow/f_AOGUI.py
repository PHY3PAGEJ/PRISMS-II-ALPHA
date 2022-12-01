'''
NAME: f_AOGUI.py
AUTHOR: John Archibald Page
DATE CREATED: 17/11/2022 
DATE LAST UPDATED: 01/12/2022

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
'''

from PyQt5 import QtWidgets
from SelfDefinedWidgets.PushButton_AdvancedOptions import AOPushButton
from SelfDefinedWidgets.PushButton_CreateWindows import MCPushButton, CCPushButton
from SelfDefinedWidgets.PushButton_saveopendir import saveopendirPushButton

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
        
        #all popups use back
        backbutton=QtWidgets.QPushButton("Back")
        func1 = lambda: exit()###place holder, gte rid of thisfor a back button!!!
        #mosaic
        mosaicopenbutton = saveopendirPushButton("Open Mosaic",savediropen="open",icon=False,filepurpose= "Mosaic file", filepath = "/InputFiles/Mosaics/", filetype="csv")
        moFunc = False
        mosaicCreatebutton = MCPushButton()
        mcFunc = False
        #setup
        setupsavebutton = saveopendirPushButton("Save Current Set-up",savediropen="save",icon=False,filepurpose= "Current Set-up", filepath = "/InputFiles/Setup/", filetype="csv")
        ssfunc = False
        setupopenbutton = saveopendirPushButton("Open Previous Set-up",savediropen="open",icon=False,filepurpose= "Current Set-up", filepath = "/InputFiles/Setup/", filetype="csv")
        sofunc = False
        #Config.
        configopenbutton = saveopendirPushButton("Open Config",savediropen="open",icon=False,filepurpose= "Config. file", filepath = "/InputFiles/Config/", filetype="csv")
        coFunc = False
        configCreatebutton = CCPushButton() 
        ccFunc = False
        #Mosaic button
        mosaicButton = AOPushButton("Mosaic","Advanced Options: Mosaic","Options", "Open existing Mosaic file or create new file.",backbutton,func1,mosaicopenbutton,moFunc,mosaicCreatebutton,mcFunc,col=False)
        mosaicButton.setToolTip("Create, open,and/or run Mosaic file")
        #setup button
        setupButton = AOPushButton("Set-Up","Advanced Options: Set-Up","Options", "Open existing set-up or save current set-up.",backbutton,func1,setupsavebutton,ssfunc,setupopenbutton,sofunc,col=False)
        setupButton.setToolTip("Save or open current display variables")
        #config button
        configButton = AOPushButton("Config","Advanced Options: PRISMS II Config.","Options", "Open existing Config. file or create new file.",backbutton,func1,configopenbutton,coFunc,configCreatebutton,ccFunc,col=False)
        configButton.setToolTip("Create, open, and/or run Config. file")
        #connect button functionality to clicked and enter button
        return(mosaicButton,setupButton,configButton)

    
      
