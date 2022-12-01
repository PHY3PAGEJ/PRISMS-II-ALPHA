FOLDER: AdditionalWindows
AUTHOR: John Archibald Page
DATE CREATED:18/11/2022
LAST UPDATED: 01/12/2022
_____________________________________________________________________________

PURPOSE:
This file contains classes used to create pop up windows with additional options or messages.

UPDATE HISTORY:

_____________________________________________________________________________
FOLDER FILE DIRECTORY:
PRISMS II ALPHA
|__|GUI
|__|__|AdditionalWindows
|__|__|__|AdvancedOptions.py
|__|__|__|AdvancedOptions_ConfigCreate.py
|__|__|__|AdvancedOptions_MosaicCreate.py
|__|__|__|popupMessage.py
|__|__|__|savediropen.py
______________________________________________________________________________
FOLDER FILE FUNCTIONALITY:
AdvancedOptions.py
	Window with 3 option buttons and a message. the functionality of buttons is defined when class is called.
AdvancedOptions_ConfigCreate.py
	Pop-up from create button that allows editting and creation of unique config file from the default that can be applied.
AdvancedOptions_MosaicCreate.py
	Pop-up from create button that allows editting and creation of unique mosaic file that can be ran.
popupMessage.py
	Creates a pop up message with more information.
savediropen.py
	Creates a pop up to save a file in a given location under a given name with given name.

_______________________________________________________________________________
FOLDER FILE WINDOW LAYOUTS:
------------------
AdvancedOptions.py
------------------
Define a button that will launch the pop up with the following class:
>PRISMS II ALPHA/GUI/SelfDefinedWidgets/
PushButton_AdvancedOptions.AOPushButton(label,title,messagetitle, message,button1,func1,button2,func2,button3,func3,col=True)

Click button:
|label|
--->
Launches pop-up:
_______________________________
|@|Title_____________________|X|             
|Pop up title&message          |                          
|______________________________|                 
|button1|      |Button2|button3|
-------------------------------

Where buttons# have functionality func#

-------------------------------
AdvancedOptions_ConfigCreate.py
-------------------------------
setting the class to a button:
ConfigCreate_class()

means the button will launch the following window:
 _________________________________________________
|@|Create Config                                |X| 
|-------------------------------------------------|            
| _Equipment____________________  _____________   |              
|| |Main Camera|      |Focuser| ||  Switch     |  |
|| |Positional Stand| |Filter|  ||    in       |  |
||        |RGB Camera|          ||     widget  |  |
||______________________________||             |  | 
| _Interface____________________ |             |  |  
||                              ||             |  |
|||save paths|  |Coms|          ||             |  |
||______________________________||_____________|  | 
|-------------------------------------------------|                
|Back|                                |SAVE|APPLY||
--------------------------------------------------

When clicking one of the buttons on the left means that the interface
on the right will switch out to give th eoption to edit the vairable inputs
which can then be applied to prisms or saved for another time.

-------------------------------
AdvancedOptions_MosaicCreate.py
------------------------------- 

setting the class to a button:
MosaicCreate_class()

means the button will launch the following window:
________________________________
|@|Create Mosaic              |X| 
|-------------------------------|            
|_Exposure_time________________ |  
||filter: 1 2 3 4 5 6 7 8 9 10 ||  
||Set-exp| | | | | | | | | |  |||
|------------------------------||
|_Positional_increments_________|  
||Azimuth: |    |              ||  
||Altitude:|    |              ||
|------------------------------||
|_Cubes________________________ |  
||rows    Columns        Cubes ||  
|||   | X  |     |   =   |    |||
|------------------------------||
|_File_Name_&_Save_Location____ |  
||file name:     |         |   ||  
||Save location: |         |   ||
|------------------------------||                
|Back|                |SAVE|RUN||
--------------------------------

typing in the values to the line edit options and clicking save saves
as a .csv file, but clicking run launches the mosaic functionality with 
the current open mosaic file.

---------------
popupMessage.py 
---------------
Define a button that will launch the pop up with the following class:
>PRISMS II ALPHA/GUI/SelfDefinedWidgets/
PushButton_popupMessage.moreinfoPushButton(messagefile)

Where message file has the following format:

title, Terminal: Serial Port Full Names
messagetitle, Serial Port Full Name
message,No Ports Available...
windowicon,False
width,300

Where the window icon can be set to something unique

Click button:
|...|
--->
Launches pop-up:
________________________
|@|Title______________|X| 
|messagetitle           |             
|message                |                 
|_______________________|                
|____________________|OK|
<--------width---------->

--------------
savediropen.py
--------------
Launches a normal directory pop up to save a file

savopendir_class(savediropen,icon,filepurpose, filepath, filetype)

where 

savediropen can be "open", "save" or "dir"

icon can be a unique icon

filepurpose will be printed as the window title with the type of window
.i.e. "Save " + filepurpose = "Save Config. file"

filepath = where the directory initially opens to

filetype can either be "csv" or "image"
_________________________________________________________________________________
FILE DEPENDANTS:
------------------------------------
AdvancedOptions.py
------------------------------------
GUI.LaunchWindow.LaunchSavefile.py
	
-------------------------------------------
AdvancedOptions_ConfigCreate.py
-------------------------------------------
GUI.SelfDefinedWidgets.PushButton_CreateWindows.py

-------------------------------------------
AdvancedOptions_MosaicCreate.py
-------------------------------------------
GUI.SelfDefinedWidgets.PushButton_CreateWindows.py

---------------------------------
popupMessage.py 
--------------------------------- 
GUI.SelfDefinedWidgets.PushButton_popupMessage.py
GUI.LaunchWindow.LaunchSavefile.py

--------------------------------
savediropen.py
--------------------------------
GUI.SelfDefinedWidgets.PushButton_saveopendir.py 
_______________________________________________________________________________
FILE DEPENDANCIES:
------------------------------------
AdvancedOptions.py
------------------------------------
from PyQt5 import QtWidgets, QtCore
	
-------------------------------------------
AdvancedOptions_ConfigCreate.py
-------------------------------------------
from PyQt5 import QtWidgets
GUI.SelfDefinedWidgets.PushButton_saveopendir.py

-------------------------------------------
AdvancedOptions_MosaicCreate.py
-------------------------------------------
from PyQt5 import QtWidgets
GUI.SelfDefinedWidgets.PushButton_saveopendir.py

---------------------------------
popupMessage.py 
--------------------------------- 
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

--------------------------------
savediropen.py
--------------------------------
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QIcon




