"""
NAME: PositionCON.py
AUTHOR: John Archibald Page
DATE CREATED: 28/11/2022 
DATE LAST UPDATED: 06/12/2022

PURPOSE:
To Connect the functionality to the buttons

          _Orientation______________
        |     | u |       Azimuth |
        | ___ ===== ___   |      ||
        || < ||   || > |   '''''' |
        | ''' ===== '''   Altitude|
        |     | d |       |______||
        |      '''        |set0,0||
        |                  '''''' |
        '''''''''''''''''''''''''''
up: click = move k  amount, if no k then move *** amount. held for 3s+: Move at ***/s, held 5s+: move at /2, realesed: Stop
down: click = move k  amount, if no k then move *** amount. held for 3s+: Move at ***/s, held 5s+: move at /2, realesed: Stop
anti-clockwise: click = move k  amount, if no k then move *** amount. held for 3s+: Move at ***/s, held 5s+: move at /2, realesed: Stop
clockwise: click = move k  amount, if no k then move *** amount. held for 3s+: Move at ***/s, held 5s+: move at /2, realesed: Stop
Azimuth: Prints current position. If input position, then move to this posiiton.
Altitude: Prints current position. If input position, then move to this posiiton.
set 0,0: clicked = current position becomes zero, have a double check on this

To connect the buttons they all need reference options. this can be done by taking th egroup from PRISMS GUI and calling
the child. 

UPDATE HISTORY:
>remove the held down functionality to see if that fixes it.
"""
import logging as log ##troubleshooting
log.info(__file__)  ##troubleshooting
from Interfacing.ZaberStand.ZaberStand import ZaberStand_class
from ConnectingWidgets.ConnectFunctions import ConnectFunctions_class

class PositionCON_class():
    """connect the position buttons for position"""
    def __init__(self,GUI):
        super(PositionCON_class,self).__init__()
        #initalise class, this also connects the device
        self.cf = ConnectFunctions_class()
        self.func = ZaberStand_class()
        #connect the buttons
        self.connectdisplaylineedit(GUI)
        self.connectmovementbuttons(GUI)
        self.connectsetzero(GUI)
        
    #connect buttons functionality
    def connectdisplaylineedit(self,GUI):
        """Connect funcitonality to the lineedit boxes"""
        textboxlist = self.cf.Textboxrefences(GUI)
        self.updatePositionDisplay(GUI)
        self.cf.buttonconnect(textboxlist[1],returnfunction=lambda: self.entermove(textboxlist[1],"azi",GUI)) # enter
        self.cf.buttonconnect(textboxlist[2],returnfunction=lambda: self.entermove(textboxlist[2],"alt",GUI)) # enter

    def connectmovementbuttons(self,GUI):
        """Connect movement buttons"""
        buttonlist = self.cf.pushbuttonsrefences(GUI) #movement buttons
        lineedit = self.cf.Textboxrefences(GUI) # central linedit input
        self.cf.buttonconnect(buttonlist[0],clickedfunction=lambda: self.clickedmove(lineedit[0],"u",GUI))
        self.cf.buttonconnect(buttonlist[1],clickedfunction=lambda: self.clickedmove(lineedit[0],"l",GUI))
        self.cf.buttonconnect(buttonlist[2],clickedfunction=lambda: self.clickedmove(lineedit[0],"r",GUI))
        self.cf.buttonconnect(buttonlist[3],clickedfunction=lambda: self.clickedmove(lineedit[0],"d",GUI))

    def connectsetzero(self,GUI):
        """Connect the set zero button""" 
        buttonlist = self.cf.pushbuttonsrefences(GUI) # 0,0 button
        self.cf.buttonconnect(buttonlist[-1],clickedfunction=lambda: self.clickedzero(GUI))

    #functionality related to textinputs 
    def clickedmove(self,lineedit,dir,GUI):
        """Movement when given button is clicked"""
        amount = lineedit.text() #read in the input value for moving
        self.func.moverelative(dir,amount)
        self.updatePositionDisplay(GUI) # update the position

    def entermove(self,lineedit,dir,GUI):
        """When number is typed into the position of altitude or azimuth and enter is clicked, moves ot absolute poisition"""
        abspos = lineedit.text() # read in position value
        self.func.moveabsolute(dir,abspos)
        self.updatePositionDisplay(GUI) # update the position

    def clickedzero(self,GUI):
        """When number is typed into the position of altitude or azimuth and enter is clicked, moves ot absolute poisition"""
        self.func.setzero()
        self.updatePositionDisplay(GUI) # update the position

    def updatePositionDisplay(self,GUI):
        """Updates the display for the position"""
        textboxlist = self.cf.Textboxrefences(GUI)
        azipos,altpos = self.func.currentposition() # altpos,azipos
        textboxlist[1].setText("{:.2f}".format(altpos)) # set the current position to 2 decimal places
        textboxlist[2].setText("{:.2f}".format(azipos)) # set the current position to 2 decimal places




        



        
      
