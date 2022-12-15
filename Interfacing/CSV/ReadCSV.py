'''
NAME: ReadCSV.py
AUTHOR: John Archibald Page
DATE CREATED: 13/12/2022 
DATE LAST UPDATED: 14/12/2022

PURPOSE:
read in a csv to interact with files

UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up
'''
import logging as log ##troubleshooting
log.info(__file__)  ##troubleshooting
import pandas as pd

class Read_class():
    """Reading the config file"""
    def __init__(self):
        super(Read_class,self).__init__()   

#generic useful functions

    def readcol(self,filename, col=1):
        """Reads in a CSV file values"""
        df = pd.read_csv(filename,header = None)
        values = df[col] #values to input to the lineedits
        return(values)

    def readrow(self,filename, row=1):
        """Reads in a CSV file values"""
        df = pd.read_csv(filename,header = None)
        values = df.loc[row] #values to input to the lineedits
        return(values)

    def readval(self,filename, row = 1,col=1):
        """Reads in a CSV file values"""
        df = pd.read_csv(filename,header = None)
        values = df.loc[row,col] #values to input to the lineedits
        return(values)
        
#read in specific CSV files in speciic format, return values

    #default save paths
    def savepaths(self,val,filepath = "InputFiles/SavePaths/DEFAULT.csv"):
        """0:COMS,1:images,2:terminallog,3:config,4:mosaic,5:savepaths,6:setup"""
        df = pd.read_csv(filepath,header = None)
        path = str(df.loc[val][1]) 
        return(path)


    

