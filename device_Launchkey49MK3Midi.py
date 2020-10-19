# name=Launchkey 49 MK3 Midi

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

#python imports
import sys
import time

#variables
dawInit = False

class TMain:
    def __init__(self):
        return
    
    def OnInit(self):
        global dawInit

        if device.isAssigned() == 0:
            print('DEVICE PORT NOT ASSIGNED. EXITING.')
            sys.exit(0)
        print('init completed')
        device.midiOutMsg(0x9F, 0x0F, 0x0C, 0x7F)

        l.initLightning()

        device.midiOutSysex(lpc.SYSEX_BEGIN_TOP + str.encode(ui.getProgTitle()) + lpc.SYSEX_END)
        device.midiOutSysex(lpc.SYSEX_BEGIN_BOTTOM + str.encode(ui.getVersion()) + lpc.SYSEX_END)
        
        dawInit = True

    def OnDeInit(self):
        global dawInit

        if device.isAssigned() == 0:
            print('DEVICE PORT NOT ASSIGNED. EXITING.')
            sys.exit(0)
        print('deinit completed')
        device.midiOutMsg(0x9F, 0x0F, 0x0C, 0x00)

        dawInit = False

    def OnMidiMsg(self, event):
        event.handled = False
        print('--------------------------------')
        print('midi id:', event.midiId, '| midi status:', event.status, '| midi channel:', event.midiChan, 
        '| midi data1:', event.data1, '| midi data2:', event.data2, '| midi sysex:', event.sysex)
        if event.midiId == midi.MIDI_CONTROLCHANGE:
            if event.data2 > 0:
                #capture midi
                if event.data1 == lpc.BTN_CAPTUREMIDI:
                    inactiveButton()
                #quantise
                if event.data1 == lpc.BTN_QUANTISE:
                    inactiveButton()
                #click
                elif event.data1 == lpc.BTN_CLICK:
                    inactiveButton()
                #undo
                elif event.data1 == lpc.BTN_UNDO:
                    general.undo()
                #play/pause
                elif event.data1 == lpc.BTN_PLAY:
                    transport.start()
                #stop
                elif event.data1 == lpc.BTN_STOP:
                    transport.stop()
                #record
                elif event.data1 == lpc.BTN_RECORD:
                    transport.record()
                #pattern/song
                elif event.data1 == lpc.BTN_PATTERN:
                    transport.setLoopMode()
                    
        #end of btn press
        event.handled = True

    def OnRefresh(self, flags):
        print('refresh')

    def OnDirtyMixerTrack(self, index):
        mixerTrackNumberStr = str(mixer.trackNumber())
        mixerTrackName = mixer.getTrackName(mixer.trackNumber())
        mixerTrackInfo = mixerTrackNumberStr + " - " + mixerTrackName

        time.sleep(0.05) #fixes the issue with the wrong settings being sent to the launchkey

        mixerTrackVolume = str("{:.1f}".format(mixer.getTrackVolume(mixer.trackNumber())*125))
        mixerTrackPan = str("{:.0f}".format(mixer.getTrackPan(mixer.trackNumber())*100))
        mixerTrackSettings = "V" + mixerTrackVolume + "% | P" + mixerTrackPan + "%"

        device.midiOutSysex(lpc.SYSEX_BEGIN_TOP + str.encode(mixerTrackInfo) + lpc.SYSEX_END)
        device.midiOutSysex(lpc.SYSEX_BEGIN_BOTTOM + str.encode(mixerTrackSettings) + lpc.SYSEX_END)


Main = TMain()


def OnInit():
    try:
        Main.OnInit()
    except:
        errorHandler()
    
def OnDeInit():
    try:
        Main.OnDeInit()
    except:
        errorHandler()

def OnMidiMsg(event):
    try:
        Main.OnMidiMsg(event)
    except:
        errorHandler()

def onRefresh(flags):
    try:
        Main.OnRefresh(flags)
    except:
        errorHandler()

def OnDirtyMixerTrack(index):
    try:
        Main.OnDirtyMixerTrack(index)
    except:
        errorHandler()

def clearSysexMessage():
    try:
        device.midiOutSysex(lpc.SYSEX_CLEAR)
    except:
        errorHandler()

def inactiveButton():
    buttonInactiveTop = "Button currently"
    buttonInactiveBottom = "inactive"

    device.midiOutSysex(lpc.SYSEX_BEGIN_TOP + str.encode(buttonInactiveTop) + lpc.SYSEX_END)
    device.midiOutSysex(lpc.SYSEX_BEGIN_BOTTOM + str.encode(buttonInactiveBottom) + lpc.SYSEX_END)

#error handler if something happens and it crashes
def errorHandler():
    global dawInit
    if dawInit:
        l.lightMainPad(lpc.COLORMODE_PULSING, lpc.PAD_1, lpc.COLOR_RED)
        l.lightMainPad(lpc.COLORMODE_PULSING, lpc.PAD_2, lpc.COLOR_RED)
        l.lightMainPad(lpc.COLORMODE_PULSING, lpc.PAD_3, lpc.COLOR_RED)
        l.lightMainPad(lpc.COLORMODE_PULSING, lpc.PAD_4, lpc.COLOR_RED)
        l.lightMainPad(lpc.COLORMODE_PULSING, lpc.PAD_5, lpc.COLOR_RED)
        l.lightMainPad(lpc.COLORMODE_PULSING, lpc.PAD_6, lpc.COLOR_RED)
        l.lightMainPad(lpc.COLORMODE_PULSING, lpc.PAD_7, lpc.COLOR_RED)
        l.lightMainPad(lpc.COLORMODE_PULSING, lpc.PAD_8, lpc.COLOR_RED)
        l.lightMainPad(lpc.COLORMODE_PULSING, lpc.PAD_9, lpc.COLOR_RED)
        l.lightMainPad(lpc.COLORMODE_PULSING, lpc.PAD_10, lpc.COLOR_RED)
        l.lightMainPad(lpc.COLORMODE_PULSING, lpc.PAD_11, lpc.COLOR_RED)
        l.lightMainPad(lpc.COLORMODE_PULSING, lpc.PAD_12, lpc.COLOR_RED)
        l.lightMainPad(lpc.COLORMODE_PULSING, lpc.PAD_13, lpc.COLOR_RED)
        l.lightMainPad(lpc.COLORMODE_PULSING, lpc.PAD_14, lpc.COLOR_RED)
        l.lightMainPad(lpc.COLORMODE_PULSING, lpc.PAD_15, lpc.COLOR_RED)
        l.lightMainPad(lpc.COLORMODE_PULSING, lpc.PAD_16, lpc.COLOR_RED)

        l.lightCCPad(lpc.COLORMODE_PULSING, lpc.PAD_UPARROW, lpc.COLOR_RED)
        l.lightCCPad(lpc.COLORMODE_PULSING, lpc.PAD_DOWNARROW, lpc.COLOR_RED)
        l.lightCCPad(lpc.COLORMODE_PULSING, lpc.PAD_RIGHTARROW, lpc.COLOR_RED)
        l.lightCCPad(lpc.COLORMODE_PULSING, lpc.PAD_STOPSOLOMUTE, lpc.COLOR_RED)
        l.lightCCPad(lpc.COLORMODE_PULSING, lpc.FADERBUTTON_1, lpc.COLOR_RED)
        l.lightCCPad(lpc.COLORMODE_PULSING, lpc.FADERBUTTON_2, lpc.COLOR_RED)
        l.lightCCPad(lpc.COLORMODE_PULSING, lpc.FADERBUTTON_3, lpc.COLOR_RED)
        l.lightCCPad(lpc.COLORMODE_PULSING, lpc.FADERBUTTON_4, lpc.COLOR_RED)
        l.lightCCPad(lpc.COLORMODE_PULSING, lpc.FADERBUTTON_5, lpc.COLOR_RED)
        l.lightCCPad(lpc.COLORMODE_PULSING, lpc.FADERBUTTON_6, lpc.COLOR_RED)
        l.lightCCPad(lpc.COLORMODE_PULSING, lpc.FADERBUTTON_7, lpc.COLOR_RED)
        l.lightCCPad(lpc.COLORMODE_PULSING, lpc.FADERBUTTON_8, lpc.COLOR_RED)

        device.midiOutSysex(lpc.SYSEX_BEGIN_TOP + str.encode("EXCEPTION!!!!!!!") + lpc.SYSEX_END)
        device.midiOutSysex(lpc.SYSEX_BEGIN_BOTTOM + str.encode("INSTRUCTIONS:") + lpc.SYSEX_END)
        time.sleep(4)
        device.midiOutSysex(lpc.SYSEX_BEGIN_TOP + str.encode("CHECK VIEW >") + lpc.SYSEX_END)
        device.midiOutSysex(lpc.SYSEX_BEGIN_BOTTOM + str.encode("SCRIPT OUTPUT") + lpc.SYSEX_END)
        time.sleep(4)
        device.midiOutSysex(lpc.SYSEX_BEGIN_TOP + str.encode("FOR TRACEBACK") + lpc.SYSEX_END)
        device.midiOutSysex(lpc.SYSEX_BEGIN_BOTTOM + str.encode("AND TO RELOAD.") + lpc.SYSEX_END)
        time.sleep(4)
        device.midiOutSysex(lpc.SYSEX_BEGIN_TOP + str.encode("REVERTING TO") + lpc.SYSEX_END)
        device.midiOutSysex(lpc.SYSEX_BEGIN_BOTTOM + str.encode("MIDI MODE...") + lpc.SYSEX_END)
        time.sleep(4)

        device.midiOutMsg(0x9F, 0x0F, 0x0C, 0x00)

        dawInit = False
        
        sys.exit(-1)