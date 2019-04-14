# P3TT - Python3 Timelapse Toolkit for the Raspberry Pi

Uses sane values for ffmpeg, mencoder or avconv to create a timelapse video using all images from the given directory. Images must be correctly ordered and currently only supports jpg files

Can also calculate average brightness of photos and delete if too bright or dark. Only run this command on a backup of images as the wrong set of arguments CAN DELETE FILES

Commands are easy to modify in the .py file.
## Examples

'''
p3tt.py --mencoder -o out.avi -f 45 ~/pictures
'''
'''
p3tt.py -bl 30 ./
'''

### Prerequisites

```
sudo apt-get install python3 python3-numpy
```

### Installing

Copy p3tt.py into your bin directory and make it executable

```
git clone https://github.com/niveknosredneh/P3TT.git
```

```
cp p3tt.py /usr/bin
```

End with an example of getting some data out of the system or using it for a little demo


## Authors

* **Kevin Henderson** - *Initial work*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
