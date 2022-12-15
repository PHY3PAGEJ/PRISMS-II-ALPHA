"""
Name: MoonliteFocuser.py
Author: John Archibald Page
Date Created: 09/12/2022
Date Last Updated: 13/12/2022

Purpose: 
To control the moonlite focuser via the serial
"""
import logging as log ##troubleshooting
log.info(__file__)  ##troubleshooting
import logging as log

class Moonlite_class():
    """List of serial commands to control the moonlite focuser"""
    
    def __init__(self):
        super(Moonlite_class,self).__init__()

    def moveabsolute(self, pos, driver):
        command = ":SN{}# :FG#".format(hex(-pos))  # this is the command used to move
        driver.write(command)
        self.position(driver)

    def moverelative(self, dir, steps, driver): #######
        if steps == "": # if no value set for steps
            steps = 10
        pos = self.position(self, driver)
        #relative direction
        if dir == "Nr":
            rel = -1
        if dir == "Fr":
            rel = 1
        newpos = pos + steps*rel
        command = ":SN{}# :FG#".format(hex(newpos))  # this is the command used to move
        driver.write(command)
        self.position(driver)

    def emergencySTOP(self, driver):
        command = ":FQ#"
        driver.write(command)
        log.info("Focuser stopped!")

    def position(self, driver):
        command = ":GP#"
        driver.write(command)
        pos = driver.read()
        log.info("Current position {} steps".format(pos))
        return(pos)

    def checkbusy(self,driver):
        command = ":GI#"
        driver.write(command)
        moving = driver.read()
        if moving == "01":
            log.info("Focuser moving!")
        else:
            log.info("Focuser still...")

    def setstepsize(self,driver,size = 1):
        """Sets the step size used by the stepper motor"""
        stepdict  ={1:":SF#" , 0.5:":SH#"}
        command = stepdict[size]
        driver.write(command)
        if size == 1:
            log.info("Focuser step size set to full")
        else:
            log.info("Focuser step size set to half")

    def setspeed(self,speed):
        """set the speed the stepper motor moves, speed options 1-5"""
        speeddict = {1:"02",2:"04",3:"08",4:"10",5:"20"}
        command = ":SD{}#".format(speeddict[speed])
        log.info("Focuser speed set to {}".format(speed))







    

