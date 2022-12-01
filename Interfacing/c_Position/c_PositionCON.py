"""
NAME: c_PositionCON.py
AUTHOR: John Archibald Page
DATE CREATED: 28/11/2022 
DATE LAST UPDATED: 28/11/2022

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
set 0,0: cliccked = current position becomes zero, have a double check on this

To connect the buttons they all need reference options. this can be done by taking th egroup from PRISMS GUI and calling
the child. 

This needs double checking, as outcoming child widgets have been guessed to be correct ********
"""
from PyQt5 import QtWidgets
from c_PositionFUNC import PositionFUNC_class
from PRISMS_II_GUI.SelfDefinedWidgets.PushButton_HoldDownButton import HoldDownButton_class
from Interfacing.ConnectFunctions import ConnectFunctions_class as cf

class PositionCON_class():
    """connect the position buttons for position"""
    def __init__(self,GUI):
        super(PositionCON_class,self).__init__()
        #connect the buttons
        self.connectlineedit(GUI)
        self.connectmovementbuttons(GUI)
        self.connectsetzero(GUI)

    #connect buttons functionality
    def connectlineedit(self,GUI):
        """Connect funcitonality to the lineedit boxes"""
        textboxlist = cf.Textboxrefences(GUI)
        dir = ["alt","azi"]
        for i in range(len(dir)):
            cf.buttonconnect(textboxlist[i+1],returnfunction=lambda: self.entermove(textboxlist[i+1],dir[i]))

    def connectmovementbuttons(self,GUI):
        """Connect movement buttons"""
        buttonlist = cf.pushbuttonsrefences(GUI)
        lineedit = cf.Textboxrefences(GUI)
        dir = ["u","l","r","d"]
        for i in range(len(dir)):
            cf.buttonconnect(buttonlist[i],clickedfunction=lambda: self.clickedmove(lineedit[0],dir[i]),heldfunction=lambda: self.clickedmove(lineedit[0],dir[i]))

    def connectsetzero(self,GUI):
        """Connect the set zero button""" 
        buttonlist = cf.pushbuttonsrefences(GUI)
        cf.buttonconnect(buttonlist[-1],clickedfunction=PositionFUNC_class.setzero)

    #functionality related to textinputs 
    def clickedmove(self,lineedit,dir):
        """Movement when given button is clicked"""
        amount = lineedit.text() #read in the input value for moving
        PositionFUNC_class.moverelative(self,dir,amount)

    def entermove(self,lineedit,dir):
        """When number is typed into the position of altitude or azimuth and enter is clicked, moves ot absolute poisition"""
        abspos = lineedit.text() # read in position value
        PositionFUNC_class.moveabsolute(dir,abspos)




        



        
      
