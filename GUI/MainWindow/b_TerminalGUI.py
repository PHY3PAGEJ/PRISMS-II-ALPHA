'''
NAME: b_TerminalGUI.py
AUTHOR: John Archibald Page
DATE CREATED: 17/11/2022 
DATE LAST UPDATED: 01/12/2022

PURPOSE:
To create the widgets for, and format the layout of, a terminal GUI. 
 __Terminal_______________
| _______________________ |                
||>unselectable Terminal ||             
||                       ||             
||                       ||   
||                       ||               
||_______________________||                                
||Input_line______|GO|...||
|-------------------------|

UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up
'''
from PyQt5 import QtCore, QtWidgets
from SelfDefinedWidgets.TextEdit_AutoverticleExpansion import GrowingTextEdit
from SelfDefinedWidgets.PushButton_popupMessage import moreinfoPushButton

messagefile = "GUI/AdditionalWindows/Messages/Terminal_moreinfo.csv"

class TerminalGUI_class():
    """Make the GUI for the Terminal"""
    def __init__(self):
        super(TerminalGUI_class,self).__init__()
        self.MaingroupBox = self.BuildTerminal()

    def BuildTerminal(self):
        """Build the main layout for th terminal GUI"""
        #initiate buttons
        scrollArea = self.terminalScript()
        inputLine = self.terminailInput()
        goButton = self.goButton()
        lcButton = self.listcommandsButton()
        # vertical orientation, as shown in the diagram
        inputLayout = QtWidgets.QHBoxLayout()
        overallLayout = QtWidgets.QVBoxLayout() 
        #add the widgets
        inputLayout.addWidget(inputLine, 8)
        inputLayout.addWidget(goButton, 1)
        inputLayout.addWidget(lcButton, 1)
        overallLayout.addWidget(scrollArea, 9)
        overallLayout.addLayout(inputLayout, 1)
        #make Group box
        terminalgroupbox = QtWidgets.QGroupBox("Terminal")
        terminalgroupbox.setLayout(overallLayout)
        return(terminalgroupbox)

    def terminalScript(self):
        """Create a scrollable area that automatically grows to use as terminal"""
        #text edit box properties and location---
        textbox = GrowingTextEdit()
        textbox.setMinimumHeight(50)
        textbox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff) #switch off automatic vertical box for textedit
        #settextboxproperties
        textbox.setTextInteractionFlags(QtCore.Qt.NoTextInteraction) 
        #verticle scroll area and scroll area widget---
        scrollArea = QtWidgets.QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollArea.setWidget(textbox)
        scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff) # switch off horizontal scroll
        vbar = scrollArea.verticalScrollBar()
        vbar.setValue(vbar.maximum()) #start at maximum verticle area
        return(scrollArea)
        
    def terminailInput(self):
        """input commands to the input line to write to terminal"""
        inputline = QtWidgets.QLineEdit()
        return(inputline)

    def goButton(self):
        """Sends the command typed into the input line to the terminal"""
        gobutton = QtWidgets.QPushButton()
        gobutton.setText("GO")
        gobutton.setToolTip('This is an enter button')
        return(gobutton)

    def listcommandsButton(self):
        """opens a message pop-up of the list of available commands"""
        lcbutton = moreinfoPushButton(messagefile)
        return(lcbutton)
       

