#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import subprocess
import sys

MORSE_CODE={
    'a':'`-',       'n':'-`',
    'b':'-```',     'o':'---',
    'c':'-`-`',     'p':'`--`',
    'd':'-``',      'q':'--`-',
    'e':'`',        'r':'`-`',
    'f':'``-`',     's':'```',
    'g':'--`',      't':'-',
    'h':'````',     'u':'``-',
    'i':'``',       'v':'```-',
    'j':'`---',     'w':'`--',
    'k':'-`-',      'x':'-``-',
    'l':'`-``',     'y':'-`--',
    'm':'--',       'z':'--``',
    '1':'`----',    '6':'-````',
    '2':'``---',    '7':'--```',
    '3':'```--',    '8':'---``',
    '4':'````-',    '9':'----`',
    '5':'`````',    '0':'-----',
}

def LED_on():
    """on led"""
    led_cmd = "echo 1 > /dev/myled0"
    subprocess.call(led_cmd, shell=True)

def LED_off():
    """off led"""
    led_cmd = "echo 0 > /dev/myled0"
    subprocess.call(led_cmd, shell=True)

def wait(self):
    """wiat time"""
    time.sleep(self)

def short_mark():
    LED_on()
    wait(0.2)
    LED_off()
    wait(0.2)

def longer_mark():
    LED_on()
    wait(0.6)
    LED_off()
    wait(0.2)

def create_morse(self):
    for char in self:
        if char.isalpha():
            char=char.lower()
        if char == '\n':
            print '\n'
            break
        elif char == ' ':
            print ' '
            wait(0.6)
        else:
            morse=MORSE_CODE.get(char)
            print morse
            for mark in morse:
                if mark == '`':
                    short_mark()
                elif mark == '-':
                    longer_mark()   

def main():
	while True:
		create_morse( raw_input("Enter messages to be converted to Morse code:") )
		print "Complete!!!\n"
		
if __name__ == "__main__":
	main()
