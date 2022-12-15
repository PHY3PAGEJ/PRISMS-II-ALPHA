"""
NAME: FocusCON.py
AUTHOR: John Archibald Page
DATE CREATED: 09/12/2022 
DATE LAST UPDATED: 09/12/2022

PURPOSE:
To write functionality to the focuser, connecting the buttons
         __Focus________________________ 
        |		                |Auto | |   
        | ______  _____  ______  _____  |            
        ||__Nr__||_____||__Fr__||_____| |
        |_______________________________|
Nr:move the filter to the printed number, update the camera label
Fr: enter moves the filter to this one, update the label for the camera

"""
import logging as log ##troubleshooting
log.info(__file__)  ##troubleshooting
from Interfacing.MoonliteFocuser.MoonliteFocuser import Moonlite_class
from Interfacing.ConnectSerial import ConnectSerial_class
from ConnectingWidgets.ConnectFunctions import ConnectFunctions_class 

class FocusCON_class():
    """Build the functionality for the Filter controls"""
    def __init__(self,GUI):
        super(FocusCON_class,self).__init__()
        #initalise class, this also connects the device
        self.cf = ConnectFunctions_class()
        self.func = Moonlite_class()
        self.cs = ConnectSerial_class()
        #initalise connection
        self.driver = self.cs.connectSerial("Fo",115200) # connect the filter wheel via serial
        #connect buttons
        self.connectdisplaylineedit(GUI)
        self.connectmovementbuttons(GUI)

    #connect buttons functionality
    def connectdisplaylineedit(self,GUI):
        """Connect funcitonality to the lineedit boxes"""
        textboxlist = self.cf.Textboxrefences(GUI)
        self.updatePositionDisplay(GUI)
        self.cf.buttonconnect(textboxlist[1],returnfunction=lambda: self.entermove(GUI)) # enter

    def connectmovementbuttons(self,GUI):
        """Connect movement buttons"""
        buttonlist = self.cf.pushbuttonsrefences(GUI) #movement buttons
        self.cf.buttonconnect(buttonlist[0],clickedfunction=lambda: self.clickedmove("Nr",GUI))
        self.cf.buttonconnect(buttonlist[1],clickedfunction=lambda: self.clickedmove("Fr",GUI))
    
    #functionality related to textinputs 
    def clickedmove(self,dir,GUI):
        """Movement when given button is clicked"""
        textboxlist = self.cf.Textboxrefences(GUI)
        relmov = textboxlist[0].text() # read in position value
        self.func.moverelative(dir, relmov, self.driver)
        self.updatePositionDisplay(self.driver,GUI) # update the position

    def entermove(self,GUI):
        """When number is typed into the position of altitude or azimuth and enter is clicked, moves ot absolute poisition"""
        textboxlist = self.cf.Textboxrefences(GUI)
        abspos = textboxlist[1].text() # read in position value
        self.func.moveabsolute(abspos, self.driver)
        self.updatePositionDisplay(self.driver,GUI) # update the position

    def updatePositionDisplay(self,GUI):
        """Updates the display for the position"""
        textboxlist = self.cf.Textboxrefences(GUI)
        pos = self.func.position(self.driver) # altpos,azipos
        textboxlist[1].setText("{:.2f}".format(pos)) # set the current position to 2 decimal places



    
        