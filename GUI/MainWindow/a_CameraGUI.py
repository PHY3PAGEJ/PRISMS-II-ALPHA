'''
NAME: a_CameraGUI.py
AUTHOR: John Archibald Page
DATE CREATED: 17/11/2022 
DATE LAST UPDATED: 05/12/2022

PURPOSE:
To create the buttons Camera GUI, with format shown below:

 __Camera_______________________
|SAVE_IMAGE|______Label_________|
|		                        |                   
|                               |  
|  DISPLAY  FRAME               |
|                               |          
|_______________________________|
|__Toggles______________________|               
| ___  ___  ___ |Dark Correction|          
||   ||   ||   |||   ||Set Dark||
| ROI  1:1  RGB | Show '''''''' |
|---------------|---------------| 
UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up

'''
import logging as log ##troubleshooting
log.info(__file__)  ##troubleshooting
from PyQt5 import QtWidgets, QtGui, QtCore
import pyqtgraph as pg
from scipy import misc 
from GUI.SelfDefinedWidgets.PushButton_saveopendir import saveopendirPushButton
from GUI.SelfDefinedWidgets.StackedWidget import StackedWidget_class
sw = StackedWidget_class()

class CameraGUI_class():
    """Build the GUI for the camera settings, contating controls for Focus and Exposure"""
    def __init__(self):
        super(CameraGUI_class,self).__init__()
        self.MaingroupBox = self.BuildMainLayout()

    def BuildMainLayout(self):
        """Build the main camera GUI layout"""
        #make main groupbox
        MaingroupBox = QtWidgets.QGroupBox("Camera")
        VLayout = QtWidgets.QVBoxLayout() 
        MaingroupBox.setLayout(VLayout)
        #initiate the sub groups
        toggleLayout = self.BuildtoggleLayout()
        savelablayout = self.BuildsavlabLayout()
        dFramewidget = self.displayFrame()
        #set subgroups into the maingroup
        VLayout.addLayout(savelablayout, 1)
        VLayout.addWidget(dFramewidget, 8)
        VLayout.addWidget(toggleLayout, 1)
        #set margins
        VLayout.setContentsMargins(20, 20, 20, 20)
        #switch out for placeholder if rgb and main not connected
        stackedgroup = sw.stackplaceholderWidget(MaingroupBox)
        return(stackedgroup)

    def displayFrame(self):
        """This is a place holder until the camera is called in"""
        dFramewidget = QtWidgets.QLabel()
        pixmax = QtGui.QPixmap('GUI/Images/PlaceHolder.png')
        myScaledPixmap = pixmax.scaled(dFramewidget.size(), QtCore.Qt.KeepAspectRatio)
        dFramewidget.setPixmap(myScaledPixmap)
        return(dFramewidget)
    
    #def displayFrame(self,image='GUI/Images/PlaceHolder.png'):
    #        """Creates pyqtgraph to update with the image"""
    #        #call in placeholder as a 2d np.array
    #        im = misc.imread(image)#
    #
    #      # Create the main pyqtgraph GraphicsLayoutWidget
    #        self.glw = pg.GraphicsLayoutWidget()
    #
    #        # Create the plotting axes in the GraphicsLayoutWidget
    #        self.plot = self.glw.addPlot()
    #        self.plot.setLabels(left="Pixel #", bottom="Pixel #")
    #        
    #        # Create the image item and add it to the plot
    #        self.image = pg.ImageItem()
    #        self.plot.addItem(self.image)
        
    def BuildsavlabLayout(self):
        """Build the buttons stored at the top of the widget:
         _______________________________
        |SAVE_IMAGE|______Label_________|
        
        """
        #call in widgets
        saveButton,darkButton = self.Buttons()
        visualLabel = self.labels()
        # Horizontal orientation, as shown in the diagram
        HLayout = QtWidgets.QHBoxLayout()
        #add the horizontal widgets |  save  |  label #  | 
        HLayout.addWidget(saveButton)
        HLayout.addWidget(visualLabel)
        #add alignment within layout
        visualLabel.setAlignment(QtCore.Qt.AlignRight)
        return(HLayout)
    
    def BuildtoggleLayout(self):
        """Build the bottom region of the Camera GUI where the checkboxes can be toggled:
         __Toggles______________________               
        | ___  ___  ___ |Dark Correction|          
        ||   ||   ||   |||   ||Set Dark||
        | ROI  1:1  RGB | Show '''''''' |
        |_______________|_______________| 
        """
        #call in widgets
        darkgroup = self.BuilddarkLayout()
        ROIToggle,D1Toggle,RGBToggle,dcToggle = self.toggles()
        #make groupbox for widgets to sit in
        SubgroupBox = QtWidgets.QGroupBox("Toggles")
        # Horizontal orientation, as shown in the diagram
        HLayout = QtWidgets.QHBoxLayout()
        #add the horizontal widgets |  t1  |  t2  |  t3  |  dark correction  | 
        HLayout.addWidget(ROIToggle,2)
        HLayout.addWidget(D1Toggle,2)
        HLayout.addWidget(RGBToggle,2)
        HLayout.addWidget(darkgroup,2)
        SubgroupBox.setLayout(HLayout)
        #switch out for placeholder if rgb and main not connected
        stackedgroup = sw.stackplaceholderWidget(SubgroupBox)
        return(stackedgroup)

    def BuilddarkLayout(self):
        """Build the layout for settitng the dark, whioch then will be on the irght hand
        side of the toggles layout (See above):
        ________________               
        |Dark Correction|          
        ||   ||Set Dark||
        | Show '''''''' |
        |_______________| 
        """
        #call in widgets
        saveButton,darkButton = self.Buttons()
        ROIToggle,D1Toggle,RGBToggle,dcToggle = self.toggles()
        #make groupbox for widgets to sit in
        SubgroupBox = QtWidgets.QGroupBox("Dark Correction")
        # vertical orientation, as shown in the diagram
        HLayout = QtWidgets.QHBoxLayout()
        #add the horizontal widgets |  toggle  |  Set Dark   |  
        HLayout.addWidget(dcToggle, 3)
        HLayout.addWidget(darkButton, 7)
        SubgroupBox.setLayout(HLayout)
        return(SubgroupBox)

    def Buttons(self):
        """Define the buttons used for the whole camera GUI, of which there is only 'save image' and 'set'"""
       #save button
        saveButton = saveopendirPushButton("Save Image", savediropen="save",filepurpose= "Image", filepath = "/OutputFiles/Images/", filetype="image")
        saveButton.setToolTip("Saves current screen as .TIFF, with .DAT and option to save RGB image too")
        #set dark button
        darkButton = saveopendirPushButton("Set",savediropen="open",filepurpose= "set dark", filepath = "/OutputFiles/Darks/", filetype="image")
        darkButton.setToolTip("Set the dark correction to an existing file")
        return(saveButton,darkButton)

    def labels(self):
        """Display title for the camera, stating the filter for the main camera, or just stating RGB if toggled"""
        visualLabel = QtWidgets.QLabel("Filter 1")
        visualLabel.setToolTip("Current visual Information")
        return(visualLabel)

    def toggles(self):
        """The toggles for the camera GUI"""
        #ROI: Region of interest, shows a rectangular area that the focus is calculated from
        ROIToggle = QtWidgets.QCheckBox("ROI")	
        ROIToggle.setToolTip("Show ROI on main camera")
        #Display 1:1: shows just the ROI area as the full camera widget area
        D1Toggle = QtWidgets.QCheckBox("1:1")
        D1Toggle.setToolTip("Show just ROI as 1:1 display")
        #RGB: switches to just the RGB camera
        RGBToggle = QtWidgets.QCheckBox("RGB")
        RGBToggle.setToolTip("Show RGB Camera")
        stackedRGB = sw.stackplaceholderWidget(RGBToggle)
        #show dark correction: shows either a lens cap dark correction, or a dark using the set dark image.
        dcToggle = QtWidgets.QCheckBox("Show")
        dcToggle.setToolTip("Apply dark correction")
        return(ROIToggle,D1Toggle,stackedRGB,dcToggle)