'''
NAME: ConnectSerial.py
AUTHOR: John Archibald Page
DATE CREATED: 28/11/2022 
DATE LAST UPDATED: 28/11/2022

PURPOSE:
Connect device to the serial, using the config file created by the launch GUI,
stored in InputFiles/SerialPorts/COMS_Config.csv (this path is hard coded) in the format:

component,connected,COMS
MainCamera,True,1
AzimuthAltitudeStand,False,0
Filter,True,0
Focuser,False,0
RGBCamera,False,0
'''
import pandas as pd
import serial.tools.list_ports
import serial

class ConnectSerial_class():
    """Connect given equipment to the serial"""
    def __init__(self):
        super(ConnectSerial_class,self).__init__()
        
    def connectSerial(self,equipment):
        """Connects the serial for the equipment"""
        connectionTF, comsno = self.ReadSerialCSV(equipment)
        if connectionTF == True: #is connected
            driver = serial.Serial(port="COMS" + str(comsno), baudrate=115200, timeout=.1)
            driver.open()
            return(driver)
        else:
            pass   
    
    def ReadSerialCSV(self,equipment):
        """Reads in which COMS to connect to for a given equipment device"""
        #dictionarys used to call in the correct row for a given equipment type
        abrvnamdict = {"M":0,"A":1,"Fi":2,"Fo":3,"R":4} #{"MainCamera":0,"AzimuthAltitudeStand":1,"Filter":2,"Focuser":3,"RGBCamera":4}
        #read in the dataframe from the stored csv
        CSVPath = "InputFiles/SerialPorts/COMS_Config.csv"
        df = pd.read_csv(CSVPath,header = 0)
        #select the correct row usingthe dictionary
        rowindex = abrvnamdict[equipment]
        connectionTF = df["connected"][rowindex]
        comsno = df["COMS"][rowindex] # coms number
        return(connectionTF, comsno)
        

            
    
 




        


      
