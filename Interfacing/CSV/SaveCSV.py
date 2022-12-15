'''
NAME: SaveCSV.py
AUTHOR: John Archibald Page
DATE CREATED: 13/12/2022 
DATE LAST UPDATED: 13/12/2022

PURPOSE:
save csv in specific format

UPDATE HISTORY:

When making an update to the code, remember to put a comment in the code what was changed and why
.i.e.
#01/12/2022: updated the message used in the pop up
'''
import logging as log ##troubleshooting
log.info(__file__)  ##troubleshooting
import pandas as pd
import numpy as np

#define the class
class Save_class():
    """Saving the config file"""
    def __init__(self):
        super(Save_class,self).__init__()  

#make the correct format    

    def filesave(self,file,vals,filesavepath):
        """Save mosaic,setup, or config in the correct format"""
        #dictionary of different labels for different files types
        mlabels = ["SetEXP","AziInc","AltInc","Rows","Columns","Name","Location"] # mosaic
        slabels = ["ONETOONE","ROI","RGB","DARKSET","AZIMUTH","ALTITUDE","EXPOSURE","FOCUS","FILTER"] # setup
        clabels = ["MCBAUDRATE","MCEXP","RGBBAUDRATE","SBAUDRATE","SSPEED","FoBAUDRATE","FoSPEED","FiBAUDRATE","FiDEFAULT","FiSPEED"] # config
        dictlabels = {"mosaic":mlabels,"setup":slabels,"config":clabels}
        #make the format
        dfarray = np.c_[dictlabels[file.lower()],vals]
        df = pd.DataFrame(dfarray)
        df.to_csv(filesavepath,index=False, header=False)

    #coms
    def comssave(self,labels,checkbox,spinbox,savepath,filename="COMS_Config.csv"):
        """Save coms in the correct format"""
        COMSsavepath = "{}/{}".format(savepath,filename)
        checkboxval = [x.isChecked() for x in checkbox]
        spinboxval = [x.value() for x in spinbox]
        dfarray = np.c_[labels,checkboxval,spinboxval]
        df = pd.DataFrame(dfarray)
        column_names = ['component','connected','COMS']
        df.to_csv(COMSsavepath,index=False, header=column_names)
      

        
        
