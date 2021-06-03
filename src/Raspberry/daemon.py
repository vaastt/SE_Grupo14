#!/bin/python3
import subprocess
import serial
import picamera
import time
import datetime
from time import strftime,localtime
pic_dir = '/home/pi/fotos/'

def convertToMp4(path_prefix):
  cmd = ['ffmpeg','-framerate','3','-i', path_prefix+'%d.jpg',path_prefix+'.mp4']
  retcode = subprocess.call(cmd)
  if not retcode == 0:
    raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd))) 
def motionDetected():
    saveSeveralPictures(strftime("%H%M%S", localtime()),pic_dir+strftime("%d%m%Y", localtime()))
    

def buttonDetected():
    # button detected
    a=0


def sendPushNotif(msg):
    # send notif to firebase
    a=0

def saveCameraPicture(name,path):
    with picamera.PiCamera() as camera:
      rawCapture = PiRGBArray(camera)
      time.sleep(0.2)
      # grab an image from the camera
      camera.capture(rawCapture, format="bgr")
      image = rawCapture.array


def saveSeveralPictures(prefix,path):
    # save several pictures from the camera
    with picamera.PiCamera() as camera:
      camera.resolution = (640, 480)
      camera.framerate = 32
      # capture frames from the camera
      camera.start_preview()
      time.sleep(2)
      camera.capture_sequence([
        path+prefix+str(1)+".jpg",
        path+prefix+str(2)+".jpg",
        path+prefix+str(3)+".jpg",
        path+prefix+str(4)+".jpg",
        path+prefix+str(5)+".jpg"
      ])
      camera.stop_preview()
      convertToMp4(path+prefix)


ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
try:
  ser.open()
except serial.serialutil.SerialException:
  ser.close()
  ser.open()
while True:
    try:
      motion_detected=0
      while 1:
        response = ser.readline()
        if "MOTION" in response:
          print response
          motion_detected=motion_detected+1
          if motion_detected>=3:
            motionDetected()
            motion_detected=0
        elif "BUTTON" in response:
          print response
          buttonDetected()
    except KeyboardInterrupt:
      ser.close()
      time.sleep(1)
