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

def mixerSettingInterface(event):
    #lights up stop buttons
    l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[19], lkc.COLOR_DARKERRED)

    s.sendMessageTopRow("Settings - Mixer")
    #lights up the settings
    if m.setting == mc.MIXERMODE_8TRACKS or event.status == 144 and event.data1 == 96 and event.data2 > 0:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[0], lkc.COLOR_WHITE)
        s.sendMessageBottomRow("Pads: 8 tracks")
        m.setting = mc.MIXERMODE_8TRACKS
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[0], lkc.COLOR_DARKER)
    
    if m.setting == mc.MIXERMODE_1TRACK or event.status == 144 and event.data1 == 97 and event.data2 > 0:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[1], lkc.COLOR_WHITE)
        s.sendMessageBottomRow("Pads: 1 track")
        m.setting = mc.MIXERMODE_1TRACK
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[1], lkc.COLOR_DARKER)
    
    if m.setting == mc.MIXERMODE_1MASTER or event.status == 144 and event.data1 == 98 and event.data2 > 0:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[2], lkc.COLOR_WHITE)
        s.sendMessageBottomRow("Pads: Master")
        m.setting = mc.MIXERMODE_1MASTER
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[2], lkc.COLOR_DARKER)

    if event.data1 == 105 and event.status == 176 and event.data2 == 127:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[19], lkc.COLOR_RED)
        s.clearSysexMessage()
    elif event.data1 == 105 and event.status == 176 and event.data2 == 0:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[19], lkc.COLOR_DARKERRED)