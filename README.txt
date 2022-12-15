File: PRISMS II ALPHA
Author: John Archibald Page
Date Created:20/11/2022
Date Last Updated: 12/12/2022
____________________________________________________________________________

PURPOSE:
This folder contains all of PRISMS II, which is run in a compartmentalised fashion

UPDATE HISTORY:
_____________________________________________________________________________
FOLDER FILE DIRECTORY:

PRISMS II ALPHA
|___|Calculations
|___|ConnectingWidgets
|___|GUI
|___|InputFiles
|___|Interfacing
|___|LaunchWindow
|___|OutputFiles
|___|InitiateLogging.py
|___|MainPRISMSII.py
|___|PRISMSIIStyle.css

__________________________________________________________________________________________
FOLDER FILE FUNCTIONALITY:
Much of the functionality of the files in the subfolders are already described, 
or have self explanatory names. Therefore, below is a breif dummary, followed by the flow of the 
files into the main running problem

Calculations
	The algoriuthms for calculating the mosaic, auto exposure and auto focusing
ConnectingWidgets
	connecting the interfacing to the GUI buttons
GUI
	The main GUI and basic internal funcitonality such as saving files
InputFiles
	config, coms etc.
Interfacing
	interfacing with the equipment of PRISMS II, such as camera, focuser, filter etc.
LaunchWindow
	This takes in what the COMS is for each GUI and decides what is shown
OutputFiles
	LOGS, images, dat files
InitiateLogging.py
	This is the config for the log files used throughout the programs
MainPRISMSII.py
	this runs the scripts
PRISMSIIStyle.css
	this defines the style of PRISMS II.
_________________________________________________________________________________
PROGRAM FLOW:
	    
   		                            |InputFiles
     OutputFiles                            ↓
         ↑
MainPRISMSII.py <---LaunchWindow <--- |ConnectingWidgets <--- |Calculations
   ↑			   ↑	      ↑			      |Interfacing
   |PRISMSIIStyle.css	   |----------|GUI
   |InitiateLogging.py
