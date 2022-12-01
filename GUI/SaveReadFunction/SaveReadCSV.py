'''
NAME: SaveReadCSV.py
AUTHOR: John Archibald Page
DATE CREATED: 25/11/2022 
DATE LAST UPDATED: 25/11/2022

PURPOSE:
create a save file csv. using the save class and create window
, then read in a mosiac to the create window using the Read class.

UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up
'''
import pandas as pd
from PyQt5 import QtWidgets

#define the class
class Save_class():
    """Saving the config file"""
    def __init__(self,GUI,filename,savepath):
        super(Save_class,self).__init__()
        self.save_file(GUI,filename,savepath)    

    def readvaluesfromwidgets(self,GUI):
        """Read in the check boxes and spin box values"""
        values = GUI.findChildren(QtWidgets.QLineEdit)
        return(values)

    def save_file(self,GUI,filename,savepath,labels):
        """Creates a config .csv file with each label and value"""
        values = self.readinformation(GUI)
        f = open(savepath+"/"+filename, 'w')
        for i in range(len(labels)):
            f.write(str(labels[i])+","+str(values[i].text())+"\n")
        f.close()

class Read_class():
    """Reading the config file"""
    def __init__(self,GUI,filename,savepath):
        super(Read_class,self).__init__()
        self.Read_file(GUI,filename,savepath)    

    def read_file(self,filename,savepath, col=1):
        """Reads in a CSV file values"""
        df = pd.read_csv(savepath +"/"+filename,header = None)
        values = df[col] #values to input to the lineedits
        return(values)

    def Setvaluesofwidgets(self,GUI,filename,savepath):
        """Read in the check boxes and spin box values"""
        values = self.read_file(filename,savepath)
        inputbox = GUI.findChildren(QtWidgets.QLineEdit)
        for i in range(len(inputbox)):
            inputbox[i].setText(str(values[i]))
        
        
