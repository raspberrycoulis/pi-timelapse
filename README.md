# Timelapse photography on Raspberry Pi
This Python script takes a pre-set number of photos over a pre-set time period using the Raspberry Pi Camera Module before converting the images into a video file (`mp4`) that can be played back on most devices. The length of the the timelapse and gap between photographs, as can the rotation can be adjusted in the `timelapse.py` code:

```python
timelapse = 2 # Time, in minutes, that the timelapse will run for. Change this to suit.
secondsinterval = 1 # Time, in seconds, between each photograph taken. Increasing leaves a longer gap between shots.
camera.rotation = 270 # Angle, in degrees, at which the captured images are positioned. Adjust according to how your Raspberry Pi Camera Module is positioned.
```

## Requirements
### `ffmpeg`
* Install with `sudo apt-get install ffmpeg`

### `picamera`
* Install with `sudo pip install picamera`

### `nfs-common` (if mounting NFS share for synchronisation of files)
* Install with `sudo apt-get install nfs-common`

#### Mounting NFS folder
This script assumes there is a folder in your home directory called `synology` which will be where the corresponding folder on a Synology NAS drive will be mounted. If a folder doesn't exist, create one with `mkdir ~/synology`. To mount the NFS share in this folder on your Raspberry Pi, run the following command whilst substituting in the relevant changes for your set-up:

```bash
sudo mount -t nfs -o proto=tcp,port=2049 192.168.1.24:/volume1/video/timelapse /home/pi/synology
```

The above command mounts the NFS share (`/volume1/video/timelapse`) on the Synology NAS drive in the local directory (`/home/pi/synology`) that is on your Raspberry Pi.