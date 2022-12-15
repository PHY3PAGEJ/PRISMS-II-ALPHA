"""
NAME: PositionFUNC.py
AUTHOR: John Archibald Page
DATE CREATED: 05/12/2022 
DATE LAST UPDATED: 07/12/2022

PURPOSE:
To write functionality to stand, using zaber-motion python library.
this funcitonality will be set to buttons in seperate document

PYTHON LIBRARY: zaber_motion
INSTALL VIA COMMANDLINE: pip install zaber_motion
DOCUMENTATION: https://www.zaber.com/software/docs/motion-library/ascii/references/python/ [Last Accessed 07/12/2022]
"""
import logging as log ##troubleshooting
log.info(__file__)  ##troubleshooting
from zaber_motion import Units, Library
from zaber_motion.ascii import Connection
import logging as log
from Interfacing.CSV.ReadCSV import Read_class
rc = Read_class()

class ZaberStand_class():
    """Build the functionality for the position controls"""
    def __init__(self):
        super(ZaberStand_class,self).__init__()
        #hard coded limits
        self.altlim = 60  #mechanical limit 66 before damaging attached equipment, 6 degrees less used as safty buffer
        #connect stand
        self.device_list = self.connectStand()

    #functions for connecting and writing to the devices
    def connectStand(self):
        Library.enable_device_db_store()
        connectedvalue = rc.readcol(filename="InputFiles\SerialPorts\COMS_Config.csv",col=2)
        #open using the zabermotion internal function
        connection = Connection.open_serial_port("COM"+str(connectedvalue[2]))
        device_list = connection.detect_devices()
        return(device_list)   

    def deviceList(self):  
        """Output the stepper motor references""" 
        altitude = self.device_list[1] #77260 = verital pivot
        azimuth = self.device_list[0] #77261 = horizontal pivot/azimuth 
        altitudeaxis = altitude.get_axis(1)   
        azimuthaxis = azimuth.get_axis(1)
        return(azimuthaxis,altitudeaxis)

    #sending commands to the device
    def moverelative(self,dir,amount):
        """Moves amount in unit degrees relative to current position"""
        #if nothing written in the input, moves 5 degrees
        if amount == "":
            amount = 5 # degrees
        else:
            amount = float(amount)
        #initalise dictionaries and devices
        aziax,altax = self.deviceList()
        reldict = {"u":1,"d":-1,"l":-1,"r":1} # relative directions
        axisdict = {"u":altax,"d":altax,"l":aziax,"r":aziax} # what axis is used
        #check limits
        altpos,azipos = self.currentposition() 
        posdict = {"u":altpos,"d":altpos,"l":azipos,"r":azipos} # what axis is used
        newpos = amount*reldict[dir]+ posdict[dir] # new position after being moved
        if (dir == "u" and newpos > self.altlim) or (dir == "d" and newpos < -self.altlim):
            log.info("Zaber Stand move out of range: Altitude -60 to 60") 
        else:
            axisdict[dir].move_relative(amount*reldict[dir], Units.ANGLE_DEGREES) 
            log.info("Zaber Stand has moved {} degrees to new position {}".format(amount*reldict[dir],axisdict[dir].get_position(unit = Units.ANGLE_DEGREES)))

    def moveabsolute(self,dir,abspos):
        """Moves to absolute position in degrees. the lineedit boxes, defined in GUI, 
        have limited inputs to stop going beyond mechanical limits: Altitude -60 to 60"""
        abspos = float(abspos)
        #write to a given axis
        aziax,altax = self.deviceList()
        axisdict = {"alt":altax,"azi":aziax}
        #make sure hard limits are met
        axisdict[dir].move_absolute(abspos, Units.ANGLE_DEGREES)
        axispos = axisdict[dir].get_position(unit = Units.ANGLE_DEGREES)
        log.info("Zaber Stand has moved to absolute position {} in {} direction".format(axispos,dir))

    def currentposition(self):
        """Returns current position of stand"""
        aziax,altax = self.deviceList()
        altpos = altax.get_position(unit = Units.ANGLE_DEGREES)
        azipos = aziax.get_position(unit = Units.ANGLE_DEGREES)
        log.info("Zaber Stand position initalised: Altitude = {}; Azimuth = {}".format(altpos,azipos))
        return(altpos,azipos)

    def setzero(self):
        """Sets the stand back to altitude, azimuth 0,0 degrees. This can be physically seen on the stand."""
        altpos,azipos = self.currentposition()
        #check which direction to move the stand, take shortest path to zero in degrees
        #altitude
        if altpos >= 0:
            self.moverelative("d",altpos)
        else:
             self.moverelative("u",-altpos)
        #azimuth
        if azipos >= 0:
            self.moverelative("l",azipos)
        else:
             self.moverelative("r",-azipos)
        log.info("Zaber stand has been returned to 0,0!")
   
    def busycheck(self):
        """Check if stand is moving in any direction"""
        altax,aziax = self.deviceList()
        if altax.is_busy():
            log.info("Altitude Adjusting...")
        if aziax.is_busy():
            log.info("Azimuth Adjusting...")

    def emergencySTOP(self):
        """Stops all motion and freezes further motion from the zaber stand"""
        altax,aziax = self.deviceList()
        altax.stop()
        aziax.stop()
        altax.wait_until_idle() # no new functions until this is stopped
        aziax.wait_until_idle() # no new functions until this is stopped
        log.info("ZABER STAND MOTION STOPPED!")



      
