#!/usr/bin/env bash

# write sensitive things to the environment so they aren't in the source code
export apikey=0xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx1
export locationkey=2xxxx2
export lon=-0.00
export lat=51.00

while true
do
	sleep 15
	/home/pi/git/piface-cad/clock.py
done
