'''
NAME: LaunchSavefile.py
AUTHOR: John Archibald Page
DATE CREATED: 22/11/2022 
DATE LAST UPDATED: 15/12/2022

PURPOSE:
>read existing data
>pop up message depending on inputs: all connected or not connected

UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up

>14/12/2022 : impliment ReadCSV and SaveCSV into MainWindowLaunch to save the coms config file
>15/12/2022: remove the first button option, hard code as a back button
'''
import logging as log ##troubleshooting
log.info(__file__)  ##troubleshooting
from PyQt5 import QtWidgets
import logging as log
from GUI.AdditionalWindows.AdvancedOptions import AdvancedOptions_class
from GUI.AdditionalWindows.popupMessage import popupmessage_class
from ConnectingWidgets.MainConnecting import MainConnecting_class
from Interfacing.CSV.SaveCSV import Save_class
from Interfacing.CSV.ReadCSV import Read_class
sc = Save_class()
rc = Read_class()

#define the class
class LaunchFUNC_class():
    """Saving the config file"""
    def __init__(self,GUI):
        super(LaunchFUNC_class,self).__init__()
        self.error1 = popupmessage_class("PRISMS II: ERROR!","ERROR!", "Two or more ports have the same Serial Port defined... :(",False,250)
        self.error2 = popupmessage_class("PRISMS II: ERROR!","ERROR!", "The ports you have selected are not available... :(",False,250)
                     
    def readinformation(self,GUI):
        """Read in the check boxes and spin box values"""
        labels = ["MainCamera","AziAlt-Stand","Filter","Focuser","RGBCamera"]
        checkbox = GUI.findChildren(QtWidgets.QCheckBox)
        spinbox = GUI.findChildren(QtWidgets.QSpinBox)
        return(labels,checkbox,spinbox)

    def connectionCheck(self,GUI):
        """To check if everything is connected"""
        labels,checkbox,spinbox = self.readinformation(GUI)
        if all([i.isChecked() for i in checkbox]):
            return(True)
        else:
            return(False)

    def runpopup(self,GUI):
        """Pop up confirmation of choice"""
        labels,checkbox,spinbox = self.readinformation(GUI)
        ##ERROR CHECKING
        connected=[]
        comstextedit = GUI.findChildren(QtWidgets.QTextEdit)[0]
        comstextedit_plaintxt = comstextedit.toPlainText()
        comsno = [int(s) for s in str.split(comstextedit_plaintxt) if s.isdigit()] # extracts ints
        for i in range(len(checkbox)):
            if checkbox[i].isChecked() == True:  
                connected.append(spinbox[i].value())
        if len(connected) > 0 and any(connected) not in comsno: #ERROR 2: Check the chosen COMS are actually available
            self.error2.show()
            return
        if len(connected) > len(set(connected)):#ERROR 1: check there are no duplicate selections of connections
            self.error1.show()
            return
        else:#ELSE run as normal
            title="PRISMS II: Confirm COMS"
            #html table of the coms results
            message = "<table><tr><th>  Component  </th><th>  connected?  </th><th>  COMS#  </th></tr>"
            for i in range(len(labels)):
                message += "<tr><td>  {}  <td></td>  {}  <td></td>  {}  </td></tr>".format(labels[i],checkbox[i].isChecked(),spinbox[i].value())
            message += "</table>"
            phbutton2 = QtWidgets.QPushButton("Cancel")
            func2 = lambda: exit()
            phbutton3 = QtWidgets.QPushButton("Confirm")
            func3 = lambda: self.MainWindowLaunch(GUI)
            if self.connectionCheck(GUI) == True:
                messagetitle = "All Components Connected!"
            else:
                messagetitle = "WARNING! Not all Components Connected...<br> Continue with reduced functionnality?"
            self.window = AdvancedOptions_class(title,messagetitle, message,phbutton2,func2,phbutton3,func3)
            self.window.show()
    
    def MainWindowLaunch(self,GUI):
        """Creates a config .csv file with the coms for each component of Prisms II and launches the main window"""
        labels,checkbox,spinbox = self.readinformation(GUI)
        sc.comssave(labels,checkbox,spinbox,rc.savepaths(0))
        #output log message
        log.info("Equipment Serial Port Configuration set:")
        log.info("component,connected,COMS")
        for i in range(len(labels)):
            log.info("{},{},{}".format(labels[i],checkbox[i].isChecked(),spinbox[i].value()))
        GUI.close()
        self.window.close()
        self.Mainconnected = MainConnecting_class()

    def enablebuttons(self,GUI):
        """This is to check what is connected"""
        labels,checkbox,spinbox = self.readinformation(GUI)
        #get the list of what is and isent connected
        checkboxbool = []
        for i in range(len(checkbox)):
            checkboxbool.append(checkbox[i].isChecked())