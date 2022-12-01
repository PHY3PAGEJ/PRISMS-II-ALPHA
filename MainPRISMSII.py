'''
NAME: MainPRISMSII.py
AUTHOR: John Archibald Page
DATE CREATED: 10/10/2022 
DATE LAST UPDATED: 30/11/2022

PURPOSE:
To run the main window for PRISMS II

UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up
'''
try:
    halt = False

    #standard libraries and modules
    from PyQt5 import QtWidgets
    import logging as log
    #add in module paths
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), "GUI"))
    sys.path.append(os.path.join(os.path.dirname(__file__), "GUI/SelfDefinedWidgets"))
    sys.path.append(os.path.join(os.path.dirname(__file__), "GUI/AdditionalWindows"))
    sys.path.append(os.path.join(os.path.dirname(__file__), "GUI/LaunchWindow"))
    sys.path.append(os.path.join(os.path.dirname(__file__), "GUI/MainWindow"))
    #self made modules
    from GUI.MainWindow.PRISMSIIGUI import PRISMSIIGUI_class
    from GUI.LaunchWindow.LaunchConnect import LaunchConnect_class
    import InitiateLogging as il

except:

    from PyQt5.QtWidgets import QApplication , QMessageBox

    msgapp = QApplication(sys.argv)
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Error during module import :)")
    msg.setInformativeText('Program will close after pressing "OK" ')
    msg.setWindowTitle("Error")
    msg.exec_()

    print("Modules could not be installed correctly, halting code")
    halt = True  

class PRISMSII():
    def __init__(self):
        #build main window
        self.PRISMSII = PRISMSIIGUI_class()
        #make inital launch window
        self.lc = LaunchConnect_class(self.PRISMSII.MainWindow)
        #show launch, will lead to main when coms confirmed
        self.lc.Launch.show()
        
if __name__ == "__main__":
    Application = QtWidgets.QApplication(sys.argv)
    Window = PRISMSII()
    Application.setStyleSheet(open('PRISMSIIStyle.css').read())
    Application.exec_()
    
