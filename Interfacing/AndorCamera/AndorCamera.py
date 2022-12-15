"""
NAME: AndorCamera.py
AUTHOR: John Archibald Page
DATE CREATED: 07/12/2022 
DATE LAST UPDATED: 07/12/2022

PURPOSE:
To write functionality to the Andor Camera, which is used as the main camera for PRISMS II

PYTHON LIBRARY: andor3
INSTALL VIA COMMANDLINE: pip install andor3
DOCUMENTATION: https://pypi.org/project/andor3/ [Last Accessed 08/12/2022]

"""
import logging as log ##troubleshooting
log.info(__file__)  ##troubleshooting
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import numpy as np
import pyqtgraph as pg
import andor3
import logging as log

class MainCamera_Class(QtWidgets.QWidget):
    """The image data is presented as a ImageItem inside a pyqtgraph plot. """
    # A Qt Signal is needed to bridge the FrameServer native python thread
    # to the Qt event loop thread for safely updating the user interface
    image_acquired = QtCore.pyqtSignal(np.ndarray)
    
    def __init__(self, parent=None):
        super(MainCamera_Class,self).__init__(parent)
        #create inital graph to append to
        self.createGraph()
        
        try:
            # Initialise the camera and start acquiring frames using the FrameServer helper
            log.info("Initialising Andor3 camera...")
            self.cam = andor3.Andor3()
            # Camera Configuration
            self.cam.SensorCooling = True
            self.cam.FanSpeed = "On"
            self.cam.TriggerMode = "Internal"
            self.cam.ExposureTime = 0.001 # initial exposure time
            self.cam.FrameRate = self.cam.max("FrameRate")//2
            log.info(f"Acquiring at {self.cam.FrameRate} fps.")
            self.cam.ElectronicShutteringMode = "Rolling"
            self.cam.SimplePreAmpGainControl = "16-bit (low noise & high well capacity)"
            self.cam.PixelEncoding = "Mono16"
            self.cam.SpuriousNoiseFilter = False
            self.cam.StaticBlemishCorrection = False
            self.cam.MetadataEnable = False
            self.cam.FastAOIFrameRateEnable = True
            self.cam.AOIHeight = self.cam.max("AOIHeight")
            self.cam.VerticallyCentreAOI = True
            self.cam.AOILeft = 1
            self.cam.AOIWidth = self.cam.max("AOIWidth")

            # Create the FrameServer helper and start it serving frames in a background thread
            # It will call the frame_callback method when new image data is available
            log.info("Starting FrameServer...")
            self.fsvr = andor3.FrameServer(self.cam, self.frame_callback, completion_callback=self.acquisition_completed)
            self.fsvr.start(frame_rate_max=60)
        except:
            log.exception("Unable to initialise Andor3 camera :(")

        # Connect the image acquired Signal to a handler
        self.image_acquired.connect(self.update_image)

    def createGraph(self):
            """Creates pyqtgraph to update with the image"""
            #call in 
            # Create the main pyqtgraph GraphicsLayoutWidget and add it to ourself
            self.glw = pg.GraphicsLayoutWidget()
            self.setLayout(QtWidgets.QVBoxLayout())

            # Create the plotting axes in the GraphicsLayoutWidget
            self.plot = self.glw.addPlot()
            self.plot.setLabels(left="Pixel #", bottom="Pixel #")
            
            # Create the image item and add it to the plot
            self.image = pg.ImageItem()
            self.plot.addItem(self.image)

    def frame_callback(self, n, data, timestamp):
        """emits the Qt Signal so that the UI can then be updated within the Qt event loop."""
        self.image_acquired.emit(data)


    def update_image(self, data):
        """Update the plot with new image data."""
        self.image.setImage(data)

    def acquisition_completed(self, frame_count):
        log.info(f"Acquisition completed, {frame_count} frames received.")
    
    def closeEvent(self, event):
        """Handler for window close event."""
        try:
            log.info("Stopping FrameServer...")
            self.fsvr.stop()
            self.cam.close()
            log.info("Camera closed.")
        except:
            log.exception("Error attempting to stop FrameServer.")

    def ROI(self,x0=40,x1=50,y0=40,y1=50):
        """Creates a region of interest rectangle, indicating where on camera stream focus is calculated"""
        ROIframe = QtGui.QPainter()
        ROIframe.setPen(QtGui.QPen(QtCore.Qt.red,  5, QtCore.Qt.SolidLine))
        ROIframe.drawRect(x0, y0, x1, y1)
        return(ROIframe)


if __name__ == "__main__":
    # Initialise the Qt app and run the event loop
    app = QtWidgets.QApplication(sys.argv)
    window = MainCamera_Class()
    window.show()
    sys.exit(app.exec_()) 

        
    

            
