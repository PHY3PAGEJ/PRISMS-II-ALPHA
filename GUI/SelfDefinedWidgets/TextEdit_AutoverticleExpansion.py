'''
NAME: TextEdit_Auto_verticle_Expansion.py
AUTHOR: John Archibald Page
DATE CREATED: 11/11/2022 
DATE LAST UPDATED: 11/11/2022

PURPOSE:
Textedit box that automatically expands vertically when expanded.

UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up
'''
import logging as log ##troubleshooting
log.info(__file__)  ##troubleshooting
from PyQt5 import QtWidgets

class GrowingTextEdit(QtWidgets.QTextEdit):
    """To have an automatic growing verticle textedit box"""

    def __init__(self, *args, **kwargs):
        super(GrowingTextEdit, self).__init__(*args, **kwargs)  
        self.document().contentsChanged.connect(self.sizeChange)

        self.heightMin = 0
        self.heightMax = 65000

    def sizeChange(self):
        docHeight = self.document().size().height()
        if self.heightMin <= docHeight <= self.heightMax:
            self.setMinimumHeight(docHeight)