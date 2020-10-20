'''
every launchkey param!
'''

#fl imports
import ui
import playlist
import channels
import mixer
import patterns
import arrangement
import ui
import transport
import device
import general
import launchMapPages
import midi

#ext imports
import consts as c
import launchkeyConsts as lpc
import lighting as l
import screenSysex as s

#python imports
import sys
import time

'''which state every launchkey params have!'''
#DAW mode state on the launchkey
dawMode = False

#which color each pad has rn
padsColor = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]

#which state each pad has rn
padsState = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]

#which color each fader button has rn
faderButtonsColor = [0,0,0,0,0,0,0,0,0]

#which state each fader button has rn
faderButtonsState = [0,0,0,0,0,0,0,0,0]

#enable daw mode
def enableDAW():
    global dawMode
    dawMode = True
    device.midiOutMsg(0x9F, 0x0F, 0x0C, 0x7F)

#disable daw mode
def disableDAW():
    global dawMode
    dawMode = False
    device.midiOutMsg(0x9F, 0x0F, 0x0C, 0x00)