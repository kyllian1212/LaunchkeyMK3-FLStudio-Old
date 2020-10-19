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
        initLightning()

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
                    print('capture midi')
                #quantise
                if event.data1 == lpc.BTN_QUANTISE:
                    print('quantise')
                #click
                elif event.data1 == lpc.BTN_CLICK:
                    print(general.getUseMetronome())
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

def errorHandler():
    global dawInit
    if dawInit:
        device.midiOutMsg(0x90, 0x02, 0x60, 0x05)
        device.midiOutMsg(0x90, 0x02, 0x61, 0x05)
        device.midiOutMsg(0x90, 0x02, 0x62, 0x05)
        device.midiOutMsg(0x90, 0x02, 0x63, 0x05)
        device.midiOutMsg(0x90, 0x02, 0x64, 0x05)
        device.midiOutMsg(0x90, 0x02, 0x65, 0x05)
        device.midiOutMsg(0x90, 0x02, 0x66, 0x05)
        device.midiOutMsg(0x90, 0x02, 0x67, 0x05)
        device.midiOutMsg(0xB0, 0x02, 0x68, 0x05)
        device.midiOutMsg(0xB0, 0x02, 0x69, 0x05)
        device.midiOutMsg(0xB0, 0x02, 0x6A, 0x05)
        device.midiOutMsg(0xB0, 0x02, 0x6B, 0x05)
        device.midiOutMsg(0x90, 0x02, 0x70, 0x05)
        device.midiOutMsg(0x90, 0x02, 0x71, 0x05)
        device.midiOutMsg(0x90, 0x02, 0x72, 0x05)
        device.midiOutMsg(0x90, 0x02, 0x73, 0x05)
        device.midiOutMsg(0x90, 0x02, 0x74, 0x05)
        device.midiOutMsg(0x90, 0x02, 0x75, 0x05)
        device.midiOutMsg(0x90, 0x02, 0x76, 0x05)
        device.midiOutMsg(0x90, 0x02, 0x77, 0x05)

        device.midiOutMsg(0xB0, 0x02, 0x25, 0x05)
        device.midiOutMsg(0xB0, 0x02, 0x26, 0x05)
        device.midiOutMsg(0xB0, 0x02, 0x27, 0x05)
        device.midiOutMsg(0xB0, 0x02, 0x28, 0x05)
        device.midiOutMsg(0xB0, 0x02, 0x29, 0x05)
        device.midiOutMsg(0xB0, 0x02, 0x2A, 0x05)
        device.midiOutMsg(0xB0, 0x02, 0x2B, 0x05)
        device.midiOutMsg(0xB0, 0x02, 0x2C, 0x05)

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

def initLightning():
    #temp until i do the lighting stuff
    device.midiOutMsg(0x90, 0x02, 0x60, 0x00)
    device.midiOutMsg(0x90, 0x02, 0x61, 0x00)
    device.midiOutMsg(0x90, 0x02, 0x62, 0x00)
    device.midiOutMsg(0x90, 0x02, 0x63, 0x00)
    device.midiOutMsg(0x90, 0x02, 0x64, 0x00)
    device.midiOutMsg(0x90, 0x02, 0x65, 0x00)
    device.midiOutMsg(0x90, 0x02, 0x66, 0x00)
    device.midiOutMsg(0x90, 0x02, 0x67, 0x00)
    device.midiOutMsg(0xB0, 0x02, 0x68, 0x00)
    device.midiOutMsg(0xB0, 0x02, 0x69, 0x00)
    device.midiOutMsg(0xB0, 0x02, 0x6A, 0x00)
    device.midiOutMsg(0xB0, 0x02, 0x6B, 0x00)
    device.midiOutMsg(0x90, 0x02, 0x70, 0x00)
    device.midiOutMsg(0x90, 0x02, 0x71, 0x00)
    device.midiOutMsg(0x90, 0x02, 0x72, 0x00)
    device.midiOutMsg(0x90, 0x02, 0x73, 0x00)
    device.midiOutMsg(0x90, 0x02, 0x74, 0x00)
    device.midiOutMsg(0x90, 0x02, 0x75, 0x00)
    device.midiOutMsg(0x90, 0x02, 0x76, 0x00)
    device.midiOutMsg(0x90, 0x02, 0x77, 0x00)

    device.midiOutMsg(0xB0, 0x02, 0x25, 0x00)
    device.midiOutMsg(0xB0, 0x02, 0x26, 0x00)
    device.midiOutMsg(0xB0, 0x02, 0x27, 0x00)
    device.midiOutMsg(0xB0, 0x02, 0x28, 0x00)
    device.midiOutMsg(0xB0, 0x02, 0x29, 0x00)
    device.midiOutMsg(0xB0, 0x02, 0x2A, 0x00)
    device.midiOutMsg(0xB0, 0x02, 0x2B, 0x00)
    device.midiOutMsg(0xB0, 0x02, 0x2C, 0x00)
    device.midiOutMsg(0xB0, 0x02, 0x2D, 0x00)
