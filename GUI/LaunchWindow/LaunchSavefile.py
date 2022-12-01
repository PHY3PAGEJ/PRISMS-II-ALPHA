'''
NAME: LaunchSavefile.py
AUTHOR: John Archibald Page
DATE CREATED: 22/11/2022 
DATE LAST UPDATED: 23/11/2022

PURPOSE:
>read existing data
>pop up message depending on inputs: all connected or not connected

UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up

'''
from PyQt5 import QtWidgets
import pandas as pd
import logging as log
from AdditionalWindows.AdvancedOptions import AdvancedOptions_class
from AdditionalWindows.popupMessage import popupmessage_class

#read in default save path for the serial port
df = pd.read_csv("InputFiles/SavePaths/DEFAULT.csv",header = None)
COMSsavepath = str(df.loc[0][1]) +"/"+ "COMS_Config.csv"# Serial Ports file
print(COMSsavepath)
#define the class
class configfile_class():
    """Saving the config file"""
    def __init__(self,GUI,MainWindow):
        super(configfile_class,self).__init__()
        self.error1 = popupmessage_class("PRISMS II: ERROR!","ERROR!", "Two or more ports have the same Serial Port defined... :(",False,250)
        self.error2 = popupmessage_class("PRISMS II: ERROR!","ERROR!", "The ports you have selected are not available... :(",False,250)
                     
    def readinformation(self,GUI):
        """Read in the check boxes and spin box values"""
        labels = ["MainCamera","AzimuthAltitudeStand","Filter","Focuser","RGBCamera"]
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

    def runpopup(self,GUI,MainWindow):
        """Pop up confirmation of choice"""
        labels,checkbox,spinbox = self.readinformation(GUI)
        ##ERROR CHECKING
        #ERROR 1: check first there are no duplicate selections of connections
        connected=[]
        checkboxbool = self.enablebuttons(GUI)
        comstextedit = GUI.findChildren(QtWidgets.QTextEdit)[0]
        comstextedit_plaintxt = comstextedit.toPlainText()
        comsno = [int(s) for s in str.split(comstextedit_plaintxt) if s.isdigit()] # extracts ints
        for i in range(len(checkbox)):
            if checkbox[i].isChecked() == True:  
                connected.append(spinbox[i].value())
        if len(connected) > len(set(connected)):
            self.error1.show()
        #ERROR 2: Check the chosen COMS are actually available
        if checkboxbool !=None:
            if ((True in checkboxbool) and (sorted(connected) == sorted(comsno))):
                self.error2.show()
        #ELSE run as normal
        else:
            title="PRISMS II: Confirm COMS"
            #html table of the coms results
            message = "<table><tr><th>Component</th><th>connected?</th><th>COMS#</th></tr>"
            for i in range(len(labels)):
                message += str("<tr><td>"+labels[i]+"<td></td>"+str(checkbox[i].isChecked())+"<td></td>"+str(spinbox[i].value())+"</td></tr>")
            message += "</table>"
            phbutton1=QtWidgets.QPushButton("Back")
            func1 = lambda: self.window.hide()
            phbutton2 = QtWidgets.QPushButton("Cancel")
            func2 = lambda: exit()
            phbutton3 = QtWidgets.QPushButton("Confirm")
            func3 = lambda: self.config_file(GUI,MainWindow)
            if self.connectionCheck(GUI) == True:
                messagetitle = "All Components Connected!"
            else:
                messagetitle = "WARNING! Not all Components Connected...<br> Continue with reduced functionnality?"
            self.window = AdvancedOptions_class(title,messagetitle, message,phbutton1,func1,phbutton2,func2,phbutton3,func3)
            self.window.show()
    
    def config_file(self,GUI,MainWindow):
        """Creates a config .csv file with the coms for each component of Prisms II"""
        labels,checkbox,spinbox = self.readinformation(GUI)
        f = open(COMSsavepath, 'w')
        f.writelines("component,connected,COMS\n")
        log.info("Equipment Serial Port Configuration set:")
        log.info("component,connected,COMS")
        for i in range(len(labels)):
            f.write(labels[i]+","+str(checkbox[i].isChecked())+","+str(spinbox[i].value())+"\n")
            log.info(labels[i]+","+str(checkbox[i].isChecked())+","+str(spinbox[i].value()))
        f.close()
        GUI.close()
        self.window.close()
        MainWindow.show()

    def enablebuttons(self,GUI):
        """This is to check what is connected"""
        labels,checkbox,spinbox = self.readinformation(GUI)
        #get the list of what is and isent connected
        checkboxbool = []
        for i in range(len(checkbox)):
            checkboxbool.append(checkbox[i].isChecked())