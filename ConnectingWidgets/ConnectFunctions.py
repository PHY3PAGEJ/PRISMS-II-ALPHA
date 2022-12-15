"""
NAME: ConnectFunctions.py
AUTHOR: John Archibald Page
DATE CREATED: 28/11/2022 
DATE LAST UPDATED: 28/11/2022

PURPOSE:
a class of functions used for connecting buttons which will be used multiple times.

UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up
"""
import logging as log ##troubleshooting
log.info(__file__)  ##troubleshooting
from PyQt5 import QtWidgets
from GUI.SelfDefinedWidgets.PushButton_HoldDownButton import HoldDownButton_class

class ConnectFunctions_class():
    """connect the position buttons for position"""
    def __init__(self):
        super(ConnectFunctions_class,self).__init__()

#references

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

    def stackedrefences(self, Groupbox):
        """draw the references to the different groups"""
        llist = Groupbox.findChildren(QtWidgets.QStackedWidget)
        return(llist)

#interacting with widgets

    def setvaluesofwidget(self,widget,val): #'toggles and line edits, have option for a list
        """Read in the check boxes and spin box values"""
        #check type of widget
        if type(widget) == list:
            for i in range(len(widget)):
                widgettype = type(widget[i])
                if widgettype == QtWidgets.QCheckBox:
                    val = widget[i].setChecked()
                if widgettype == QtWidgets.QSpinBox:
                    val = widget[i].setValue()
                else:
                    val = widget[i].setText()
        else:
            widgettype = type(widget)
            if widgettype == QtWidgets.QCheckBox:
                val = widget.setChecked()
            if widgettype == QtWidgets.QSpinBox:
                val = widget.setValue()
            else:
                val = widget.setText()

    def readvaluesofwidget(self,widget): #set this for toggles and line edits, have options for a list input
        """Read in the check boxes and spin box values"""
        if type(widget) == list:
            for i in range(len(widget)):
                widgettype = type(widget[i])
                if widgettype == QtWidgets.QCheckBox:
                    val = widget[i].isChecked()
                if widgettype == QtWidgets.QSpinBox:
                    val = widget[i].Value()
                else:
                    val = widget[i].Text()
        else:
            widgettype = type(widget)
            if widgettype == QtWidgets.QCheckBox:
                val = widget.isChecked()
            if widgettype == QtWidgets.QSpinBox:
                val = widget.Value()
            else:
                val = widget.Text()
        return(val)

#connecting widgets

    def heldconnect(self,button,func1,at):
        """Hold down button to move in given direction"""
        self.hdb = HoldDownButton_class(func1, at)
        button.pressed.connect(lambda: self.hdb.buttonheld(func1, at))
        button.released.connect(self.hdb.buttonreleased)

    def buttonconnect(self,button,clickedfunction=False, pressedfunction=False,releasedfunction=False, returnfunction=False, heldfunction=False):
        """Connects button/widget to functionality"""
        if clickedfunction != False:
            button.clicked.connect(clickedfunction)
        if pressedfunction != False:
            button.pressed.connect(pressedfunction)
        if releasedfunction != False:
            button.released.connect(releasedfunction)
        if returnfunction != False:
            button.returnPressed.connect(returnfunction)
        if heldfunction != False:
            self.heldconnect(button,heldfunction,at=3000)



        



        
      
