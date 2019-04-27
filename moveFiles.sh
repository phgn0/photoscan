#!/bin/bash

if [ $# -ne 1 ]; 
    then echo "Provide the destination dir as parameter."
fi

echo "Watching for files to copy..."
while true
do
	mv /run/user/1000/gvfs/mtp:host=OnePlus_OnePlus_326ba09f/'Internal shared storage'/DCIM/PhotoScan/* $1 > /dev/null 2>&1
	sleep .1
done