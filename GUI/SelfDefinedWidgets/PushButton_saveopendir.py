'''
NAME: PushButton_saveopendir.py
AUTHOR: John Archibald Page
DATE CREATED: 21/11/2022 
DATE LAST UPDATED: 21/11/2022

PURPOSE:
A class of push button that opens a save, open or directory setting window.

THIS IS BEING USED AS A PLACEHOLDER TO DEMONSTRATE FUTURE FUNCTIONALITY.

UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up
'''
import logging as log ##troubleshooting
log.info(__file__)  ##troubleshooting
from PyQt5 import QtWidgets
from GUI.AdditionalWindows.savediropen import savopendir_class

class saveopendirPushButton(QtWidgets.QPushButton):
    """To have a push button with built in pop up save/open/directory window"""

    def __init__(self,label,savediropen,filepurpose, filepath, filetype):
        super(saveopendirPushButton, self).__init__()  
        self.sodButton(label)
        self.clicked.connect(lambda:self.runwindow(savediropen,filepurpose, filepath, filetype))

    def sodButton(self,label):
        """Properties of button"""
        self.setText(label)

    def runwindow(self,savediropen,filepurpose, filepath, filetype):
        filename = savopendir_class(savediropen,filepurpose, filepath, filetype)
        return(filename)     

    
            



        #######run the SaveRead function file purpose

        #######if save, open or directory savediropen


      
       


    