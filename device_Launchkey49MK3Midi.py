# name=Launchkey 49 MK3 Midi

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
import mixerSettingsMode as ms
import quitMode as q
import programConsts as prog

#python imports
import sys
import time

class TMain:
    def __init__(self):
        return
    
    def OnInit(self):
        global programMode

        if device.isAssigned() == 0:
            print('DEVICE PORT NOT ASSIGNED. EXITING.')
            sys.exit(0)
        print('init completed')

        lk.enableDAW()
        l.resetLightning()

        device.setHasMeters()

        lk.modeChange(prog.MODE_INIT)
        s.sendMessageTopRow(ui.getProgTitle())
        s.sendMessageBottomRow(ui.getVersion())
        m.mixerInterface()
        lk.modeChange(prog.MODE_MIXER)


    def OnDeInit(self):
        if device.isAssigned() == 0:
            print('DEVICE PORT NOT ASSIGNED. EXITING.')
            sys.exit(0)
        print('deinit completed')

        lk.modeChange(prog.MODE_OFF)
        
        lk.disableDAW()


    def OnMidiMsg(self, event):
        event.handled = False
        btnPressedFromPastMode = True
        print('--------------------------------')
        print('midi id:', event.midiId, '| midi status:', event.status, '| midi channel:', event.midiChan, 
        '| midi data1:', event.data1, '| midi data2:', event.data2, '| midi sysex:', event.sysex)
        if event.midiId == midi.MIDI_CONTROLCHANGE:
            if event.data2 > 0:
                #capture midi
                if event.data1 == lkc.BTN_CAPTUREMIDI:
                    inactiveButton()
                #quantise
                if event.data1 == lkc.BTN_QUANTISE:
                    inactiveButton()
                #click
                elif event.data1 == lkc.BTN_CLICK:
                    inactiveButton()
                #undo
                elif event.data1 == lkc.BTN_UNDO:
                    general.undo()
                #play/pause
                elif event.data1 == lkc.BTN_PLAY:
                    transport.start()
                #stop
                elif event.data1 == lkc.BTN_STOP:
                    transport.stop()
                #record
                elif event.data1 == lkc.BTN_RECORD:
                    transport.record()
                #pattern/song
                elif event.data1 == lkc.BTN_PATTERN:
                    transport.setLoopMode()
        
        if event.data1 == 108 and event.status == 176 and event.data2 == 127:
            lk.modeChange(prog.MODE_SHIFT)
        elif event.data1 == 108 and event.status == 176 and event.data2 == 0:
            lk.modeChange(prog.MODE_MIXER)

        if lk.programMode == prog.MODE_MIXER:
            m.mixerEvent(event)
            if event.data1 == 104 and event.status == 176 and event.data2 == 127:
                l.resetLightning()
                lk.modeChange(prog.MODE_MIXERSETTINGS)
                ms.mixerSettingInterface(event)
            if event.data1 == 105 and event.status == 176 and event.data2 == 127:
                l.resetLightning()
                lk.modeChange(prog.MODE_QUITPROGRAMMENU)
                q.quitModeInterface(event)
                btnPressedFromPastMode = False
        
        if lk.programMode == prog.MODE_MIXERSETTINGS:
            ms.mixerSettingInterface(event)
            if event.data1 == 105 and event.status == 176 and event.data2 == 127:
                l.resetLightning()
                lk.modeChange(prog.MODE_MIXER)
                m.mixerInterface()
        
        if lk.programMode == prog.MODE_QUITPROGRAMMENU:
            q.quitModeInterface(event)
            if event.data1 == 104 and event.status == 176 and event.data2 == 127:
                l.resetLightning()
                s.clearSysexMessage()
                lk.modeChange(prog.MODE_OFF)
                lk.disableDAW()
            if event.data1 == 105 and event.status == 176 and event.data2 == 127 and btnPressedFromPastMode:
                l.resetLightning()
                s.clearSysexMessage()
                lk.modeChange(prog.MODE_MIXER)
                m.mixerInterface()
            
        
        #end of btn press
        event.handled = True

    def OnRefresh(self, flags):
        print('refresh')

    def OnUpdateBeatIndicator(self, value):
        if lk.programMode == prog.MODE_MENU:
            if value == 0:
                l.lightPad(lkc.STATE_STATIONARY, lkc.FADERBUTTON_ARMSELECT, lkc.COLOR_OFF)
            elif value == 1:
                l.lightPad(lkc.STATE_STATIONARY, lkc.FADERBUTTON_ARMSELECT, lkc.COLOR_WHITE)
            elif value == 2:
                l.lightPad(lkc.STATE_STATIONARY, lkc.FADERBUTTON_ARMSELECT, lkc.COLOR_DARKER)

    def OnDirtyMixerTrack(self, index):
        global programMode

        if lk.programMode == prog.MODE_MIXER:
            m.mixerUpdate(index)
            m.mixerInterface()

    def OnUpdateMeters(self):
        global programMode

        if lk.programMode == prog.MODE_MIXER:
            m.mixerPeakInterface()
        

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

def OnUpdateBeatIndicator(value):
    try:
        Main.OnUpdateBeatIndicator(value)
    except:
        errorHandler()

def OnDirtyMixerTrack(index):
    try:
        Main.OnDirtyMixerTrack(index)
    except:
        errorHandler()

def OnUpdateMeters():
    try:
        Main.OnUpdateMeters()
    except:
        errorHandler()

#not fl functions
def inactiveButton():
    buttonInactiveTop = "Button currently"
    buttonInactiveBottom = "inactive"

    device.midiOutSysex(lkc.SYSEX_BEGIN_TOP + str.encode(buttonInactiveTop) + lkc.SYSEX_END)
    device.midiOutSysex(lkc.SYSEX_BEGIN_BOTTOM + str.encode(buttonInactiveBottom) + lkc.SYSEX_END)

#error handler if something happens and it crashes
def errorHandler():
    SLEEP_TIME = 0.25
    if lk.dawMode:
        for light in list(lk.lightingDict)[:-1]:
            l.lightPad(lkc.STATE_PULSING, light, lkc.COLOR_RED)

        s.sendMessageTopRow("EXCEPTION!!!!!!!")
        s.sendMessageBottomRow("INSTRUCTIONS:")
        time.sleep(SLEEP_TIME)
        s.sendMessageTopRow("CHECK VIEW >")
        s.sendMessageBottomRow("SCRIPT OUTPUT")
        time.sleep(SLEEP_TIME)
        s.sendMessageTopRow("FOR TRACEBACK")
        s.sendMessageBottomRow("AND TO RELOAD.")
        time.sleep(SLEEP_TIME)
        s.sendMessageTopRow("REVERTING TO")
        s.sendMessageBottomRow("MIDI MODE...")
        time.sleep(SLEEP_TIME)

        lk.disableDAW()
        
        sys.exit(-1)