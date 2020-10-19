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

#applies to the main pads (note on)
def lightMainPad(colorMode, padNumber, color):
    device.midiOutMsg(0x90, colorMode, padNumber, color)

#applies to the secondary pads and fader (cc)
def lightCCPad(colorMode, padNumber, color):
    device.midiOutMsg(0xB0, colorMode, padNumber, color)

#clearing the lighting at the beginning just incase
def initLightning():
    lightMainPad(lpc.COLORMODE_STATIONARY, lpc.PAD_1, lpc.COLOR_OFF)
    lightMainPad(lpc.COLORMODE_STATIONARY, lpc.PAD_2, lpc.COLOR_OFF)
    lightMainPad(lpc.COLORMODE_STATIONARY, lpc.PAD_3, lpc.COLOR_OFF)
    lightMainPad(lpc.COLORMODE_STATIONARY, lpc.PAD_4, lpc.COLOR_OFF)
    lightMainPad(lpc.COLORMODE_STATIONARY, lpc.PAD_5, lpc.COLOR_OFF)
    lightMainPad(lpc.COLORMODE_STATIONARY, lpc.PAD_6, lpc.COLOR_OFF)
    lightMainPad(lpc.COLORMODE_STATIONARY, lpc.PAD_7, lpc.COLOR_OFF)
    lightMainPad(lpc.COLORMODE_STATIONARY, lpc.PAD_8, lpc.COLOR_OFF)
    lightMainPad(lpc.COLORMODE_STATIONARY, lpc.PAD_9, lpc.COLOR_OFF)
    lightMainPad(lpc.COLORMODE_STATIONARY, lpc.PAD_10, lpc.COLOR_OFF)
    lightMainPad(lpc.COLORMODE_STATIONARY, lpc.PAD_11, lpc.COLOR_OFF)
    lightMainPad(lpc.COLORMODE_STATIONARY, lpc.PAD_12, lpc.COLOR_OFF)
    lightMainPad(lpc.COLORMODE_STATIONARY, lpc.PAD_13, lpc.COLOR_OFF)
    lightMainPad(lpc.COLORMODE_STATIONARY, lpc.PAD_14, lpc.COLOR_OFF)
    lightMainPad(lpc.COLORMODE_STATIONARY, lpc.PAD_15, lpc.COLOR_OFF)
    lightMainPad(lpc.COLORMODE_STATIONARY, lpc.PAD_16, lpc.COLOR_OFF)
    
    lightCCPad(lpc.COLORMODE_STATIONARY, lpc.PAD_UPARROW, lpc.COLOR_OFF)
    lightCCPad(lpc.COLORMODE_STATIONARY, lpc.PAD_DOWNARROW, lpc.COLOR_OFF)
    lightCCPad(lpc.COLORMODE_STATIONARY, lpc.PAD_RIGHTARROW, lpc.COLOR_OFF)
    lightCCPad(lpc.COLORMODE_STATIONARY, lpc.PAD_STOPSOLOMUTE, lpc.COLOR_OFF)
    lightCCPad(lpc.COLORMODE_STATIONARY, lpc.FADERBUTTON_1, lpc.COLOR_OFF)
    lightCCPad(lpc.COLORMODE_STATIONARY, lpc.FADERBUTTON_2, lpc.COLOR_OFF)
    lightCCPad(lpc.COLORMODE_STATIONARY, lpc.FADERBUTTON_3, lpc.COLOR_OFF)
    lightCCPad(lpc.COLORMODE_STATIONARY, lpc.FADERBUTTON_4, lpc.COLOR_OFF)
    lightCCPad(lpc.COLORMODE_STATIONARY, lpc.FADERBUTTON_5, lpc.COLOR_OFF)
    lightCCPad(lpc.COLORMODE_STATIONARY, lpc.FADERBUTTON_6, lpc.COLOR_OFF)
    lightCCPad(lpc.COLORMODE_STATIONARY, lpc.FADERBUTTON_7, lpc.COLOR_OFF)
    lightCCPad(lpc.COLORMODE_STATIONARY, lpc.FADERBUTTON_8, lpc.COLOR_OFF)
    lightCCPad(lpc.COLORMODE_STATIONARY, lpc.FADERBUTTON_ARMSELECT, lpc.COLOR_OFF)