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
import ui
import transport
import device
import general
import launchMapPages
import midi

#ext imports
import launchkeyConsts as lpc

def sendMessageTopRow(message):
    device.midiOutSysex(lpc.SYSEX_BEGIN_TOP + str.encode(message) + lpc.SYSEX_END)

def sendMessageBottomRow(message):
    device.midiOutSysex(lpc.SYSEX_BEGIN_BOTTOM + str.encode(message) + lpc.SYSEX_END)