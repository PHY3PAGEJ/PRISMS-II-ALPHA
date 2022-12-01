"""
NAME: d_FilterCON.py
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
from PyQt5 import QtWidgets
from d_FilterFUNC import FilterFUNC_class as ff
from Interfacing.ConnectFunctions import ConnectFunctions_class as cf

class FilterFUNC_class():
    """Build the functionality for the Filter controls"""
    def __init__(self):
        super(FilterFUNC_class,self).__init__()
        
    def spinwheelconnect(self,FGUI,CGUI):
        """Connect spinwheel functionality"""
        spinwheel = cf.spinboxrefences(FGUI)
        spinwheel.valueChanged.connect(lambda: self.updatelabelandmovespinwheel(FGUI,CGUI))
        cf.buttonconnect(returnfunction=lambda: self.updatelabelandmovespinwheel(FGUI,CGUI))

    def updateLabelconnect(self,FGUI,CGUI):
        """Update the label for the camera GUI to show what filter is shown"""
        #reference to the checkbox
        label = cf.labelrefences(CGUI)
        changelab = label[0]
        #reference to spin box
        spinwheel = cf.spinboxrefences(FGUI)
        #reference to check mark of rgb camera
        checkbox = cf.checkboxrefences(CGUI)
        RGBCamera = checkbox[2]
        if RGBCamera.isChecked() == False:
            changelab.setText("Filter "+str(spinwheel.value()))
        else:
            pass

    def updatelabelandmovespinwheel(self,FGUI,CGUI):
        """Comnbine the update label and move the wpin wheel by combining the funcitons"""
        spinwheel = cf.spinboxrefences(FGUI)
        ff.setFilterWheel(spinwheel.value()) # move the spin filter
        self.updateLabelconnect(FGUI,CGUI) # update the label


    
        