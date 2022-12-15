"""
NAME: FilterCON.py
AUTHOR: John Archibald Page
DATE CREATED: 29/11/2022 
DATE LAST UPDATED: 06/12/2022

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
from Interfacing.FilterWheel.FilterWheel import FilterWheel_class
from Interfacing.ConnectSerial import ConnectSerial_class
from ConnectingWidgets.ConnectFunctions import ConnectFunctions_class 

class FilterCON_class():
    """Build the functionality for the Filter controls"""
    def __init__(self,FGUI,CGUI):
        super(FilterCON_class,self).__init__()
        #initalise class, this also connects the device
        self.cf = ConnectFunctions_class()
        self.func = FilterWheel_class()
        self.cs = ConnectSerial_class()
        #connect buttons
        self.spinwheelconnect(FGUI,CGUI)
        #initalise connection
        self.driver = self.cs.connectSerial("Fi",9600) # connect the filter wheel via serial

    #connect buttons functionality   
    def spinwheelconnect(self,FGUI,CGUI):
        """Connect spinwheel functionality"""
        spinwheellist = self.cf.spinboxrefences(FGUI)
        spinwheel = spinwheellist[0]
        spinwheel.valueChanged.connect(lambda: self.updatelabelandmovespinwheel(FGUI,CGUI))

    def updatelabelandmovespinwheel(self,FGUI,CGUI):
        """Comnbine the update label and move the wpin wheel by combining the funcitons"""
        spinwheellist = self.cf.spinboxrefences(FGUI)
        spinwheel = spinwheellist[0]
        self.func.setFilterWheel(spinwheel.value(),self.driver) # move the spin filter
        self.updateLabelconnect(FGUI,CGUI) # update the label

    def updateLabelconnect(self,FGUI,CGUI):
        """Update the label for the camera GUI to show what filter is shown"""
        #reference to the checkbox
        label = self.cf.labelrefences(CGUI)
        changelab = label[0]
        #reference to spin box
        spinwheellist = self.cf.spinboxrefences(FGUI)
        spinwheel = spinwheellist[0]
        #reference to check mark of rgb camera
        checkbox = self.cf.checkboxrefences(CGUI)
        RGBCamera = checkbox[2]
        if RGBCamera.isChecked() == False:
            changelab.setText("Filter "+str(spinwheel.value()))
        else:
            changelab.setText("RGB Camera")


    
        