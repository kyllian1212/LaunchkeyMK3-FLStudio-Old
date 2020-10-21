# name=Launchkey 49 MK3

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
import launchkeyConsts as lkc

#python imports
import sys
import time

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

Main = TMain()

def OnInit():
    Main.OnInit()

def OnDeInit():
    Main.OnDeInit()

def OnMidiMsg(event):
    Main.OnMidiMsg(event)
    
    
    
    
