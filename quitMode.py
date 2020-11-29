#fl imports
import ui
import playlist
import channels
import mixer
import patterns
import arrangement
import transport
import device
import general
import launchMapPages
import midi

#ext imports
import launchkeyConsts as lkc
import launchkey as lk
import lighting as l
import screenSysex as s
import mixerMode as m
import mixerModeConsts as mc
import programConsts as prog

#python imports
import sys
import time

def quitModeInterface(event):
    #lights up stop and right arrow buttons
    l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[18], lkc.COLOR_DARKERGREEN)
    l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[19], lkc.COLOR_DARKERRED)

    s.sendMessageTopRow("Are you sure you")
    s.sendMessageBottomRow("want to quit?")
    if event.data1 == 104 and event.status == 176 and event.data2 == 127:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[18], lkc.COLOR_GREEN)
    elif event.data1 == 104 and event.status == 176 and event.data2 == 0:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[18], lkc.COLOR_DARKERGREEN)

    if event.data1 == 105 and event.status == 176 and event.data2 == 127:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[19], lkc.COLOR_RED)
    elif event.data1 == 105 and event.status == 176 and event.data2 == 0:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[19], lkc.COLOR_DARKERRED)