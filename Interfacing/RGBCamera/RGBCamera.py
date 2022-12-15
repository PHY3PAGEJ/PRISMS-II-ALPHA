"""
NAME: RGBCamera.py
AUTHOR: John Archibald Page
DATE CREATED: 08/12/2022 
DATE LAST UPDATED: 08/12/2022

PURPOSE:
To write functionality to the RGB Camera, which is used as navigating camera for PRISMS II,
as the main camera may not be clear when it is running to what it is actually looking at.

PYTHON LIBRARY: thorcam
INSTALL VIA COMMANDLINE: pip install thorcam
DOCUMENTATION: https://pypi.org/project/thorcam/ [Last Accessed 08/12/2022]

"""
import logging as log ##troubleshooting
log.info(__file__)  ##troubleshooting
from thorcam.camera import ThorCam
import logging as log

class MyThorCam(ThorCam):
    """Class to run the RGB camera for PRISMS II with output messages"""
    def received_camera_response(self, msg, value):
        """Prinst camera's responses with outgoing messages and images"""
        super(MyThorCam, self).received_camera_response(msg, value)
        if msg == 'image':
            return
        print('Received "{}" with value "{}"'.format(msg, value))
    def got_image(self, image, count, queued_count, t):
        """find out more information about a given image"""
        print('Received image "{}" with time "{}" and counts "{}", "{}"'
              .format(image, t, count, queued_count))

# create camera
cam = MyThorCam()

# start the server etc.
cam.start_cam_process()
'''
# get list of attached cams
cam.refresh_cameras()

# open the camera
cam.open_camera('03756')
#exposure values
cam.exposure_range
#[0.0, 1000000.0]
cam.exposure_ms
#241.948
# update the exposure value
cam.set_setting('exposure_ms', 150)
# now play the camera
cam.play_camera()


# now stop playing
cam.stop_playing_camera()
# close the camera
cam.close_camera()
# close the server and everything
cam.stop_cam_process(join=True)
'''