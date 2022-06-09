from picamera import PiCamera
from os import system
import datetime
from time import sleep

timelapse = 5 #set this to the number of minutes you wish to run your timelapse camera
secondsinterval = 1 #number of seconds delay between each photo taken
fps = 30 #frames per second timelapse video
numphotos = int((timelapse*60)/secondsinterval) #number of photos to take
print("Taking", numphotos, "photos.")

dateraw = datetime.datetime.now()
startnameformat = dateraw.strftime("%d %B %Y at %I:%M%p")
filenameformat = dateraw.strftime("%d-%m-%y-%H%M")
print("Started: " + startnameformat)

camera = PiCamera()
camera.resolution = (1024, 768)
camera.rotation = 270

print("Removing any old pictures from previous timelapse.")
system('rm /home/pi/Pictures/*.jpg') #delete all photos in the Pictures folder before timelapse start
print("Done! Now taking photos...")

for i in range(numphotos):
    camera.capture('/home/pi/Pictures/image{0:06d}.jpg'.format(i))
    sleep(secondsinterval)

print("Now creating timelapse video. Please wait...")

system('ffmpeg -r {} -f image2 -s 1024x768 -nostats -loglevel 0 -pattern_type glob -i "/home/pi/Pictures/*.jpg" -vcodec libx264 -crf 25  -pix_fmt yuv420p /home/pi/Videos/{}.mp4'.format(fps, filenameformat))

print('Timelapse video is complete. Video saved as /home/pi/Videos/{}.mp4'.format(filenameformat))

datenow = datetime.datetime.now()
endnameformat = datenow.strftime("%d %B %Y at %I:%M%p")

print("Finished: " + endnameformat)