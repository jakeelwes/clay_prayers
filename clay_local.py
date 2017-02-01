import socket
import os
import subprocess
from subprocess import Popen, PIPE, STDOUT
import time
import cv2

ip = "54.229.182.178";

#empty quote
open('clay1.txt', 'w').close()
# timer triggers webcam to take image
# os.system('fswebcam --no-banner -S 20 claycam.jpg')

camera_port = 0
ramp_frames = 10
camera = cv2.VideoCapture(camera_port)
def get_image():
	retval, im = camera.read()
	return im
for i in xrange(ramp_frames):
	temp = camera.read()

camera_capture = get_image()
face_file_name = "claycam.jpg"
cv2.imwrite(face_file_name, camera_capture)
del(camera)


# send image
s = socket.socket()
host = ip
port = 12345
s.connect((host, port))
time.sleep (2)
f=open ("claycam.jpg", "rb")
l = f.read(4096)
while (l):
	s.send(l)
	l = f.read(4096)
time.sleep(3)
print "image sent"
s.close()                # Close the connection

	# wait for densecap & torch-rnn to write quote
print "done"
time.sleep(6)
s = socket.socket()
host = ip
port = 12345

s.connect((host, port))
l = s.recv(1024)
print str(l)
clay = open("clay1.txt", "w")
clay.write(l)
clay.close()
s.send("file received")
s.close()
