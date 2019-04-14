# P3TT - Python3 Timelapse Toolkit for the Raspberry Pi

Uses sane values for ffmpeg, mencoder or avconv to create a timelapse video using all images from the given directory. Images must be correctly ordered and currently only supports jpg files

Can also calculate average brightness of photos and delete if too bright or dark. Only run this command on a backup of images as the wrong set of arguments CAN DELETE FILES

Commands are easy to modify in the .py file.

## Examples

```
# uses mencoder to encode video at 45fps from all photos in pictures folder 
p3tt.py --mencoder -o out.avi -f 45 ~/pictures
```
```
# checks mean brightness of all photos in current directory
# and deletes all those with a value of less than 30
p3tt.py -bl 30 ./
```

### Prerequisites

Uses [Click](https://github.com/pallets/click) to help with help interface, [opencv](https://www.opencv.org) to open images and [Numpy](https://www.numpy.org) analyze them

```
sudo apt-get install python3 python3-numpy python3-pip
sudo pip3 install opencv-python click

```

### Installing

Copy p3tt.py into /usr/local/bin directory and make it executable

```
# git clone https://github.com/niveknosredneh/P3TT.git ~/Downloads/p3tt
# sudo cp ~/Downloads/p3ttp3tt.py /usr/local/bin/p3tt
# sudo chmod a+x /usr/local/bin/p3tt
```

## Authors

* **Kevin Henderson** - *Initial work*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
