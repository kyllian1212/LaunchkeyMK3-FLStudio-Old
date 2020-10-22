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
import launchkeyConsts as lkc
import launchkey as lk

def lightPad(state, padNumber, color):
    if list(lk.lightingDict).index(padNumber) <= 15:
        device.midiOutMsg(0x90, state, padNumber, color)
    else:
        device.midiOutMsg(0xB0, state, padNumber, color)
    
    lk.lightingDict[padNumber][0] = color
    lk.lightingDict[padNumber][1] = state
    
#allows to clear the lighting of every pad
def resetLightning():
    for light in lk.lightingDict:
        lightPad(lkc.STATE_STATIONARY, light, lkc.COLOR_OFF)