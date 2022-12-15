"""
NAME: InitiateLogging.py
AUTHOR: John Archibald Page
DATE CREATED: 29/11/2022 
DATE LAST UPDATED: 30/11/2022

PURPOSE:
To initiate the logging file that logs will be saved to. a new log will be created each day

UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up
"""
import logging as log
import datetime
import math

#initalise program information---------------------------------
programname= "PRISMS II"
logo = [" ___  ___  ____ ___  _   _  ___    ____ ____",
        "|[_]||[_]|  || ||^||||\V/||||^||    ||   || ",
        "||'' ||^\\\  ||  \\\  || V || \\\      ||   || ",
        "||   ||  \\\_||_||_||||   ||||_||   _||_ _||_"]
        
author = "John Archibald Page"
creationdate = "30/11/2022"
updatedate =  "13/12/2022"
purpose = """To operate the PRISMS II system using an intuative user interface."""
#initialise file name and path
logpath = "OutputFiles/Logs/"
logFile = "PRISMSII{}.log".format(datetime.datetime.now().date())
#----------------------------------------------------------------
#initalise log file
logfp = logpath + logFile
log.basicConfig(filename = logfp,level = log.NOTSET,filemode = 'a',format = '%(asctime)s: %(message)s',datefmt = '%m/%d/%Y %H:%M:%S' )

#welcome message formatting
logo = logo
im2 = "Author: " + author
im3 = "Created on: " + creationdate
im4 = "Last updated on: " + updatedate
is1 = "_"
is2 = "|"
is3 = " "
is4 = "-"

#calculations for the start message
messages = [len(im2),len(im3),len(im4),len(logo[0])]
width = max(messages)+1 # width of inital message

##start printing the initial message
log.info(is1*(width+2))
log.info(is2+width*is3+is2)
for i in range(len(logo)):
    log.info(is2+is3*math.floor((width - len(logo[0]))/2)+logo[i]+is3*math.floor((width - len(logo[0]))/2)+is3*(math.ceil((width - len(logo[0]))/2)-math.floor((width - len(logo[0]))/2))+is2)
log.info(is2+width*is3+is2)
log.info(is2+im2+is3*(width - len(im2))+is2)
log.info(is2+im3+is3*(width - len(im3))+is2)
log.info(is2+im4+is3*(width - len(im4))+is2)
log.info(is2+is1*width+is2)
log.info("Initiating program...")

