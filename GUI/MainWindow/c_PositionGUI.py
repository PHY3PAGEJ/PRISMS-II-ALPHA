'''
NAME: c_PositionGUI.py
AUTHOR: John Archibald Page
DATE CREATED: 17/11/2022 
DATE LAST UPDATED: 01/12/2022

PURPOSE:
To create the buttons for position GUI, with mock up shown in Mock-up.PNG.
    _Orientation______________
    |     | u |       Azimuth |
    | ___ ===== ___   |______||
    || < ||___|| > |  Altitude|
    | --- | d | ---   |______||
    |      ---        |0,0 __||
    |_________________________|

UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up
'''
from PyQt5 import QtWidgets,QtGui

class PositionGUI_class():
    """Build the GUI for the position controls"""
    def __init__(self):
        super(PositionGUI_class,self).__init__()
        self.MaingroupBox = self.BuildLayout()
    
    def BuildLayout(self):
        """Build the Orientation of PRISMS II widgets group"""
        #call in widgets
        leftButton,rightButton,upButton,downButton,setzeroButton = self.Buttons()
        StepSize = self.Textbox(info="Increment steps in degrees", label=False)
        aziLayout = self.Textbox(info="Azimuth Position", label="Azimuth")
        altLayout = self.Textbox(info="Altitude Position", label="Altitude")
        #make groupbox for widgets to sit in
        groupBox = QtWidgets.QGroupBox("Orientation")
        #main dial button grid layout, set like a 3 x 3 shown below
        #|1||2||3|
        #|4||5||6|
        #|7||8||9|
        glayout = QtWidgets.QGridLayout()
        glayout.addWidget(upButton,0,1) # 2
        glayout.addWidget(leftButton,1,0) # 4
        glayout.addWidget(StepSize,1,1) # 5
        glayout.addWidget(rightButton,1,2) # 6
        glayout.addWidget(downButton,2,1) # 8
        glayout.setColumnStretch(0, 1)
        glayout.setColumnStretch(1, 1)
        glayout.setColumnStretch(2, 1)
        #Make theend column of vertical layout for the azimuth and altitude values, with orientation:
        #|_|
        #| |
        azialtLayout = QtWidgets.QVBoxLayout()
        azialtLayout.addLayout(aziLayout, 1)
        azialtLayout.addLayout(altLayout, 1)
        azialtLayout.addWidget(setzeroButton,1)
        # combine the grid and vertical layouts using a horizontal layout:
        #| Grid | Vertical |
        HLayout = QtWidgets.QHBoxLayout()
        HLayout.addLayout(glayout, 7)
        HLayout.addLayout(azialtLayout, 3)
        #add the layout to the group
        groupBox.setLayout(HLayout)
        return(groupBox)

    def Buttons(self):
        """Define the buttons of the position GUI"""
       #left button
        leftButton = QtWidgets.QPushButton()
        leftButton.setText(u"\u21BA")
        leftButton.setToolTip("Rotate anticlockwise")
        #right button
        rightButton = QtWidgets.QPushButton()
        rightButton.setText(u"\u21BB")
        rightButton.setToolTip("Rotate clockwise")
        #up button
        upButton = QtWidgets.QPushButton()
        upButton.setText(u"\u25B4")
        upButton.setToolTip("Tilt upwards")
        #down button
        downButton = QtWidgets.QPushButton()
        downButton.setText(u"\u25BC")
        downButton.setToolTip("Tilt downwards")
        #set zero location button
        setzeroButton = QtWidgets.QPushButton()
        setzeroButton.setText("(0,0)")
        setzeroButton.setToolTip("Set the position to (0,0) for the Altitude and Azimuth")
        #connect button functionality to clicked and enter button
        return(leftButton,rightButton,upButton,downButton,setzeroButton)

    def Textbox(self, info, label):
        """define the input text boxes, and whether it has a label"""
        #initalise float inputs
        Value = QtWidgets.QLineEdit()
        #make only accept numbers by making validator
        dv = QtGui.QDoubleValidator(0.0, 1000000.0, 2) # [0, 5] with 2 decimals of precision
        dv.setNotation(QtGui.QDoubleValidator.StandardNotation) # no scientifc notation accepted
        #apply validator
        Value.setValidator(dv)
        ##Add tool tips
        Value.setToolTip(info)
        #if there is a label, it is stacked on top of the linedit with a vertical layout:
        #|_|
        #| |
        if label != False:
            labelwidget = QtWidgets.QLabel()
            labelwidget.setText(label)
            VLayout = QtWidgets.QVBoxLayout() 
            VLayout.addWidget(labelwidget, 2)
            VLayout.addWidget(Value, 8)
            return(VLayout)
        else:
            return(Value)
    
      
