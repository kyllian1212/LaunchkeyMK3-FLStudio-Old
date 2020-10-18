# name=Launchkey 49 MK3 Midi

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
import sys
import internal
import consts

btnCaptureMidi = 0x4A
btnQuantise = 0x4B
btnClick = 0x4C
btnUndo = 0x4D

btnPlay = 0x73
btnStop = 0x74
btnRecord = 0x75
btnPattern = 0x76

class TMain:
    def __init__(self):
        return
    
    def OnInit(self):
        if device.isAssigned() == 0:
            print('DEVICE PORT NOT ASSIGNED. EXITING.')
            sys.exit(0)
        print('init completed')
        device.midiOutMsg(0x9F, 0x0F, 0x0C, 0x7F)
        
        device.midiOutSysex(consts.SYSEX_BEGIN_TOP + str.encode(ui.getProgTitle()) + consts.SYSEX_END)
        device.midiOutSysex(consts.SYSEX_BEGIN_BOTTOM + str.encode(ui.getVersion()) + consts.SYSEX_END)

    def OnDeInit(self):
        if device.isAssigned() == 0:
            print('DEVICE PORT NOT ASSIGNED. EXITING.')
            sys.exit(0)
        print('deinit completed')
        device.midiOutMsg(0x9F, 0x0F, 0x0C, 0x00)

    def OnMidiMsg(self, event):
        event.handled = False
        print('--------------------------------')
        print('midi id:', event.midiId, '| midi status:', event.status, '| midi channel:', event.midiChan, 
        '| midi data1:', event.data1, '| midi data2:', event.data2, '| midi sysex:', event.sysex)
        if event.midiId == midi.MIDI_CONTROLCHANGE:
            if event.data2 > 0:
                #capture midi
                if event.data1 == btnCaptureMidi:
                    print('capture midi')
                #quantise
                if event.data1 == btnQuantise:
                    print('quantise')
                #click
                elif event.data1 == btnClick:
                    print(general.getUseMetronome())
                #undo
                elif event.data1 == btnUndo:
                    general.undo()
                #play/pause
                elif event.data1 == btnPlay:
                    transport.start()
                #stop
                elif event.data1 == btnStop:
                    transport.stop()
                #record
                elif event.data1 == btnRecord:
                    transport.record()
                #pattern/song
                elif event.data1 == btnPattern:
                    transport.setLoopMode()
                    
        #end of btn press
        event.handled = True

    def OnRefresh(self, flags):
        print('refresh')

    def OnDirtyMixerTrack(self, index):
        mixerTrackNumberStr = str(mixer.trackNumber())
        mixerTrackName = mixer.getTrackName(mixer.trackNumber())
        mixerTrackInfo = mixerTrackNumberStr + " - " + mixerTrackName

        mixerTrackVolume = str("{:.1f}".format(mixer.getTrackVolume(mixer.trackNumber())*125))
        mixerTrackPan = str("{:.0f}".format(mixer.getTrackPan(mixer.trackNumber())*100))
        mixerTrackSettings = "V" + mixerTrackVolume + "% | P" + mixerTrackPan + "%"

        device.midiOutSysex(consts.SYSEX_BEGIN_TOP + str.encode(mixerTrackInfo) + consts.SYSEX_END)
        device.midiOutSysex(consts.SYSEX_BEGIN_BOTTOM + str.encode(mixerTrackSettings) + consts.SYSEX_END)


Main = TMain()

def OnInit():
    Main.OnInit()

def OnDeInit():
    Main.OnDeInit()

def OnMidiMsg(event):
    Main.OnMidiMsg(event)

def onRefresh(flags):
    Main.OnRefresh(flags)

def OnDirtyMixerTrack(index):
    Main.OnDirtyMixerTrack(index)

def clearSysexMessage():
    device.midiOutSysex(consts.SYSEX_CLEAR)
