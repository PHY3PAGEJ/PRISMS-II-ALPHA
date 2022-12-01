"""
NAME: d_FilterFUNC.py
AUTHOR: John Archibald Page
DATE CREATED: 29/11/2022 
DATE LAST UPDATED: 29/11/2022

PURPOSE:
To write functionality to filter.
this funcitonality will be set to buttons in seperate document

 _Filter___________
| | u | <>| | ... ||
''''''''''''''''''''
<>:move the filter to the printed number, update the camera label
u: enter moves the filter to this one, update the label for the camera

"""
from ConnectSerial import ConnectSerial_class as cs
import struct

class FilterFUNC_class():
    """Build the functionality for the filter controls, which takes binary commands given through serial"""
    def __init__(self):
        super(FilterFUNC_class,self).__init__()
        self.FilterDriver = cs.connectSerial("Fi") # connect the filter wheel via serial
        filter, speed = self.defaultsettings(self)
        #initalise filter to setting 5
        self.setFilterWheel(filter, speed)
    
    def defaultsettings(self):
        """This is the default filter wheel settings, that is hard coded"""
        filterno = 5
        speedno = 7
        return(filterno,speedno)
    
    def setFilterWheel(self, filter, speed):
        """Set filter wheel to given filter at given speed"""
        filters = {0: "0000", 1: "0001", 2: "0010", 3: "0011", 4: "0100", 5: "0101", 6: "0110", 7: "0111", 8: "1000", 9: "1001"}
        speeds = {0: "000", 1: "001", 2: "010", 3: "011", 4: "100", 5: "101", 6: "110", 7: "111"}
        #binary message to send to filter wheel
        message = struct.pack(">B", int("0"+ speed[speed] + filter[filter],2))
        self.FilterDriver.write(message)
        return("The Filter has been set to filter "+str(filter) + " and speed " + str(speed))
            
