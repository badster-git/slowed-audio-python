from pydub import AudioSegment
import os
import sys
import time
import json
import argparse

POSSIBLE_FORMATS = {1: '.mp3', 2: '.wav'}

PATH=""
while not os.path.isdir(PATH):
    PATH = os.path.realpath(input('Path to work in: '))
    if not os.path.isdir(PATH):
        print('Invalid path. Try again.')
print("Test folder: " + PATH)

FORMAT=""
while (FORMAT != "1" or FORMAT != "2"):
    FORMAT = input("Select format (1 [default]: mp3 | 2: wav): ") or "1"
    if (FORMAT == "1" or FORMAT == "2"):
        FORMAT = POSSIBLE_FORMATS[int(FORMAT)]
        print(FORMAT.partition('.')[2] + ' selected.')
        break
    else:
        print('Invalid format. Try again.')


INFILE = ""
while not os.path.isfile(os.path.join(PATH, INFILE)):
    INFILE = input('Name of input file: ')
    INFILE = os.path.splitext(INFILE)[0] + FORMAT
    if not os.path.isfile(os.path.join(PATH, INFILE)):
        print(f"{os.path.join(PATH,INFILE)} not found. Try again.")
    else:
        print(f"Input file: {os.path.join(PATH, INFILE)}")

# Remove file extension
INFILE = os.path.splitext(INFILE)[0]

def speed_change(filename, speed=1.0):
    audio = AudioSegment.from_mp3(filename + FORMAT)
    altered_audio = audio._spawn(audio.raw_data, overrides={
        "frame_rate": int(audio.frame_rate * speed)
        })
    OUTFILE = filename + " SLOWED" + FORMAT
    print("OUTFILE: " + OUTFILE)
    altered_audio.export(OUTFILE, format=FORMAT.partition('.')[2])

speed_change(os.path.join(PATH, INFILE), 0.801)





















