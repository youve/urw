#!/usr/bin/python3

import pyautogui
import time
import sys
import logging
logging.disable()

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

import argparse

parser = argparse.ArgumentParser(description='automate skill grinding in urw')
parser.add_argument('-s', '--skill', metavar='skill', type=str, nargs='?', default="w",
                    help='The single character you use to cast the skill in urw. Default: w')
parser.add_argument('-t', '--times', metavar='times', type=int, help='How many times to cast it. Default: 10', 
                    nargs='?', default='10')
parser.add_argument('-w', '--wait', metavar='seconds', type=int, help='How many seconds to wait between casts. Default: 2', 
                    nargs='?', default='2')
parser.add_argument('-d', '--switchDesktop', metavar='key combo', type=str, nargs='*', default=['ctrl', 'winleft', '5'],
                    help='Keyboard combination to switch to the desktop that has urw open. Default: ctrl winleft 5')

args = parser.parse_args()

logging.debug(f"args: {args}")

def castSkill(skill, times, wait):
    pyautogui.click(200, 200)
    time.sleep(1)
    pyautogui.typewrite(['left', 'right'], 1)
    for i in range(times):
        time.sleep(wait)
        pyautogui.hotkey('alt', skill)

#switch to desktop with urw running and wait a second
for key in args.switchDesktop:
    pyautogui.keyDown(key)
args.switchDesktop.reverse()
for key in args.switchDesktop:
    pyautogui.keyUp(key)
time.sleep(1)

#cast it
castSkill(args.skill, args.times, args.wait)