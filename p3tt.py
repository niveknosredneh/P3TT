#!/usr/bin/env python

import cv2 as cv
import os
import sys
import numpy
import click
import traceback
import subprocess

@click.command()
@click.argument('files', nargs=-1)
@click.option("--output", "-o",  default="timelapse.mp4", help="file name to use for output video, default='timelapse.mp4'")
@click.option("--ffmpeg", default=False, is_flag=True, help="use ffmpeg")
@click.option("--mencoder", default=False, is_flag=True,  help="use mencoder")
@click.option("--avconv", default=False, is_flag=True,  help="use avconv")
@click.option("--fps", "-f", default=24, help="FPS of timelapse video, default=")
@click.option("--brightness", "-b", default=False, is_flag=True,  help="Calculate average brightness of images")
@click.option("--verbose", "-v",  default=False, is_flag=True, help="display more output than necessary")
def main(files, fps, verbose, brightness,  ffmpeg,  mencoder, avconv, output):
    """ 
    P3TT - Python3 Timelapse Toolkit
    
    Uses sane values for ffmpeg and mencoder
    
    Example: timelapse.py -vb *.jpg
    
    """
    
   
    #cv.imwrite(str(root) + "new/" + str(file), img)
    
    #ffmpeg -i timelapse_video.avi -filter:v "crop=1080:1090:0:300" out.avi
    
    stills = open("stills.txt",  'w+')
    mencoderCMD = ["mencoder",  "mf://*.jpg",  "-mf",  "type=jpg:fps=" + str(fps), "-o", output, 
                    "-ovc",  "lavc",  "-lavcopts", "vcodec=mpeg4:vbitrate=800000"]
                    
    ffmpegCMD = ["ffmpeg",  "-r",  str(fps), "-pattern_type", "glob", "-i", "*.jpg", "-c:v", "libx264", 
                    "-pix_fmt",  "yuv420p",  output]
    
    avconvCMD = ["avconv"]
    
    path = os.getcwd()
    mean = []
    # no input files specified
    if len(files) == 0:
        print("No files specified.\nUse --help for options")
       
    
    
    # files specified as input
    if brightness:
        
        numFiles = 0
        for file in files:
            if '.jpg' in file:
                img = cv.imread(os.path.join(os.getcwd(), file))
                print("Files found: " + str(numFiles) + "/" + str(len(files)) + "  Brightness: " + str(numpy.mean(img)), end="\r", flush=True)
                if verbose: print(file + "  " + str(len(img)) + " x " + str(len(img[0])) + "  Brightness: " + str(numpy.mean(img)))
                mean.append(numpy.mean(img))
                numFiles +=1
            else: print(file + " is not a supported file type")
        if numFiles > 0: print("Total Average Brightness of " + str(numFiles) + " files: " + str(numpy.mean(mean)))
    
    if mencoder:
        output = subprocess.call(mencoderCMD)
        if output == 0: print( "success" )
        
        
    if ffmpeg:
        """
        ps = subprocess.Popen(('ps', '-A'), stdout=subprocess.PIPE)
        output = subprocess.check_output(('grep', 'process_name'), stdin=ps.stdout)
        ps.wait()
        """
        
        
        output = subprocess.call(ffmpegCMD)
        if output == 0: print( "success" )
       
       
if __name__ == '__main__':
    main()
