# name=Launchkey 49 MK3

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

btnCaptureMidi = 0x4A
btnQuantise = 0x4B
btnClick = 0x4C
btnUndo = 0x4D

btnPlay = 0x73
btnStop = 0x74
btnRecord = 0x75
btnPattern = 0x76


class TMain():
    def __init__(self):
        return

    def OnInit(self):
        print('Initialisation complete')

    def OnDeInit(self):
        print('Deinitialisation complete')

    def OnMidiMsg(self, event):
        event.handled = False
        print('--------------------------------')
        print(event.midiId, event.midiChan, event.data1, event.data2, event.sysex)
        event.handled = False
        
        # If the event is unhandled, print out what it is:
        if event.handled is False:
            print("Unhandled event: {:X} {:X} {:2X} {}".format(event.status, event.data1, event.data2,  internal.EventNameT[(event.status - 0x80) // 16] + ': '+  utils.GetNoteName(event.data1)))


Main = TMain()

def OnInit():
    Main.OnInit()

def OnDeInit():
    Main.OnDeInit()

def OnMidiMsg(event):
    Main.OnMidiMsg(event)
    
    
    
    
