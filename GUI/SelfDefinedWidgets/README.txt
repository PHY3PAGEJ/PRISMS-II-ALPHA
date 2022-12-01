FOLDER: SelfDefinedWidgets
AUTHOR: John Archibald Page
DATE CREATED:18/11/2022
LAST UPDATED: 01/12/2022
_____________________________________________________________________________

PURPOSE:
This folder contains self defined widgets to be used in PRISMS II interface.

UPDATE HISTORY:

_____________________________________________________________________________
FOLDER FILE DIRECTORY:
PRISMS II ALPHA
|__|GUI
|__|__|SelfDefinedWidgets
|__|__|__|PushButton_AdvancedOptions.py
|__|__|__|PushButton_CreateWindows.py
|__|__|__|PushButton_HoldDownButton.py
|__|__|__|PushButton_popupMessage.py
|__|__|__|PushButton_saveopendir.py
|__|__|__|MainWindow.py
|__|__|__|TextEdit_AutoverticleExpansion.py
______________________________________________________________________________
FOLDER FILE FUNCTIONALITY:

PushButton_AdvancedOptions.py
	A push button to launch the pop up GUI.AdditionalWindows.AdvancedOptions.py
PushButton_CreateWindows.py
	A push button to launch the pop up GUI.AdditionalWindows.AdvancedOptions_CreateMosaic.py or GUI.AdditionalWindows.AdvancedOptions_CreateConfig.py
PushButton_HoldDownButton.py
	A push button with functionality to launch a function after it has been held for a defined amount of time.
PushButton_popupMessage.py
	A push button to launch the pop up GUI.AdditionalWindows.popupMessage.py
PushButton_saveopendir.py
	A push button to launch the pop up GUI.AdditionalWindows.saveopendir.py with inputs to define being save, open or directory setter
MainWindow.py
	A main window pop up that can have compoents appended to it as it scales depending on screen hardware.
TextEdit_AutoverticleExpansion.py
	A vertical exapnding text box that can be used as a terminal.
_______________________________________________________________________________

FILE DEPENDANTS:
-----------------------------
PushButton_AdvancedOptions.py
-----------------------------
GUI.MainWindow.f_AOGUI.py

---------------------------
PushButton_CreateWindows.py
---------------------------
GUI.MainWindow.f_AOGUI.py

----------------------------
PushButton_HoldDownButton.py
----------------------------
################################
--------------------------
PushButton_popupMessage.py
--------------------------
GUI.LaunchWindow.LaunchGUI.py
GUI.MainWindow.b_TerminalGUI.py
GUI.MainWindow.d_FilterGUI.py

-------------------------
PushButton_saveopendir.py
-------------------------
GUI.AdditionalWindows.AdvancedOptions_ConfigCreate.py
GUI.AdditionalWindows.AdvancedOptions_MosaicCreate.py
GUI.MainWindow.a_CameraGUI.py
GUI.MainWindow.f_AOGUI.py

-------------
MainWindow.py
-------------
GUI.MainWindow.PRISMSIIGUI.py
---------------------------------
TextEdit_AutoverticleExpansion.py 
---------------------------------
GUI.MainWindow.b_TerminalGUI.py

_______________________________________________________________________________
FILE DEPENDANCIES:
-----------------------------
PushButton_AdvancedOptions.py
-----------------------------
from PyQt5 import QtWidgets
GUI.AdditionalWindows.AdvancedOptions.py

---------------------------
PushButton_CreateWindows.py
---------------------------
from PyQt5 import QtWidgets
GUI.AdditionalWindows.AdvancedOptions_MosaicCreate.py
GUI.AdditionalWindows.AdvancedOptions_ConfigCreate.py
----------------------------
PushButton_HoldDownButton.py
----------------------------
from PyQt5 import QtCore, QtWidgets

--------------------------
PushButton_popupMessage.py
--------------------------
from PyQt5 import QtWidgets
import pandas 
GUI.AdditionalWindows.popupMessage.py

-------------------------
PushButton_saveopendir.py
-------------------------
from PyQt5 import QtWidgets
GUI.AdditionalWindows.savediropen.py

-------------
MainWindow.py
-------------
from PyQt5 import QtGui, QtWidgets
import screeninfo
import re

---------------------------------
TextEdit_AutoverticleExpansion.py 
---------------------------------
from PyQt5 import QtWidgets
