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

from keys import lightingDict

def lightPad(state, padNumber, color):
    lightingDict[padNumber][0] = color
    lightingDict[padNumber][1] = state
    
#allows to clear the lighting of every pad
def resetLightning():
    for light in lightingDict:
        lightPad(lkc.STATE_STATIONARY, light, lkc.COLOR_OFF)