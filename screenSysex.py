'''
all commands handling lighting
'''

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

def sendMessageTopRow(message):
    device.midiOutSysex(lkc.SYSEX_BEGIN_TOP + str.encode(message) + lkc.SYSEX_END)

def sendMessageBottomRow(message):
    device.midiOutSysex(lkc.SYSEX_BEGIN_BOTTOM + str.encode(message) + lkc.SYSEX_END)

def clearSysexMessage():
    device.midiOutSysex(lkc.SYSEX_CLEAR)