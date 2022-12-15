'''
NAME: HoldDownButton.py
AUTHOR: John Archibald Page
DATE CREATED: 03/11/2022 
DATE LAST UPDATED: 29/11/2022

PURPOSE:
To allow for press button widgets to be pressed and held for a set time of activation (at)
 for a function (func1) to run.

 UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up

'''
import logging as log ##troubleshooting
log.info(__file__)  ##troubleshooting
from PyQt5 import QtCore, QtWidgets

class HoldDownButton_class(QtWidgets.QPushButton):  
    """To activate a button fucntion when held for activation time."""

    def __init__(self,at,funca,text=False,purp=False):
        super(HoldDownButton_class,self).__init__()
        if text != False and purp !=False:
            self.buttondefine(text,purp)
        self.pressed.connect(lambda: self.buttonheld(funca, at))
        self.released.connect(self.buttonreleased)
        self.timer = QtCore.QTimer()
    
    def buttonheld(self, func1, at):
        """hold down button for at time for function to start. releasing stops loop"""
        #initiate timer
        print("Button pressed")
        self.timer.timeout.connect(func1)  # connect it to your update function
        self.timer.start(at)  # set it to timeout in 5000 ms
        
    def buttonreleased(self):
        """Stops the timer and resets it"""
        self.timer.stop() 

    def buttondefine(self,text,purp):
        """Define the label and the tooltip of the button"""
        self.setText(text)
        self.setToolTip(purp)