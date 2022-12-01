File: MainWindow
Author: John Archibald Page
Date Created:18/11/2022
Date Last Updated: 01/12/2022
____________________________________________________________________________________________
PURPOSE:
This file puts the groupings of the main GUI together into one, as shown in "layout.jpg", shown below:

 	 _______________________________
        |_______________________________|  a_Camera
        | a             ||b            ||  b_Terminal
        |               ||_____________||  c_Position  
        |               || c  ||  d    ||  d_Filter
        |               ||    ||_______||  e_CameraSettings
        |               ||____||  f    ||  f_AdvancedOptions
        |               || e  ||_______||
        |               ||____|| STOP  ||
        '''''''''''''''''''''''''''''''''

UPDATE HISTORY:

______________________________________________
FOLDER FILE DIRECTORY:

PRISMS II ALPHA
|___|GUI
|___|___|MainWindow
|___|___|___|PRISMSIIGUI.py
|___|___|___|a_CameraGUI.py
|___|___|___|b_TerminalGUI.py
|___|___|___|c_PositionGUI.py
|___|___|___|d_FilterGUI.py
|___|___|___|e_CameraSettingsGUI.py
|___|___|___|f_AOGUI.py
______________________________________________________________
FOLDER FILE FUNCTIONALITY:
PRISMSIIGUI.py
	Launches all the components of the main window and builds them into a layout.
a_CameraGUI.py
	camera interface
b_TerminalGUI.py
	terminal to input commands
c_PositionGUI.py
	Orientation grouping
d_FilterGUI.py
	Filter grouping
e_CameraSettingsGUI.py
	Camera Settings grouping, containing Exposure and Focus
f_AOGUI.py
	Advanced Options Grouping
______________________________________________________________
FOLDER FILES FLOW DIAGRAM:
		                               
MAINPRISMSII.py <----------------------------------|_a_CameraGUI.py									
	↑                   			   |_b_TerminalGUI.py <--- GUI.SelfDefinedWidgets.TextEdit_Auto_verticle_Expansion.py		  						  				
        |_____GUI.SelfDefinedWidgets.MainWindow.py |_c_PositionGUI.py
			   			   |_d_FilterGUI.py
			    			   |_e_CameraSettingsGUI.py
			   			   |_f_AOGUI.py
______________________________________________________________
FOLDER FILE FUNCTIONALITY:
--------------
a_CameraGUI.py
--------------

GUI, with funcitoning 'save image' and 'set dark' buttons, using GUI.SelfDefinedWidgets.PushButton_saveopendir.py

 __Camera_______________________
|SAVE_IMAGE|______Label_________|
|		                |                   
|                               |  
|  DISPLAY                      |
|                               |          
|_______________________________|
|__Toggles______________________|               
| ___  ___  ___ |Dark Correction|          
||   ||   ||   |||   ||Set Dark||
| ROI  1:1  RGB | Show '''''''' |
|---------------|---------------| 

----------------
b_TerminalGUI.py
----------------

GUI of a terminal

 __Terminal_______________
| _______________________ |                
||>unselectable Terminal ||             
||                       ||             
||                       ||   
||                       ||               
||_______________________||                                
||Input_line______|GO|...||<--- available commands pop-up
|-------------------------|

---------------
c_PositionGUI.py
----------------

GUI of posiiton controls
	
_Orientation______________
|     | u |       Azimuth |
| ___ ===== ___   |______||
|| < ||___|| > |  Altitude|
| --- | d | ---   |______||
|      ---        |0,0 __||
|_________________________|

--------------
d_FilterGUI.py
--------------

GUI of filter controls

 _Filter___________
| | u | <>| | ... ||
|------------------|

----------------------
e_CameraSettingsGUI.py
----------------------

GUI of camera settings controls

__Camera_Settings_________________
| __Focus________________________ |
||		        |Auto |  ||   
|| ______  _____  ______  _____  ||            
|||__Nr__||_____||__Fr__||_____| ||
||_______________________________||
| __Exposure_____________________ |
||		        |Auto |  ||   
|| ______  _____  ______  _____  ||            
|||__Nr__||_____||__Fr__||_____| ||
||_______________________________||
|_________________________________|

----------
f_AOGUI.py
----------

GUI of advanced options controls, with functionality of GUI.SelfDefinedWidgets.PushButton_AdvancedOptions.py

 _Advance_Options_
|   |Mosaic |     |
|    =======      |
|   |Set-Up |     |
|    =======      |
|   |Config.|     |
|_________________|

These buttons lead to the following pop-ups:

Mosaic:
________________________
|@|Mosaic______________|X|             
|Pop up title&message    |  ------> Further action/ additional window                          
|________________________|                 
|Back|      |Open|Create |
-------------------------

Set-Up:
________________________
|@|Set-Up_____________|X|             
|Pop up title&message   |  ------> Further action/ additional window                          
|_______________________|                 
|Back|        |Open|Save|
-------------------------

Config.:
________________________
|@|Config.____________|X|             
|Pop up title&message   |  ------> Further action/ additional window                          
|_______________________|                 
|Back|   |Open|Create|
-------------------------


_________________________________________________________________________________
FILE DEPENDANTS:

-------------
PRISMSIIGUI.py
-------------
MainPRISMSII.py

--------------
a_CameraGUI.py
-------------- 
GUI.MainWindow.MainPRISMSII.py

----------------
b_TerminalGUI.py
----------------
GUI.MainWindow.MainPRISMSII.py

---------------
c_PositionGUI.py
----------------

GUI.MainWindow.MainPRISMSII.py

--------------
d_FilterGUI.py
--------------
GUI.MainWindow.MainPRISMSII.py
GUI.MainWindow.a_CameraGUI.py

----------------------
e_CameraSettingsGUI.py
----------------------
GUI.MainWindow.MainPRISMSII.py

----------
f_AOGUI.py
----------
GUI.MainWindow.MainPRISMSII.py

_______________________________________________________________________________
FILE DEPENDANCIES:

-------------
PRISMSIIGUI.py
-------------
from PyQt5 import QtWidgets
import os
import logging as log
GUI.MainWindow.a_CameraGUI.py
GUI.MainWindow.b_TerminalGUI.py
GUI.MainWindow.c_PositionGUI.py
GUI.MainWindow.d_FilterGUI.py
GUI.MainWindow.e_CameraSettingsGUI.py
GUI.MainWindow.f_AOGUI.py
GUI.SelfDefinedWidgets.MainWindow.py


--------------
a_CameraGUI.py
-------------- 
from PyQt5 import QtWidgets, QtGui, QtCore
GUI.SelfDefinedWidgets.PushButton_saveopendir.py
from GUI.MainWindow.d_FilterGUI.py

----------------
b_TerminalGUI.py
----------------
from PyQt5 import QtCore, QtWidgets
GUI.SelfDefinedWidgets.TextEdit_AutoverticleExpansion.py
GUI.SelfDefinedWidgets.PushButton_popupMessage.py

---------------
c_PositionGUI.py
----------------
from PyQt5 import QtWidgets,QtGui

--------------
d_FilterGUI.py
--------------
from PyQt5 import QtWidgets
GUI.SelfDefinedWidgets.PushButton_popupMessage.py

----------------------
e_CameraSettingsGUI.py
----------------------
from PyQt5 import QtWidgets, QtGui

----------
f_AOGUI.py
----------
from PyQt5 import QtWidgets
GUI.SelfDefinedWidgets.PushButton_AdvancedOptions.py
GUI.SelfDefinedWidgets.PushButton_CreateWindows.py
GUI.SelfDefinedWidgets.PushButton_saveopendir.py







