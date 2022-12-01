File: Launch
Author: John Archibald Page
Date Created:20/11/2022
Date Last Updated: 24/11/2022
____________________________________________________________________________

PURPOSE:
This folder creates the Launch file for writting COMS to csv. configuration file.

To set the coms, the toggle and the spin wheel needs to be set and unique from other
connected components. 

|CONFIRM| <- launches a pop up showing what coms have been connected and asking to confirm.
If not all coms connected, this leads to pop up with prompt saying "are you sure?",
but prisms II will still launch with reduced functionality.

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
__________________________________________________________________________________________
FOLDER FILE FUNCTIONALITY:

LaunchConnect.py
	Connects the unique button functionality
LaunchGUI.py
	Class to create GUI and windows
LaunchSavefile.py
	Class for saving the coms file which will be used for connecting serial
LaunchSerial.py
	Class for reading in the serials connected to laptop
_______________________________________________________________________________
FLOW DIAGRAM:

 _________________________________
|_PRISMS_II:Connect_COMS________|X|
| __Available_COMS_______________ |
||		                 ||                    
||_______________________________||            
||_________________________|_..._||<--- Pop -up of full names
| __Main_Camera__________________ |
||  _                 COMS #     ||
|| |_|Connected?     |    |<>|	 ||
||                   ''''''      ||
||_______________________________||
| __Positional_Stand_____________ |
||  _                 COMS #     ||
|| |_|Connected?     |    |<>|	 ||
||                   ''''''      ||
||_______________________________||
| __Filter_______________________ |
||  _                 COMS #     ||
|| |_|Connected?     |    |<>|	 ||
||                   ''''''      ||
||_______________________________||
| __Focuser______________________ |
||  _                 COMS #     ||
|| |_|Connected?     |    |<>|	 ||
||                   ''''''      ||
||_______________________________||
| __RGB_Camera___________________ |
||  _                 COMS #     ||
|| |_|Connected?     |    |<>|	 ||	|All connected correctly ---> AdditionalOptions pop-up stating options, confirm, cancel or go back ---> Launch Main Window
||                   ''''''      ||	|
||_______________________________||	|
| |CANCEL|              |CONFIRM| | --->|Not all connected ---> AdditionalOptions pop-up with warning of reduced functionality to confirm, cancel or go back ---> Launch Main Window
'''''''''''''''''''''''''''''''''''     |  
     |_Closes Program			|
					|Connection incorrect (.i.e. two coms set as same, or not available)---> Message pop-up stating this is not allowed
_________________________________________________________________________________
FILE DEPENDANTS:

----------------
LaunchConnect.py
----------------
MainPRISMSII.py

------------
LaunchGUI.py
------------
GUI.LaunchWindow.LaunchConnect.py

-----------------
LaunchSavefile.py
-----------------
GUI.LaunchWindow.LaunchConnect.py

---------------
LaunchSerial.py
---------------
GUI.LaunchWindow.LaunchConnect.py

_______________________________________________________________________________
FILE DEPENDANCIES:

----------------
LaunchConnect.py
----------------
import pandas as pd
GUI.LaunchWindow.LaunchSerial.py
GUI.LaunchWindow.LaunchSavefile.py
GUI.LaunchWindow.LaunchGUI.py

------------
LaunchGUI.py
------------
from PyQt5 import QtWidgets, QtCore
import logging
GUI.SelfDefinedWidgets.PushButton_popupMessage.py

-----------------
LaunchSavefile.py
-----------------
from PyQt5 import QtWidgets
import pandas
import logging
GUI.AdditionalWindows.AdvancedOptions.py
GUI.AdditionalWindows.popupMessage.py

---------------
LaunchSerial.py
---------------
import serial.tools.list_ports
			






