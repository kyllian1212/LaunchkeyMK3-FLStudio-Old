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
import launchkey as lp

#applies to the main pads (note on)
def lightMainPad(state, padNumber, color):
    device.midiOutMsg(0x90, state, padNumber, color)

    if padNumber == lpc.PAD_1:
        lp.padsColor[0][1] == color
        lp.padsState[0][1] == state
    elif padNumber == lpc.PAD_2:
        lp.padsColor[0][2] == color
        lp.padsState[0][2] == state
    elif padNumber == lpc.PAD_3:
        lp.padsColor[0][3] == color
        lp.padsState[0][3] == state
    elif padNumber == lpc.PAD_4:
        lp.padsColor[0][4] == color
        lp.padsState[0][4] == state
    elif padNumber == lpc.PAD_5:
        lp.padsColor[0][5] == color
        lp.padsState[0][5] == state
    elif padNumber == lpc.PAD_6:
        lp.padsColor[0][6] == color
        lp.padsState[0][6] == state
    elif padNumber == lpc.PAD_7:
        lp.padsColor[0][7] == color
        lp.padsState[0][7] == state
    elif padNumber == lpc.PAD_8:
        lp.padsColor[0][8] == color
        lp.padsState[0][8] == state
    elif padNumber == lpc.PAD_9:
        lp.padsColor[1][1] == color
        lp.padsState[1][1] == state
    elif padNumber == lpc.PAD_10:
        lp.padsColor[1][2] == color
        lp.padsState[1][2] == state
    elif padNumber == lpc.PAD_11:
        lp.padsColor[1][3] == color
        lp.padsState[1][3] == state
    elif padNumber == lpc.PAD_12:
        lp.padsColor[1][4] == color
        lp.padsState[1][4] == state
    elif padNumber == lpc.PAD_13:
        lp.padsColor[1][5] == color
        lp.padsState[1][5] == state
    elif padNumber == lpc.PAD_14:
        lp.padsColor[1][6] == color
        lp.padsState[1][6] == state
    elif padNumber == lpc.PAD_15:
        lp.padsColor[1][7] == color
        lp.padsState[1][7] == state
    elif padNumber == lpc.PAD_16:
        lp.padsColor[1][8] == color
        lp.padsState[1][8] == state

#applies to the secondary pads and fader (cc)
def lightCCPad(state, padNumber, color):
    device.midiOutMsg(0xB0, state, padNumber, color)

    if padNumber == lpc.PAD_UPARROW:
        lp.padsColor[0][0] == color
        lp.padsState[0][0] == state
    elif padNumber == lpc.PAD_DOWNARROW:
        lp.padsColor[1][0] == color
        lp.padsState[1][0] == state
    elif padNumber == lpc.PAD_RIGHTARROW:
        lp.padsColor[0][9] == color
        lp.padsState[0][9] == state
    elif padNumber == lpc.PAD_STOPSOLOMUTE:
        lp.padsColor[1][9] == color
        lp.padsState[1][9] == state
    elif padNumber == lpc.FADERBUTTON_1:
        lp.faderButtonsColor[0] == color
        lp.faderButtonsState[0] == state
    elif padNumber == lpc.FADERBUTTON_2:
        lp.faderButtonsColor[1] == color
        lp.faderButtonsState[1] == state
    elif padNumber == lpc.FADERBUTTON_3:
        lp.faderButtonsColor[2] == color
        lp.faderButtonsState[2] == state
    elif padNumber == lpc.FADERBUTTON_4:
        lp.faderButtonsColor[3] == color
        lp.faderButtonsState[3] == state
    elif padNumber == lpc.FADERBUTTON_5:
        lp.faderButtonsColor[4] == color
        lp.faderButtonsState[4] == state
    elif padNumber == lpc.FADERBUTTON_6:
        lp.faderButtonsColor[5] == color
        lp.faderButtonsState[5] == state
    elif padNumber == lpc.FADERBUTTON_7:
        lp.faderButtonsColor[6] == color
        lp.faderButtonsState[6] == state
    elif padNumber == lpc.FADERBUTTON_8:
        lp.faderButtonsColor[7] == color
        lp.faderButtonsState[7] == state
    elif padNumber == lpc.FADERBUTTON_ARMSELECT:
        lp.faderButtonsColor[8] == color
        lp.faderButtonsState[8] == state

#allows to clear the lighting of every pad
def resetLightning():
    lightMainPad(lpc.STATE_STATIONARY, lpc.PAD_1, lpc.COLOR_OFF)
    lightMainPad(lpc.STATE_STATIONARY, lpc.PAD_2, lpc.COLOR_OFF)
    lightMainPad(lpc.STATE_STATIONARY, lpc.PAD_3, lpc.COLOR_OFF)
    lightMainPad(lpc.STATE_STATIONARY, lpc.PAD_4, lpc.COLOR_OFF)
    lightMainPad(lpc.STATE_STATIONARY, lpc.PAD_5, lpc.COLOR_OFF)
    lightMainPad(lpc.STATE_STATIONARY, lpc.PAD_6, lpc.COLOR_OFF)
    lightMainPad(lpc.STATE_STATIONARY, lpc.PAD_7, lpc.COLOR_OFF)
    lightMainPad(lpc.STATE_STATIONARY, lpc.PAD_8, lpc.COLOR_OFF)
    lightMainPad(lpc.STATE_STATIONARY, lpc.PAD_9, lpc.COLOR_OFF)
    lightMainPad(lpc.STATE_STATIONARY, lpc.PAD_10, lpc.COLOR_OFF)
    lightMainPad(lpc.STATE_STATIONARY, lpc.PAD_11, lpc.COLOR_OFF)
    lightMainPad(lpc.STATE_STATIONARY, lpc.PAD_12, lpc.COLOR_OFF)
    lightMainPad(lpc.STATE_STATIONARY, lpc.PAD_13, lpc.COLOR_OFF)
    lightMainPad(lpc.STATE_STATIONARY, lpc.PAD_14, lpc.COLOR_OFF)
    lightMainPad(lpc.STATE_STATIONARY, lpc.PAD_15, lpc.COLOR_OFF)
    lightMainPad(lpc.STATE_STATIONARY, lpc.PAD_16, lpc.COLOR_OFF)
    
    lightCCPad(lpc.STATE_STATIONARY, lpc.PAD_UPARROW, lpc.COLOR_OFF)
    lightCCPad(lpc.STATE_STATIONARY, lpc.PAD_DOWNARROW, lpc.COLOR_OFF)
    lightCCPad(lpc.STATE_STATIONARY, lpc.PAD_RIGHTARROW, lpc.COLOR_OFF)
    lightCCPad(lpc.STATE_STATIONARY, lpc.PAD_STOPSOLOMUTE, lpc.COLOR_OFF)
    lightCCPad(lpc.STATE_STATIONARY, lpc.FADERBUTTON_1, lpc.COLOR_OFF)
    lightCCPad(lpc.STATE_STATIONARY, lpc.FADERBUTTON_2, lpc.COLOR_OFF)
    lightCCPad(lpc.STATE_STATIONARY, lpc.FADERBUTTON_3, lpc.COLOR_OFF)
    lightCCPad(lpc.STATE_STATIONARY, lpc.FADERBUTTON_4, lpc.COLOR_OFF)
    lightCCPad(lpc.STATE_STATIONARY, lpc.FADERBUTTON_5, lpc.COLOR_OFF)
    lightCCPad(lpc.STATE_STATIONARY, lpc.FADERBUTTON_6, lpc.COLOR_OFF)
    lightCCPad(lpc.STATE_STATIONARY, lpc.FADERBUTTON_7, lpc.COLOR_OFF)
    lightCCPad(lpc.STATE_STATIONARY, lpc.FADERBUTTON_8, lpc.COLOR_OFF)
    lightCCPad(lpc.STATE_STATIONARY, lpc.FADERBUTTON_ARMSELECT, lpc.COLOR_OFF)