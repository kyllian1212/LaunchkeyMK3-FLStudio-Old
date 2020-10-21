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

#applies to the main pads (note on)
def lightMainPad(state, padNumber, color):
    device.midiOutMsg(0x90, state, padNumber, color)

    if padNumber == lkc.PAD_1:
        lk.padsColor[0][1] == color
        lk.padsState[0][1] == state
    elif padNumber == lkc.PAD_2:
        lk.padsColor[0][2] == color
        lk.padsState[0][2] == state
    elif padNumber == lkc.PAD_3:
        lk.padsColor[0][3] == color
        lk.padsState[0][3] == state
    elif padNumber == lkc.PAD_4:
        lk.padsColor[0][4] == color
        lk.padsState[0][4] == state
    elif padNumber == lkc.PAD_5:
        lk.padsColor[0][5] == color
        lk.padsState[0][5] == state
    elif padNumber == lkc.PAD_6:
        lk.padsColor[0][6] == color
        lk.padsState[0][6] == state
    elif padNumber == lkc.PAD_7:
        lk.padsColor[0][7] == color
        lk.padsState[0][7] == state
    elif padNumber == lkc.PAD_8:
        lk.padsColor[0][8] == color
        lk.padsState[0][8] == state
    elif padNumber == lkc.PAD_9:
        lk.padsColor[1][1] == color
        lk.padsState[1][1] == state
    elif padNumber == lkc.PAD_10:
        lk.padsColor[1][2] == color
        lk.padsState[1][2] == state
    elif padNumber == lkc.PAD_11:
        lk.padsColor[1][3] == color
        lk.padsState[1][3] == state
    elif padNumber == lkc.PAD_12:
        lk.padsColor[1][4] == color
        lk.padsState[1][4] == state
    elif padNumber == lkc.PAD_13:
        lk.padsColor[1][5] == color
        lk.padsState[1][5] == state
    elif padNumber == lkc.PAD_14:
        lk.padsColor[1][6] == color
        lk.padsState[1][6] == state
    elif padNumber == lkc.PAD_15:
        lk.padsColor[1][7] == color
        lk.padsState[1][7] == state
    elif padNumber == lkc.PAD_16:
        lk.padsColor[1][8] == color
        lk.padsState[1][8] == state

#applies to the secondary pads and fader (cc)
def lightCCPad(state, padNumber, color):
    device.midiOutMsg(0xB0, state, padNumber, color)

    if padNumber == lkc.PAD_UPARROW:
        lk.padsColor[0][0] == color
        lk.padsState[0][0] == state
    elif padNumber == lkc.PAD_DOWNARROW:
        lk.padsColor[1][0] == color
        lk.padsState[1][0] == state
    elif padNumber == lkc.PAD_RIGHTARROW:
        lk.padsColor[0][9] == color
        lk.padsState[0][9] == state
    elif padNumber == lkc.PAD_STOPSOLOMUTE:
        lk.padsColor[1][9] == color
        lk.padsState[1][9] == state
    elif padNumber == lkc.FADERBUTTON_1:
        lk.faderButtonsColor[0] == color
        lk.faderButtonsState[0] == state
    elif padNumber == lkc.FADERBUTTON_2:
        lk.faderButtonsColor[1] == color
        lk.faderButtonsState[1] == state
    elif padNumber == lkc.FADERBUTTON_3:
        lk.faderButtonsColor[2] == color
        lk.faderButtonsState[2] == state
    elif padNumber == lkc.FADERBUTTON_4:
        lk.faderButtonsColor[3] == color
        lk.faderButtonsState[3] == state
    elif padNumber == lkc.FADERBUTTON_5:
        lk.faderButtonsColor[4] == color
        lk.faderButtonsState[4] == state
    elif padNumber == lkc.FADERBUTTON_6:
        lk.faderButtonsColor[5] == color
        lk.faderButtonsState[5] == state
    elif padNumber == lkc.FADERBUTTON_7:
        lk.faderButtonsColor[6] == color
        lk.faderButtonsState[6] == state
    elif padNumber == lkc.FADERBUTTON_8:
        lk.faderButtonsColor[7] == color
        lk.faderButtonsState[7] == state
    elif padNumber == lkc.FADERBUTTON_ARMSELECT:
        lk.faderButtonsColor[8] == color
        lk.faderButtonsState[8] == state

#allows to clear the lighting of every pad
def resetLightning():
    lightMainPad(lkc.STATE_STATIONARY, lkc.PAD_1, lkc.COLOR_OFF)
    lightMainPad(lkc.STATE_STATIONARY, lkc.PAD_2, lkc.COLOR_OFF)
    lightMainPad(lkc.STATE_STATIONARY, lkc.PAD_3, lkc.COLOR_OFF)
    lightMainPad(lkc.STATE_STATIONARY, lkc.PAD_4, lkc.COLOR_OFF)
    lightMainPad(lkc.STATE_STATIONARY, lkc.PAD_5, lkc.COLOR_OFF)
    lightMainPad(lkc.STATE_STATIONARY, lkc.PAD_6, lkc.COLOR_OFF)
    lightMainPad(lkc.STATE_STATIONARY, lkc.PAD_7, lkc.COLOR_OFF)
    lightMainPad(lkc.STATE_STATIONARY, lkc.PAD_8, lkc.COLOR_OFF)
    lightMainPad(lkc.STATE_STATIONARY, lkc.PAD_9, lkc.COLOR_OFF)
    lightMainPad(lkc.STATE_STATIONARY, lkc.PAD_10, lkc.COLOR_OFF)
    lightMainPad(lkc.STATE_STATIONARY, lkc.PAD_11, lkc.COLOR_OFF)
    lightMainPad(lkc.STATE_STATIONARY, lkc.PAD_12, lkc.COLOR_OFF)
    lightMainPad(lkc.STATE_STATIONARY, lkc.PAD_13, lkc.COLOR_OFF)
    lightMainPad(lkc.STATE_STATIONARY, lkc.PAD_14, lkc.COLOR_OFF)
    lightMainPad(lkc.STATE_STATIONARY, lkc.PAD_15, lkc.COLOR_OFF)
    lightMainPad(lkc.STATE_STATIONARY, lkc.PAD_16, lkc.COLOR_OFF)
    
    lightCCPad(lkc.STATE_STATIONARY, lkc.PAD_UPARROW, lkc.COLOR_OFF)
    lightCCPad(lkc.STATE_STATIONARY, lkc.PAD_DOWNARROW, lkc.COLOR_OFF)
    lightCCPad(lkc.STATE_STATIONARY, lkc.PAD_RIGHTARROW, lkc.COLOR_OFF)
    lightCCPad(lkc.STATE_STATIONARY, lkc.PAD_STOPSOLOMUTE, lkc.COLOR_OFF)
    lightCCPad(lkc.STATE_STATIONARY, lkc.FADERBUTTON_1, lkc.COLOR_OFF)
    lightCCPad(lkc.STATE_STATIONARY, lkc.FADERBUTTON_2, lkc.COLOR_OFF)
    lightCCPad(lkc.STATE_STATIONARY, lkc.FADERBUTTON_3, lkc.COLOR_OFF)
    lightCCPad(lkc.STATE_STATIONARY, lkc.FADERBUTTON_4, lkc.COLOR_OFF)
    lightCCPad(lkc.STATE_STATIONARY, lkc.FADERBUTTON_5, lkc.COLOR_OFF)
    lightCCPad(lkc.STATE_STATIONARY, lkc.FADERBUTTON_6, lkc.COLOR_OFF)
    lightCCPad(lkc.STATE_STATIONARY, lkc.FADERBUTTON_7, lkc.COLOR_OFF)
    lightCCPad(lkc.STATE_STATIONARY, lkc.FADERBUTTON_8, lkc.COLOR_OFF)
    lightCCPad(lkc.STATE_STATIONARY, lkc.FADERBUTTON_ARMSELECT, lkc.COLOR_OFF)