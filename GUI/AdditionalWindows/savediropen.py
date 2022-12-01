'''
NAME: saveoropen.py
AUTHOR: John Archibald Page
DATE CREATED: 16/11/2022 
DATE LAST UPDATED: 21/11/2022

PURPOSE:
pop up window to save or open a file with type .csv or .tiff in a given directory suggestion.

savopendir_class(savediropen,icon,filepurpose, filepath, filetype)

where 

savediropen can be "open", "save" or "dir"

icon can be a unique icon

filepurpose will be printed as the window title with the type of window
.i.e. "Save " + filepurpose = "Save Config. file"

filepath = where the directory initially opens to

filetype can either be "csv" or "image"

UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up
'''
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog


class savopendir_class(QtWidgets.QFileDialog):
    """A class to either show open a file window or save a file window in a given format, OR set directory"""

    def __init__(self,savediropen,icon,filepurpose, filepath, filetype):
        super(savopendir_class,self).__init__()
        self.setWindowIcon(QtGui.QIcon('GUI/Images/Logo.png'))
        
        #open either a save window, open window, or change directory window depending on variable put into class
        if (savediropen.lower() == "s") or (savediropen.lower() == "save"):
            self.saveFileDialog(filepurpose, filepath, filetype)
        if (savediropen.lower() == "o") or (savediropen.lower() == "open"):
            self.openFileNameDialog(filepurpose, filepath, filetype)
        if (savediropen.lower() == "d") or (savediropen.lower() == "dir"):
            self.changedirDialog(filepurpose, filepath)

    def openFileNameDialog(self, filepurpose, filepath, filetype):
        """Used to open Mosaic, set-up or config files, which are all stored as .txt, which therefore is hardcoded to function"""
        ##set the file type limiter for what can be opened/ what is shown when GUI opened 
        if (filetype.lower() == "t") or (filetype.lower() == "csv"):
            filetype_lim = "CSV Files (*.csv)"
        if (filetype.lower() == "i") or (filetype.lower() == "image"):
            filetype_lim = "Data Files (*.dat);;Image Files (*.TIFF)"

        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,"Open "+filepurpose, filepath,filetype_lim, options=options)
        ##return the filename that is chosen that can then be applied.
        if fileName:
            return(fileName)
    
    def saveFileDialog(self, filepurpose, filepath, filetype):
        """Used to save Mosaic, set-up or config files, which are .txt, 
        or to save images which have a .TIFF component or .dat component"""
        ##set the file type limiter for what can be opened/ what is shown when GUI opened 
        if (filetype.lower() == "t") or (filetype.lower() == "csv"):
            filetype_lim = "CSV Files (*.csv)"
        if (filetype.lower() == "i") or (filetype.lower() == "image"):
            filetype_lim = "Data Files (*.dat);;Image Files (*.TIFF)"

        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self,"Save "+filepurpose, filepath,filetype_lim, options=options)
        if fileName:
            return(fileName)

    def changedirDialog(self, filepurpose, filepath):
        """Set the directory"""
        directory, _ = QFileDialog.getSaveFileName(self,"Change "+filepurpose+" directory", filepath,self.ShowDirsOnly| self.DontResolveSymlinks)
        if directory:
            return(directory)

    