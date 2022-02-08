#!/usr/bin/env python3
from threading import Thread
from urllib.request import urlopen, Request
import os

os.system('setfont Lat15-TerminusBold14')
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, OUTPUT_A, OUTPUT_D
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from ev3dev2.sound import Sound
from time import sleep

key = "PN6k6R_UDkO5P4UMgfiXKAn243odcQn0Ku-U-hmy7JdARZssHrAGUUeAqA5XdhoNqQRpBCipp3Uk2ujp6nbeDwjQ2oEU5lInXkeFitwRJ_AG9g"

fr = LargeMotor(OUTPUT_B)
fl = LargeMotor(OUTPUT_C)

br = LargeMotor(OUTPUT_D)
bl = LargeMotor(OUTPUT_A)


def horn():
    s = Sound()
    s.play_file('/home/robot/sounds/horn.wav')


def move(station):
    print("moving to station {}".format(station))
    Thread(target=horn).start()
    sleep(1.5)
    Thread(target=lambda: fr.on_for_seconds(speed=SpeedDPM(-36000), seconds=3), daemon=True).start()
    Thread(target=lambda: fl.on_for_seconds(speed=SpeedDPM(-36000), seconds=3), daemon=True).start()
    Thread(target=lambda: br.on_for_seconds(speed=SpeedDPM(-36000), seconds=3), daemon=True).start()
    Thread(target=lambda: bl.on_for_seconds(speed=SpeedDPM(-36000), seconds=3), daemon=True).start()


try:
    # MAIN_HOST = 'http://38.242.196.170'
    MAIN_HOST = 'http://38.242.196.170/robotPull'
    first = True
    if not MAIN_HOST.startswith("http"):
        raise RuntimeError("Incorrect and possibly insecure protocol in url")

    req = Request(MAIN_HOST)
    urlopen(req).read().decode()
    while True:

        if not MAIN_HOST.startswith("http"):
            raise RuntimeError("Incorrect and possibly insecure protocol in url")

        httprequest = Request(MAIN_HOST)
        r = urlopen(httprequest).read().decode()
        if first:
            sound = Sound()
            sound.beep()
            first = False
        if r != key:
            print("got a valid response!")
            Thread(target=move, args=r, daemon=True).start()
        else:
            print("got a bad response!")
            # print("Bad!")
        sleep(1)

except Exception as ex:
    print(ex)
    so = Sound()
    for i in range(3):
        so.beep()
        sleep(0.5)
