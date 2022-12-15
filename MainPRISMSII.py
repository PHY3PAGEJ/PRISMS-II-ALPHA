'''
NAME: MainPRISMSII.py
AUTHOR: John Archibald Page
DATE CREATED: 10/10/2022 
DATE LAST UPDATED: 13/12/2022

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
    import sys
    #self made modules
    from LaunchWindow.LaunchCON import LaunchCON_class
    import InitiateLogging as il
    
except:

    from PyQt5.QtWidgets import QApplication , QMessageBox

    msgapp = QApplication(sys.argv)
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Error during module import!")
    msg.setInformativeText('Program will close after pressing "OK" ')
    msg.setWindowTitle("Error")
    msg.exec_()

    print("Modules could not be installed correctly, halting code...")
    halt = True  

class PRISMSII():
    def __init__(self):
        #make inital launch window
        self.lc = LaunchCON_class()
        #show launch, will lead to main when coms confirmed
        self.lc.Launch.show()
 
if __name__ == "__main__":
    Application = QtWidgets.QApplication(sys.argv)
    Window = PRISMSII()
    Application.setStyleSheet(open('PRISMSIIStyle.css').read())
    Application.exec_()
    
