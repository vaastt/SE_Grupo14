#!/bin/python3
# coding=utf-8
import FCMManager as fcm
import subprocess
import serial
import picamera
import time
import datetime
from time import strftime,localtime

## default vars
pic_dir = '/home/pi/fotos/'

#evan: "cZO8o2tVQb2zKC-s6SkA-7:APA91bFESs1bKXS83W0knZITfq82gDNENk23LOJLF0PXhsdnknTBZHhJzUVYbjyOrtKd18eY96Wrg24Da2dYsjrB2kepoUb6pqSo4_Qs0VVKcc12mulfc6Obg_GQfKbkkN6iedRr66Li"
tokens = ["cZO8o2tVQb2zKC-s6SkA-7:APA91bFESs1bKXS83W0knZITfq82gDNENk23LOJLF0PXhsdnknTBZHhJzUVYbjyOrtKd18eY96Wrg24Da2dYsjrB2kepoUb6pqSo4_Qs0VVKcc12mulfc6Obg_GQfKbkkN6iedRr66Li",
"dc_vyVWQQ2OcYWDXa7qblV:APA91bHcRzsiRkf3LsmJOc10Za6W5nCooHwCCbAYRzW7N7aH4VqZ1rItNlqQO2X94S4Lf66LqNX8EmJ8IAvN-3R-xtLrUZJKIqSKQL2IkmVtG8xbY4ZeSGb7e3E_pnwYLHNHZPvMP4u8"]
##

## this function converts varius jpg files into a simple mp4 video. The default framerate is 3 which makes a video of +-1.6 seconds
## it takes path_prefix as parameter and it's for the jpg location. the output is the same path+prefix but in mp4 format
def convertToMp4(path_prefix):
  cmd = ['ffmpeg','-framerate','3','-i', path_prefix+'%d.jpg',path_prefix+'.mp4']
  retcode = subprocess.call(cmd)
  if not retcode == 0:
    raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd)))
  sendFileToAWS(path_prefix+".mp4")


def appendFile(file_path):
  file1 = open(pic_dir+"/files.txt", "a")  # append mode
  file1.write(file_path+".mp4\n")
  file1.close()
  sendFileToAWS(pic_dir+"/files.txt")

## this function sends a file to the root of AWS web server.
def sendFileToAWS(fullpathfile):
  cmd = ["scp","-i","/home/pi/.ssh/awsse",fullpathfile,"ec2-user@34.252.199.165:/home/ec2-user/se/"]
  retcode = subprocess.call(cmd)
  if not retcode == 0:
    raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd)))

## function that handles motion detection using PIR of arduino
def motionDetected():
  sendPushNotif("Ring! Alguém está à sua porta!")
  saveSeveralPictures(strftime("%H%M%S", localtime()),pic_dir+strftime("%d%m%Y", localtime()))
    
## function that handles button of our ring bell.
def buttonDetected():
  sendPushNotif("Ring! Alguém tocou na campaínha!")
  saveSeveralPictures(strftime("%H%M%S", localtime()),pic_dir+strftime("%d%m%Y", localtime()))

## function that takes msg as argument and send the push-up notification via firebase.
def sendPushNotif(msg):
  fcm.sendPush("Camera na Campainha", msg, tokens)

## this function takes prefix (files prefix) and path (path-to-save files) as parameter. It takes 5 photos in sequence at a framerate of 32FPS.
## this will later call a convert to mp4 function in order to process the jpg and make the video reable by the phone application
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
      appendFile(path.split('/')[-1]+prefix)



### MAIN PROGRAM
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
