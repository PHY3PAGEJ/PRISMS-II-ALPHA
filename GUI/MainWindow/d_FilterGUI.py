'''
NAME: d_FilterGUI.py
AUTHOR: John Archibald Page
DATE CREATED: 18/11/2022 
DATE LAST UPDATED: 01/12/2022

PURPOSE:
To create the Filter GUI:
 _Filter___________
| | u | <>| | ... ||
''''''''''''''''''''

UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up
'''
import logging as log ##troubleshooting
log.info(__file__)  ##troubleshooting
from PyQt5 import QtWidgets
from GUI.SelfDefinedWidgets.PushButton_popupMessage import moreinfoPushButton
from GUI.SelfDefinedWidgets.StackedWidget import StackedWidget_class
sw = StackedWidget_class()

messagefile = "GUI/AdditionalWindows/Messages/Filter_moreinfo.csv"

class FilterGUI_class():
    """Build the GUI for the filter wheel setting"""
    def __init__(self):
        super(FilterGUI_class,self).__init__()
        self.MaingroupBox = self.BuildLayout()
    
    def BuildLayout(self):
        """Build the Layout of PRISMS II widgets group, which has the following layout:
          _Filter___________
         | | u | <>| | ... ||
          '''''''''''''''''' 
       """
        #call in widgets
        self.swBox = self.SpinWheel()
        iButton = self.infoButton()
        #make groupbox for widgets to sit in
        groupBox = QtWidgets.QGroupBox("Filter")
        #layout Buttons
        filterLayout = QtWidgets.QHBoxLayout()
        filterLayout.addWidget(self.swBox, 7)
        filterLayout.addWidget(iButton, 3)
        #add the layout to the group
        groupBox.setLayout(filterLayout)
        stackedgroup = sw.stackplaceholderWidget(groupBox)
        return(stackedgroup)

    def SpinWheel(self):
        """Define the filter spinbox choices"""
        spinWheel = QtWidgets.QSpinBox()
        spinWheel.setWrapping(True) # when go to top number, goes back to first
        spinWheel.setRange(0, 9) # 0-9
        spinWheel.setToolTip("Which filter is selected, 0-9")
        return(spinWheel)

    def infoButton(self):
        """Define the button"""
       #left button
        iButton = moreinfoPushButton(messagefile)
        return(iButton)

  
    
      
