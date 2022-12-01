'''
NAME: LaunchConnect.py
AUTHOR: John Archibald Page
DATE CREATED: 23/11/2022 
DATE LAST UPDATED: 23/11/2022

PURPOSE:Connect functionality of launch

UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up

'''
#main modules
import pandas as pd
#self defined modules
from LaunchSerial import serialport_class
from LaunchSavefile import configfile_class
from LaunchGUI import LaunchGUI_class

class LaunchConnect_class():
    """connecting COMS button funcitonality"""
    def __init__(self,MainWindow):
        super(LaunchConnect_class,self).__init__()
        #call in classes
        self.Launch = LaunchGUI_class()
        self.lc = configfile_class(self.Launch,MainWindow)
        self.serial = serialport_class()
        #run connect functions
        self.connectSerialfunc()
        self.connectGenralFunc(MainWindow)

    def connectSerialfunc(self):
        """Reads in the existing serial port numbers and prints to widgets"""
        #call in information
        COMnumlist = self.serial.serialcomnamefunc()
        fullnamlist = self.serial.serialfullnamefunc()
        #set text to coms list 

        self.Launch.textbox.setText(COMnumlist)
        #update message pop up .csv file
        df = pd.read_csv(self.Launch.messagefile, header=None)
        df.at[2,1]=fullnamlist
        df.to_csv(self.Launch.messagefile, mode='w',index=False, header=False)

    def connectGenralFunc(self,MainWindow):
        """connects buttons to general functionality"""
        self.Launch.confirmButton.clicked.connect(lambda: self.lc.runpopup(self.Launch, MainWindow))




