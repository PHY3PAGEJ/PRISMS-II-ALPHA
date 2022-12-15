
'''
NAME: AdvancedOptions.py
AUTHOR: John Archibald Page
DATE CREATED: 21/11/2022 
DATE LAST UPDATED: 15/12/2022

AdvancedOptions_class -> creates pop up messagebox that directs to further windows .i.e.:
    Main window button (e.g. "Mosaic") -> popup (e.g. "Back, Open, Create") -> further windows
________________________
|@|Title______________|X|             
|Pop up title&message   |  ------> Further action/ additional window                          
|_______________________|                 
|Back|   |Cancel|Confirm|
-------------------------
UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up
>15/12/2022: remove the first button option, hard code as a back button
'''
import logging as log ##troubleshooting
log.info(__file__)  ##troubleshooting
from PyQt5 import QtWidgets, QtCore, QtGui

class AdvancedOptions_class(QtWidgets.QWidget):
    """This is a pop-up class which directs to further windows .i.e.:
    Main window button (e.g. "Mosaic") -> limbopopup (e.g. "Back, Open, Create") -> further windows"""

    def __init__(self,title,messagetitle, message,phbutton2,func2,phbutton3,func3,col=True):
       super(AdvancedOptions_class,self).__init__()
       self.buildpopup(title,messagetitle, message,phbutton2,func2,phbutton3,func3,col)
       self.setWindowIcon(QtGui.QIcon('GUI/Images/Logo.png'))
     
    def buildpopup(self,title,messagetitle, message,phbutton2,func2,phbutton3,func3,col=True):
        """Build the layout of the pop up"""
        #call in widgets to build layout
        label, textbox = self.DefinePopup(title,messagetitle, message)
        button1, button2, button3 = self.Buttons(phbutton2,func2,phbutton3,func3,col) 
        #define layouts
        VLayout = QtWidgets.QVBoxLayout()
        HLayout = QtWidgets.QHBoxLayout()#buttons
        #build button layout
        HLayout.addWidget(button1)
        HLayout.addWidget(button2)
        HLayout.addWidget(button3)
        #build overall layout
        VLayout.addWidget(label)
        VLayout.addWidget(textbox)
        VLayout.addLayout(HLayout)
        #put layout to ,main widget
        self.setLayout(VLayout)
 
    def DefinePopup(self,title,messagetitle, message):
        """Define what the message is and what the icon is, and what the width is in characters of the set style font."""   
        self.setWindowTitle(title) # title of window
        label = QtWidgets.QLabel(messagetitle)
        textbox = QtWidgets.QTextEdit(message)
        textbox.setTextInteractionFlags(QtCore.Qt.NoTextInteraction) 
        return(label, textbox)

    def Buttons(self,phbutton2,func2,phbutton3,func3,col=True):
        """Build the buttons needed for the advanced options. if button already has function then put func# = False"""
        #the back button which closes the current window, in this case the advanced options window
        button1=QtWidgets.QPushButton("Back")
        func1 = lambda: self.hide()
        button1.clicked.connect(func1)
        #two other optional buttons
        button2 = phbutton2
        button3 = phbutton3
        if func2 !=False:
            button2.clicked.connect(func2)
        if func3 !=False:
            button3.clicked.connect(func3)
        if col == True:
            button2.setStyleSheet("background-color: red")
            button3.setStyleSheet("background-color: green")
        return(button1,button2,button3)
            

