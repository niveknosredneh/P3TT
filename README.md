### P3TT - Python3 Timelapse Toolkit
##### IN HEAVY DEVELOPMENT

Uses sane values for ffmpeg, mencoder or avconv to create a timelapse video
using all images from the given directory

Images must be correctly ordered and currently only supports jpg files

Can also calculate average brightness of photos and delete if too bright or dark

Only run this command on a backup of images as the wrong set of arguments 
CAN DELETE FILES

Examples:

p3tt.py --mencoder -o out.avi -f 45 ~/pictures

p3tt.py -bl 30 ./


To use, clone project, cp p3tt.py to /usr/bin/ and make executable

Prerequisites: 
> apt-get install python3 python3-numpy


