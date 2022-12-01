File: GUI
Author: John Archibald Page
Date Created:20/11/2022
Date Last Updated: 01/12/2022
____________________________________________________________________________

PURPOSE:
This folder is used to create PRISMS GUI functionality, as well as backgorund funcitonality
not requiring the connection of equipment, for example making config csv or saving a csv

UPDATE HISTORY:
_____________________________________________________________________________
FOLDER FILE DIRECTORY:

PRISMS II ALPHA
|___|GUI
|___|___|Launch
|___|___|___|LaunchConnect.py
|___|___|___|LaunchGUI.py
|___|___|___|LaunchSavefile.py
|___|___|___|LaunchSerial.py
|__|__|AdditionalWindows
|__|__|__|AdvancedOptions.py
|__|__|__|AdvancedOptions_ConfigCreate.py
|__|__|__|AdvancedOptions_MosaicCreate.py
|__|__|__|popupMessage.py
|__|__|__|savediropen.py
|__|__|Images
|__|__|__|PlaceHolder.png
|__|__|__|Logo.png
|___|___|MainWindow
|___|___|___|PRISMSIIGUI.py
|___|___|___|a_CameraGUI.py
|___|___|___|b_TerminalGUI.py
|___|___|___|c_PositionGUI.py
|___|___|___|d_FilterGUI.py
|___|___|___|e_CameraSettingsGUI.py
|___|___|___|f_AOGUI.py
|___|___|SaveReadFunction
|___|___|___|SaveReadCSV.py
|__|__|SelfDefinedWidgets
|__|__|__|PushButton_AdvancedOptions.py
|__|__|__|PushButton_CreateWindows.py
|__|__|__|PushButton_HoldDownButton.py
|__|__|__|PushButton_popupMessage.py
|__|__|__|PushButton_saveopendir.py
|__|__|__|MainWindow.py
|__|__|__|TextEdit_AutoverticleExpansion.py
__________________________________________________________________________________________
FOLDER FILE FUNCTIONALITY:
Much of the functionality of the files in th esubfolders are already described, 
or have self explanatory names. Therefore, below are the explanations of any subfolders
not yet defined:

******
Images
	This folder stores the Icon used for the windows, as well as a placeholder
	used for when images are not connected.
	The Icon is called upon at any point a new window has been made.
SaveReadFunction
	This file is still in progress, but will be used ot read and write to the create files
	used for making mosaic and config files.


