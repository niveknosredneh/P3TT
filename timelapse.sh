#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

# takes picture and updates old
raspistill -n -rot 90 -w 1080 -h 1920 -o $DATE.jpg
