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
import serial.tools.list_ports
import serial
import logging as log
from Interfacing.CSV.ReadCSV import Read_class
rc = Read_class()

class ConnectSerial_class():
    """Connect given equipment to the serial"""
    def __init__(self):
        super(ConnectSerial_class,self).__init__()

    def connectSerial(self,equip,br):
        """Connects the serial for the equipment"""
        #check the config folder
        connectedvalue = rc.readcol(filename="InputFiles\SerialPorts\COMS_Config.csv",col=1)
        connectedvalue = [ True if x == "True" else False for x in connectedvalue ] # convert to boolean
        comsno = rc.readcol(filename="COMS_Config.csv",savepath="InputFiles\SerialPorts", col=2)
        #depending on selection set i
        dictequip = {"C":1,"P":2,"Fi":3,"Fo":4,"RGB":5}
        i = dictequip[equip]
        if connectedvalue[i] == True: #is connected
            driver = serial.Serial(port="COM{}".format(comsno[i]), baudrate=br, timeout=.1)
            if(driver.isOpen() == False): #if not already connected, open the driver
                driver.open()
            
            log.info("COM{} has been opened!".format(comsno[i]))
        return(driver)
 
        

            
    
 




        


      
