'''
NAME: PushButton_advancedoptions.py
AUTHOR: John Archibald Page
DATE CREATED: 21/11/2022 
DATE LAST UPDATED: 21/11/2022

PURPOSE:
A class of push button that opens a dialog window with additional press button options that go on to further functionality.

UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up
'''
from PyQt5 import QtWidgets
from AdditionalWindows.AdvancedOptions import AdvancedOptions_class

class AOPushButton(QtWidgets.QPushButton):
    """To have a push button that opens additional window with further options"""

    def __init__(self,label,title,messagetitle, message,phbutton1,func1,phbutton2,func2,phbutton3,func3,col=True):
        super(AOPushButton, self).__init__()  
        self.AOButton(label)
        self.clicked.connect(lambda:self.runwindow(title,messagetitle, message,phbutton1,func1,phbutton2,func2,phbutton3,func3,col))

    def AOButton(self,label):
        """Properties of button"""
        self.setText(label)

    def runwindow(self,title,messagetitle, message,phbutton1,func1,phbutton2,func2,phbutton3,func3,col):
        self.window = AdvancedOptions_class(title,messagetitle, message,phbutton1,func1,phbutton2,func2,phbutton3,func3,col)
        self.window.show()
    

      
       


    