#!/bin/python
import RPi.GPIO as GPIO

from imgproc import *
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

pic_dir = '/tmp'

GPIO.setmode(GPIO.BOARD);
GPIO.setup(18, GPIO.IN)


def motionDetected():
    # motion detected
    a=0
    

def buttonDetected():
    # button detected
    a=0


def sendPushNotif(msg):
    # send notif to firebase
    a=0

def saveCameraPicture(name,path):
    # asdsa
    camera = PiCamera()
    rawCapture = PiRGBArray(camera)
    time.sleep(0.2)
    # grab an image from the camera
    camera.capture(rawCapture, format="bgr")
    image = rawCapture.array


def saveSeveralPictures(prefix,path):
    # save several pictures from the camera
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(640, 480))
    # capture frames from the camera
    for i in range(1,5):
        camera.catpure(path+prefix+str(i)+".jpg")
        time.sleep(0.5)
