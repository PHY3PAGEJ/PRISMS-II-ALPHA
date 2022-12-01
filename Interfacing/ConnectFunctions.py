"""
NAME: ConnectFunctions.py
AUTHOR: John Archibald Page
DATE CREATED: 28/11/2022 
DATE LAST UPDATED: 28/11/2022

PURPOSE:
a class of functions used for connecting buttons which will be used multiple times.
"""
from PyQt5 import QtWidgets
from PRISMS_II_GUI.SelfDefinedWidgets.PushButton_HoldDownButton import HoldDownButton_class

class ConnectFunctions_class():
    """connect the position buttons for position"""
    def __init__(self,Groupbox):
        super(ConnectFunctions_class,self).__init__()
    
    def Textboxrefences(self, Groupbox):
        """draw the references to the different groups"""
        tblist = Groupbox.findChildren(QtWidgets.QLineEdit)
        return(tblist)

    def Texteditrefences(self, Groupbox):
        """draw the references to the different groups"""
        telist = Groupbox.findChildren(QtWidgets.QTextEdit)
        return(telist)

    def pushbuttonsrefences(self, Groupbox):
        """draw the references to the different groups"""
        pblist = Groupbox.findChildren(QtWidgets.QPushButton)
        return(pblist)

    def checkboxrefences(self, Groupbox):
        """draw the references to the different groups"""
        cblist = Groupbox.findChildren(QtWidgets.QCheckBox)
        return(cblist)

    def spinboxrefences(self, Groupbox):
        """draw the references to the different groups"""
        sblist = Groupbox.findChildren(QtWidgets.QSpinBox)
        return(sblist)

    def labelrefences(self, Groupbox):
        """draw the references to the different groups"""
        llist = Groupbox.findChildren(QtWidgets.QLabel)
        return(llist)

    def heldconnect(self,button,func1,at):
        """Hold down button to move in given direction"""
        button.pressed.connect(lambda: HoldDownButton_class.buttonheld(func1, at))
        button.released.connect(HoldDownButton_class.buttonreleased())

    def buttonconnect(self,button,clickedfunction=False, pressedfunction=False,releasedfunction=False, returnfunction=False, heldfunction=False):
        """Connects button/widget to functionality"""
        if clickedfunction != False:
            button.clicked.connect(clickedfunction)
        if pressedfunction != False:
            button.pressed.connect(pressedfunction)
        if releasedfunction != False:
            button.released.connect(releasedfunction)
        if returnfunction != False:
            button.returnPressed.connect(releasedfunction)
        if heldfunction != False:
            self.heldconnect(button,heldfunction,at=3000)

        



        
      
