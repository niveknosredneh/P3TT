### P3TT - Python3 Timelapse Toolkit
##### IN HEAVY DEVELOPMENT

Usage: test.py [OPTIONS] DIRECTORY

  P3TT - Python3 Timelapse Toolkit for the Raspberry Pi     Uses sane values
  for ffmpeg, mencoder or avconv to create a timelapse video using all
  images from the given directory

  Images must be correctly ordered and currently only supports jpg files

  Only run this command on a backup of images as the wrong set of arguments
  CAN DELETE FILES 

  Examples:

  'p3tt.py --mencoder -o out.avi -f 45 ~/pictures'

  'p3tt.py -bl 30 ./'

Options:
  -o, --output TEXT  file name to use for output video
                     default='timelapse.mp4'
  --ffmpeg           use ffmpeg
  --mencoder         use mencoder
  --avconv           use avconv
  -f, --fps INTEGER  FPS of timelapse video, 
                     default='24'
  -b, --brightness   Calculate average brightness of images [0-255]
  -g INTEGER         Deletes files with brightness of greater than
  -l INTEGER         Deletes files with brightness of less than
  -v, --verbose      Display more output than necessary
  --help             Show this message and exit.
