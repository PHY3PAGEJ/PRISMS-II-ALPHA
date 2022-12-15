'''
NAME: PushButtton_CreateWindows.py
AUTHOR: John Archibald Page
DATE CREATED: 24/11/2022 
DATE LAST UPDATED: 30/11/2022

PURPOSE:
A class of push button that opens a dialog window to create and run mosaic or config.

UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up
'''
import logging as log ##troubleshooting
log.info(__file__)  ##troubleshooting
from PyQt5 import QtWidgets
from GUI.AdditionalWindows.AdvancedOptions_MosaicCreate import MosaicCreate_class
from GUI.AdditionalWindows.AdvancedOptions_ConfigCreate import ConfigCreate_class

class MCPushButton(QtWidgets.QPushButton):
    """To have a push button that runs the mosaic create window"""

    def __init__(self):
        super(MCPushButton, self).__init__()  
        self.setText("create")
        self.clicked.connect(self.runwindow)

    def runwindow(self):
        self.window = MosaicCreate_class()
        self.window.show()

class CCPushButton(QtWidgets.QPushButton):
    """To have a push button that runs the config create window"""

    def __init__(self):
        super(CCPushButton, self).__init__()  
        self.setText("create")
        self.clicked.connect(self.runwindow)

    def runwindow(self):
        self.window = ConfigCreate_class()
        self.window.show()
      
       


    