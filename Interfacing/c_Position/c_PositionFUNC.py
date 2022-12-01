"""
NAME: c_PositionFUNC.py
AUTHOR: John Archibald Page
DATE CREATED: 28/11/2022 
DATE LAST UPDATED: 28/11/2022

PURPOSE:
To write functionality to stand, using zaber-motion python library.
this funcitonality will be set to buttons in seperate document

          _Orientation______________
        |     | u |       Azimuth |
        | ___ ===== ___   |      ||
        || < ||   || > |   '''''' |
        | ''' ===== '''   Altitude|
        |     | d |       |______||
        |      '''        |set0,0||
        |                  '''''' |
        '''''''''''''''''''''''''''
up: click = move k  amount, if no k then move *** amount. held for 3s+: Move at ***/s, held 5s+: move at /2, realesed: Stop
down: click = move k  amount, if no k then move *** amount. held for 3s+: Move at ***/s, held 5s+: move at /2, realesed: Stop
anti-clockwise: click = move k  amount, if no k then move *** amount. held for 3s+: Move at ***/s, held 5s+: move at /2, realesed: Stop
clockwise: click = move k  amount, if no k then move *** amount. held for 3s+: Move at ***/s, held 5s+: move at /2, realesed: Stop
Azimuth: Prints current position. If input position, then move to this posiiton.
Altitude: Prints current position. If input position, then move to this posiiton.
set 0,0: cliccked = current position becomes zero, have a double check on this

To connect the buttons they all need reference options. this can be done by taking th egroup from PRISMS GUI and calling
the child
"""

from ConnectSerial import ConnectSerial_class
from zaber_motion import Units, Library
from zaber_motion.ascii import Connection

class PositionFUNC_class():
    """Build the functionality for the position controls"""
    def __init__(self):
        super(PositionFUNC_class,self).__init__()
        self.sethardlimits()

    def sethardlimits(self):
        """Sets hard coded limits on the motion of the stand, to stop equipment being taken out or wires tangled"""
        #altitude
        self.altlim = 66 # degrees either side of 0 degrees to stop equipment hitting stand
        #speed

    def connectStand(self):
        Library.enable_device_db_store()
        connectionTF, comsno = ConnectSerial_class.ReadSerialCSV("A") #read in form the config coms file made by launch
        connection = Connection.open_serial_port("COM"+str(comsno))
        device_list = connection.detect_devices()
        altitude = device_list[1] #77260 = verital pivot
        azimuth = device_list[0] #77261 = horizontal pivot/azimuth 
        altitudeaxis = altitude.get_axis(1)   
        azimuthaxis = azimuth.get_axis(1)
        return(altitudeaxis,azimuthaxis)

    def moverelative(self,dir,amount):
        """Moves amount in unit degrees relative to current position"""
        #if nothing written in the input, moves set amount
        if amount == "":
            amount = 5
        #makes sure not to go out of range for the altitude
        if dir == "u" or dir == "d":
            if amount > self.altlim:
                pass
            else:
                altax,aziax = self.connectStand()
                reldict = {"u":1,"d":-1,"l":-1,"r":1}
                axisdict = {"u":altax,"d":altax,"l":aziax,"r":aziax}
                axisdict[dir].move_relative(reldict[dir]*amount, Units.ANGLE_DEGREES)
        return("Zaber Stand has moved "+ str(reldict[dir]*amount)+ " degrees to new position " +str(axisdict[dir].get_position(unit = Units.ANGLE_DEGREES)))

    def moveabsolute(self,dir,abspos):
        """Moves to absolute position in degrees"""
        #if nothing written in the input, moves set amount
        altax,aziax = self.connectStand()
        axisdict = {"alt":altax,"azi":aziax}
        #make sure hard limits are met
        if dir == "alt":
            if self.altlim< abspos < 360 - self.altlim:
                return("Zaber Stand absolute position out of altitdude range of +/-"+str(self.altlim) +" degrees about zero position.")
        else:
            axisdict[dir].move_absolute(abspos, Units.ANGLE_DEGREES)
            axispos = axisdict[dir].get_position(unit = Units.ANGLE_DEGREES)
        return("Zaber Stand has moved to absolute position "+str(axispos) + " in "+ str(dir) + "direction")

    def currentposition(self):
        """Returns current position of stand"""
        altax,aziax = self.connectStand()
        altpos = altax.get_position(unit = Units.ANGLE_DEGREES)
        azipos = aziax.get_position(unit = Units.ANGLE_DEGREES)
        return("Zaber Stand position: Altitude = "+str(altpos) + "; Azimuth = "+str(azipos),altpos,azipos)

    def busycheck(self):
        """Check if stand is moving in any direction"""
        altax,aziax = self.connectStand()
        if altax.is_busy():
            return("Altitude Adjusting...")
        if aziax.is_busy():
            return("Azimuth Adjusting...")

    def emergencySTOP(self):
        """Stops all motion and freezes further motion from the zaber stand"""
        altax,aziax = self.connectStand()
        altax.stop()
        aziax.stop()
        altax.wait_until_idle() # no new functions until this is stopped
        aziax.wait_until_idle() # no new functions until this is stopped
        return("ZABER STAND MOTION STOPPED!")

    def setzero(self):
        """Sets the stand back to altitude, azimuth 0,0 degrees. This can be physically seen on the stand."""
        msg,altpos,azipos = self.currentposition()
        #check which direction to move the stand, take shortest path to zero in degrees
        if altpos <= 180:
            self.moverelative(self,"d",altpos)
        else:
             self.moverelative(self,"u",360-altpos)
        
        if azipos <= 180:
            self.moverelative(self,"l",altpos)
        else:
             self.moverelative(self,"r",360-altpos)
        return("Zaber stand has been returned to 0,0")

      
