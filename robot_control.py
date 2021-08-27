#This is a simple python script to move a raspberry pi robot using WiFi

import RPi.GPIO as GPIO
import socket
import csv
import time
import os
import re
import subprocess


LeftMotarForward = 29
RightMotarForward = 31
LeftMotarReverse = 33
RightMotarReverse = 35  


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)   
GPIO.setup(LeftMotarForward,GPIO.OUT)
GPIO.setup(RightMotarForward,GPIO.OUT)
GPIO.setup(LeftMotarReverse,GPIO.OUT)
GPIO.setup(RightMotarReverse,GPIO.OUT)

#Setting up UDP ip address and port 
UDP_IP = "192.168.43.213"
UDP_PORT = 5000

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT))


while True:
 data, addr = sock.recvfrom(1024)
 raw=data

 if raw=="forward":
     
    GPIO.output(LeftMotarForward,True)
    GPIO.output(RightMotarForward,True)
    GPIO.output(LeftMotarReverse,False)
    GPIO.output(RightMotarReverse,False)
    print "Robot Moving Forward"
  
  
 elif raw=="stop":
    GPIO.output(LeftMotarForward,False)
    GPIO.output(RightMotarForward,False)
    GPIO.output(LeftMotarReverse,False)
    GPIO.output(RightMotarReverse,False)
    print "Robot Stoped"
    

 elif raw=="backward":
    GPIO.output(LeftMotarForward,False)
    GPIO.output(RightMotarForward,False)
    GPIO.output(LeftMotarReverse,True)
    GPIO.output(RightMotarReverse,True)
    print "Robot Moving Backward"

 elif raw=="right":
    GPIO.output(LeftMotarForward,True)
    GPIO.output(RightMotarForward,False)
    GPIO.output(LeftMotarReverse,False)
    GPIO.output(RightMotarReverse,False)
    print "Robot Moving Right"

 elif raw=="left":
    GPIO.output(LeftMotarForward,False)
    GPIO.output(RightMotarForward,True)
    GPIO.output(LeftMotarReverse,False)
    GPIO.output(RightMotarReverse,False)  
    print "Robot Moving Left"

 else:
    print "invalid input"  
    


GPIO.cleanup()
