#!/usr/bin/env python

import cv2 as cv
import os
import sys
import numpy
import click
import traceback
import subprocess
from pathlib import Path

@click.command()
@click.argument('directory', nargs=1)
@click.option("--output", "-o",  default="timelapse.mp4", help="file name to use for output video \ndefault='timelapse.mp4'")
@click.option("--ffmpeg", default=False, is_flag=True, help="use ffmpeg")
@click.option("--mencoder", default=False, is_flag=True,  help="use mencoder")
@click.option("--avconv", default=False, is_flag=True,  help="use avconv")
@click.option("--fps", "-f", default=24, help="FPS of timelapse video, \ndefault='24'")
@click.option("--brightness", "-b", default=False, is_flag=True,  help="Calculate average brightness of images [0-255]")
@click.option("-g", default=-1, help="Deletes files with brightness of greater than")
@click.option("-l", default=-1, help="Deletes files with brightness of less than")
@click.option("--verbose", "-v",  default=False, is_flag=True, help="Display more output than necessary")
def main(directory, fps, verbose, brightness, g,  l,  ffmpeg,  mencoder, avconv, output):
    """ 
    P3TT - Python3 Timelapse Toolkit for the Raspberry Pi
       
    Uses sane values for ffmpeg, mencoder or avconv to create a timelapse video
    using all images from the given directory

    Images must be correctly ordered and currently only supports jpg files

    Only run this command on a backup of images as the wrong set of arguments 
    \033[1;31;40mCAN DELETE FILES \033[1;0;40m

    Examples:

    p3tt.py --mencoder -o out.avi -f 45 ~/pictures

    p3tt.py -bl 30 ./
        
    """
    
    # change directory to that given in argument
    os.chdir(directory)
    
    print(os.getcwd())
    
    #cv.imwrite(str(root) + "new/" + str(file), img)
    
    mencoderCMD = ["mencoder",  
                    "mf://" + str(os.getcwd()) + "/*.jpg",  
                    "-mf",  "type=jpg:fps=" + str(fps),
                    "-ovc",  "lavc",  "-lavcopts", 
                    "vcodec=mpeg4:vbitrate=800000",
                    "-o", output, ]
                    
    ffmpegCMD = ["ffmpeg",  "-r",  str(fps), 
                    "-pattern_type", "glob", 
                    "-i", str(os.getcwd()) + "/*.jpg",
                    "-vcodec:v", "mpeg2video", 
                    output]
    
    avconvCMD = ["avconv",   
                    "-r", str(fps),
                    "-pattern_type", "glob", 
                    "-i",  str(os.getcwd()) + "/*.jpg", 
                    "-vcodec",  "libx264",  
                    "-q:v",  "3", 
                    "-vf",  "scale=iw:ih", 
                    output]
    
    pathList = Path(directory).glob('*.jpg')
    
    # no input files specified
    if len(directory) == 0:
        print("No directory specified.\nUse --help for options")
    
    if not brightness and (l or t):
        print("'-g' or '-l' options must be used in conjuction with '-b'")
    elif brightness:
        mean = []
        numFiles = 0
        
        for file in os.listdir(directory):
            if file.endswith(".jpg"):
                img = cv.imread(os.path.join(os.getcwd(), file))
                print("Files found: " + str(numFiles) + "/" + str(len(os.listdir(directory))) + "  Brightness: \033[1;34;40m" + str(numpy.mean(img)) + "\033[1;0;40m", end="\r", flush=True)
                if verbose: print(file + "  " + str(len(img)) + " x " + str(len(img[0])) + "  Brightness: \033[1;34;40m" + str(numpy.mean(img)) + "\033[1;0;40m")
                mean.append(numpy.mean(img))
                numFiles +=1
            #else: print(file + " is not a supported file type")
        if numFiles > 0: print("Total Average Brightness of " + str(numFiles) + " files: \033[1;35;40m" + str(numpy.mean(mean)) + "\033[1;0;40m")
    
        if(g>0 and l>0): print("must use either -g or -l, not both")
        elif(g>0 or l>0):
            if query("This may delete some files, confirm 'yes' or 'no' ") == True:
                for file in os.listdir(directory):
                    if file.endswith(".jpg"):
                        img = cv.imread(os.path.join(os.getcwd(), file))
                        if g > 0 and numpy.mean(img) > g:
                            os.remove(file)
                            print("\033[1;31;40mDELETING " + file + "\033[1;0;40m")
                        if l > 0 and numpy.mean(img) < l:
                            os.remove(file)
                            print("\033[1;31;40mDELETING " + file + "\033[1;0;40m")
                            
    
    
    if mencoder:
        out = subprocess.call(mencoderCMD)#,  stdin=files)
        if out == 0: 
            print( "Output file - \033[1;31;40m" + 
                    os.path.join(os.getcwd(), output) + "\033[1;0;40m")
        
    if avconv:
        out = subprocess.call(avconvCMD)#,  stdin=files)
        if out == 0: 
            print( "Output file - \033[1;31;40m" + 
                    os.path.join(os.getcwd(), output) + "\033[1;0;40m")
        
    if ffmpeg:        
        out = subprocess.call(ffmpegCMD)#,  stdin=files)
        if out == 0: 
            print( "Output file - \033[1;31;40m" + 
                    os.path.join(os.getcwd(), output) + "\033[1;0;40m")
       
       
       
       
def query(question):
    yes = {'yes','y', 'ye'}
    no = {'no','n', ''} # default
    
    choice = input(question).lower()
    if choice in yes:
       return True
    elif choice in no:
       return False
    else:
       print("Exiting...")
       

       
if __name__ == '__main__':
    main()
