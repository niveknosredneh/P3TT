# P3TT - Python3 Timelapse Toolkit

 Usage: test.py [OPTIONS] [FILES]...

  Uses sane values for ffmpeg and mencoder

  > Example: timelapse.py -vb *.jpg

Options:
  -o, --output TEXT  file name to use for output video,
                     default='timelapse.mp4'
  --ffmpeg           use ffmpeg
  --mencoder         use mencoder
  --avconv           use avconv
  -f, --fps INTEGER  FPS of timelapse video, default=
  -b, --brightness   Calculate average brightness of images
  -v, --verbose      display more output than necessary
  --help             Show this message and exit.
