'''
NAME: PushButton_moreinfo.py
AUTHOR: John Archibald Page
DATE CREATED: 21/11/2022 
DATE LAST UPDATED: 01/12/2022

PURPOSE:
A class of push button that makes a pop up with more information. the message input format is csv,
which can be stored in the "message" sub folder

UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up
'''
import logging as log ##troubleshooting
log.info(__file__)  ##troubleshooting
from PyQt5 import QtWidgets
import pandas as pd
from GUI.AdditionalWindows.popupMessage import popupmessage_class

class moreinfoPushButton(QtWidgets.QPushButton):
    """To have a push button with built in message pop up"""

    def __init__(self, messagefile):
        super(moreinfoPushButton, self).__init__()  
        self.moreinfoButton()
        self.clicked.connect(lambda:self.runwindow(messagefile))

    def moreinfoButton(self):
        self.setText("...")
        self.setToolTip('More Information')

    def readmessageFile(self, messagefile):
        """Store the message information as a csv file to make editing later easier"""
        data = pd.read_csv(messagefile, header=None)
        msgcomponents = data[1] # the second column
        return(str(msgcomponents[0]),str(msgcomponents[1]), str(msgcomponents[2]),msgcomponents[3], int(msgcomponents[4]))

    def runwindow(self,messagefile):
        title,messagetitle, message,windowicon, width = self.readmessageFile(messagefile)
        self.popup = popupmessage_class(title,messagetitle, message,windowicon, width)
        self.popup.exec_()

    