# name=Launchkey 49 MK3

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
import programConsts as prog

#python imports
import sys
import time

#variables
programMode = prog.MODE_OFF

class TMain():
    def __init__(self):
        return

    def OnInit(self):
        global programMode
        print('Initialisation complete')
        programMode = prog.MODE_MIXER
        

    def OnDeInit(self):
        print('Deinitialisation complete')

    def OnMidiMsg(self, event):
        event.handled = False
        print('--------------------------------')
        print(event.midiId, event.midiChan, event.data1, event.data2, event.sysex)

    '''    
    def OnUpdateMeters(self):
        m.mixerPeakInterface()
    '''

Main = TMain()

def OnInit():
    Main.OnInit()

def OnDeInit():
    Main.OnDeInit()

def OnMidiMsg(event):
    Main.OnMidiMsg(event)

'''
def OnUpdateMeters():
    Main.OnUpdateMeters()
'''
    
    
