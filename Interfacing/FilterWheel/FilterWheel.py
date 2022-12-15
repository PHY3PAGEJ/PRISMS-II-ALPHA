"""
NAME: FilterWheel.py
AUTHOR: John Archibald Page
DATE CREATED: 29/11/2022 
DATE LAST UPDATED: 13/12/2022

PURPOSE:
To write functionality to filter.
this funcitonality will be set to buttons in seperate document

 _Filter___________
| | u | <>| | ... ||
''''''''''''''''''''
<>:move the filter to the printed number, update the camera label
u: enter moves the filter to this one, update the label for the camera

"""
import logging as log ##troubleshooting
log.info(__file__)  ##troubleshooting
import struct
import logging as log

class FilterWheel_class():
    """Build the functionality for the filter controls, which takes binary commands given through serial"""
    def __init__(self):
        super(FilterWheel_class,self).__init__()
        #hard coded limits
        self.filterno = 5
        self.speedno = 7
        
    def setFilterWheel(self, filter, driver, speed=7):
        """Set filter wheel to given filter at given speed"""
        filters = {0: "0000", 1: "0001", 2: "0010", 3: "0011", 4: "0100", 5: "0101", 6: "0110", 7: "0111", 8: "1000", 9: "1001"}
        speeds = {0: "000", 1: "001", 2: "010", 3: "011", 4: "100", 5: "101", 6: "110", 7: "111"}
        #binary message to send to filter wheel
        message = struct.pack(">B", int("0"+ speeds[speed] + filters[filter],2))
        driver.write(message)
        log.info("The Filter has been set to filter {} and speed {}".format(filter,speed))


            
