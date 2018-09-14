#!/bin/bash

logfile="/home/sprawl/.config/snes-controller/logs.txt"

echo "-----------------------------------------------------------------------" >> "$logfile"
echo "Mapping Controller. Date $(date)" >> "$logfile"

ls "/dev/input/by-id" >> "$logfile"

echo "Executing python script to find controller event endpoint" >> $logfile
event=$(python /home/sprawl/.config/snes-controller/get_controller_event.py 2>&1)
echo "Event found at $event in /dev/input" >> $logfile

echo "Executing XBOXDRV command mappings" >> $logfile

xboxdrv --evdev /dev/input/$event --evdev-absmap ABS_X=dpad_x,ABS_Y=dpad_y --evdev-keymap BTN_TOP=X,BTN_TRIGGER=B,BTN_THUMB=A,BTN_THUMB2=Y,BTN_BASE=back,BTN_BASE2=start,BTN_TOP2=lb,BTN_PINKIE=rb --mimic-xpad >> $logfile
