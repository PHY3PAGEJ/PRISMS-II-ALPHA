'''
NAME: LaunchSerial.py
AUTHOR: John Archibald Page
DATE CREATED: 22/11/2022 
DATE LAST UPDATED: 28/11/2022

PURPOSE:
To create the launch functionality
>read in available ports 
>print ports as com 1, com 2 etc. to the textedit script 

UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up

'''
import serial.tools.list_ports

class serialport_class():
    """reading in the serial ports"""
    def __init__(self):
        super(serialport_class,self).__init__()

    def serial_port(self):
        """Reads in the existing serial port numbers and names"""
        ports = serial.tools.list_ports.comports()
        
        if len(ports) == 0:
            return ("No Ports Available...")
        else:
            comno = ["{}".format(port) for port, desc, hwid in sorted(ports)]
            full_name = ["{} [{}]".format(desc, hwid) for port, desc, hwid in sorted(ports)]
            return (comno, full_name)

    def serialfullnamefunc(self):
        """Full name of the serial port to be printed in the info box"""
        if type(self.serial_port()) is not tuple:
            fullname = self.serial_port()
        else:
            comno, fullname = self.serial_port()
            fullname = '<br>'.join(fullname)
        return(fullname)
    
    def serialcomnamefunc(self):
        """com name of the serial port to be printed in the text box"""
        if type(self.serial_port()) is not tuple:
            comname = self.serial_port()
        else:
            comno, fullname = self.serial_port()
            comnolist = []
            for i in range(len(comno)):
                justnum = ''.join(filter(str.isdigit, comno[i]))#strip words just return number
                comnolist.append("COMS "+justnum)
            if len(comno)>1:    
                comname = '<br>'.join(comnolist)
                return(comname)
            else:
                return(comnolist[0])
        
        




