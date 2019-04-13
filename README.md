### P3TT - Python3 Timelapse Toolkit
##### IN HEAVY DEVELOPMENT

Prerequisites: 
>sudo apt-get install python3


Usage: test.py [OPTIONS] DIRECTORY

  P3TT - Python3 Timelapse Toolkit for the Raspberry Pi     Uses sane values
  for ffmpeg, mencoder or avconv to create a timelapse video using all
  images from the given directory

  Images must be correctly ordered and currently only supports jpg files

  Only run this command on a backup of images as the wrong set of arguments
  CAN DELETE FILES 

  Examples:

  p3tt.py --mencoder -o out.avi -f 45 ~/pictures

  p3tt.py -bl 30 ./
