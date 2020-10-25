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
import programConsts as prog

#python imports
import sys
import time

mixerTrackLaunchKeyIndex = 1
setting = 0

def mixerUpdate(index):
    global mixerTrackLaunchKeyIndex
    if mixer.trackNumber() > 118 and mixer.trackNumber() < 127:
        mixerTrackLaunchKeyIndex = 118
    elif not mixer.trackNumber() == 0:
        mixerTrackLaunchKeyIndex = mixer.trackNumber()
    

    mixerTrackNumberStr = str(mixer.trackNumber())
    mixerTrackName = mixer.getTrackName(mixer.trackNumber())
    mixerTrackInfo = mixerTrackNumberStr + " - " + mixerTrackName

    time.sleep(0.05) #fixes the issue with the wrong settings being sent to the launchkey

    mixerTrackVolume = str("{:.1f}".format(mixer.getTrackVolume(mixer.trackNumber())*125))
    mixerTrackPan = str("{:.0f}".format(mixer.getTrackPan(mixer.trackNumber())*100))
    mixerTrackSettings = "V" + mixerTrackVolume + "% | P" + mixerTrackPan + "%"

    s.sendMessageTopRow(mixerTrackInfo)
    s.sendMessageBottomRow(mixerTrackSettings)

def mixerInterface():
    global mixerTrackLaunchKeyIndex

    #lights up the arrows + stop buttons
    l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[16], lkc.COLOR_DARKER)
    l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[17], lkc.COLOR_DARKER)
    l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[18], lkc.COLOR_DARKER)
    l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[19], lkc.COLOR_DARKERRED)


    if not mixer.isTrackMuted(0):
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[28], lkc.COLOR_DARKER)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[28], lkc.COLOR_OFF)

    for i in range(1,9):
        if not mixer.isTrackMuted(mixerTrackLaunchKeyIndex+(i-1)):
            l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[20+(i-1)], lkc.COLOR_DARKERLIMEGREEN)
        else:
            l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[20+(i-1)], lkc.COLOR_OFF)

def mixerPeakInterface():
    global mixerTrackLaunchKeyIndex
    global setting 

    if setting == mc.MIXERMODE_8TRACKS:
        mixerPeakInterface8Tracks(mixerTrackLaunchKeyIndex)
    elif setting == mc.MIXERMODE_1TRACK:
        mixerPeakInterface1Track(mixerTrackLaunchKeyIndex)
    elif setting == mc.MIXERMODE_1MASTER:
        mixerPeakInterface1Master()
            
def mixerPeakInterface8Tracks(index):
    for i in range(0, 8):
        if mixer.getTrackPeaks(index+i, 0) >= 0 and mixer.getTrackPeaks(index+i, 0) <= 0.149:
            l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[i], lkc.COLOR_OFF)
        elif mixer.getTrackPeaks(index+i, 0) >= 0.150 and mixer.getTrackPeaks(index+i, 0) <= 0.374:
            l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[i], lkc.COLOR_DARKERGREEN)
        elif mixer.getTrackPeaks(index+i, 0) >= 0.375 and mixer.getTrackPeaks(index+i, 0) <= 0.499:
            l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[i], lkc.COLOR_DARKGREEN)
        elif mixer.getTrackPeaks(index+i, 0) >= 0.500 and mixer.getTrackPeaks(index+i, 0) <= 0.624:
            l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[i], lkc.COLOR_GREEN)
        elif mixer.getTrackPeaks(index+i, 0) >= 0.625 and mixer.getTrackPeaks(index+i, 0) <= 0.749:
            l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[i], lkc.COLOR_YELLOW)
        elif mixer.getTrackPeaks(index+i, 0) >= 0.750 and mixer.getTrackPeaks(index+i, 0) <= 0.874:
            l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[i], lkc.COLOR_ORANGE)
        elif mixer.getTrackPeaks(index+i, 0) >= 0.875 and mixer.getTrackPeaks(index+i, 0) <= 0.999:
            l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[i], lkc.COLOR_PUREORANGE)
        elif mixer.getTrackPeaks(index+i, 0) > 1:
            l.lightPad(lkc.STATE_PULSING, list(lk.lightingDict)[i], lkc.COLOR_RED)

        if mixer.getTrackPeaks(index+i, 1) >= 0 and mixer.getTrackPeaks(index+i, 1) <= 0.149:
            l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[i+8], lkc.COLOR_OFF)
        elif mixer.getTrackPeaks(index+i, 1) >= 0.150 and mixer.getTrackPeaks(index+i, 1) <= 0.374:
            l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[i+8], lkc.COLOR_DARKERGREEN)
        elif mixer.getTrackPeaks(index+i, 1) >= 0.375 and mixer.getTrackPeaks(index+i, 1) <= 0.499:
            l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[i+8], lkc.COLOR_DARKGREEN)
        elif mixer.getTrackPeaks(index+i, 1) >= 0.500 and mixer.getTrackPeaks(index+i, 1) <= 0.624:
            l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[i+8], lkc.COLOR_GREEN)
        elif mixer.getTrackPeaks(index+i, 1) >= 0.625 and mixer.getTrackPeaks(index+i, 1) <= 0.749:
            l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[i+8], lkc.COLOR_YELLOW)
        elif mixer.getTrackPeaks(index+i, 1) >= 0.750 and mixer.getTrackPeaks(index+i, 1) <= 0.874:
            l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[i+8], lkc.COLOR_ORANGE)
        elif mixer.getTrackPeaks(index+i, 1) >= 0.875 and mixer.getTrackPeaks(index+i, 1) <= 0.999:
            l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[i+8], lkc.COLOR_PUREORANGE)
        elif mixer.getTrackPeaks(index+i, 1) > 1:
            l.lightPad(lkc.STATE_PULSING, list(lk.lightingDict)[i+8], lkc.COLOR_RED)
    
def mixerPeakInterface1Track(index):
    if mixer.getTrackPeaks(index, 0) >= 0.150:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[0], lkc.COLOR_DARKERGREEN)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[0], lkc.COLOR_OFF)
    if mixer.getTrackPeaks(index, 0) >= 0.250:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[1], lkc.COLOR_DARKERGREEN)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[1], lkc.COLOR_OFF)
    if mixer.getTrackPeaks(index, 0) >= 0.375:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[2], lkc.COLOR_DARKGREEN)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[2], lkc.COLOR_OFF)
    if mixer.getTrackPeaks(index, 0) >= 0.500:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[3], lkc.COLOR_GREEN)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[3], lkc.COLOR_OFF)
    if mixer.getTrackPeaks(index, 0) >= 0.625:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[4], lkc.COLOR_YELLOW)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[4], lkc.COLOR_OFF)
    if mixer.getTrackPeaks(index, 0) >= 0.750:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[5], lkc.COLOR_ORANGE)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[5], lkc.COLOR_OFF)   
    if mixer.getTrackPeaks(index, 0) >= 0.875:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[6], lkc.COLOR_PUREORANGE)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[6], lkc.COLOR_OFF) 
    if mixer.getTrackPeaks(index, 0) > 1:
        l.lightPad(lkc.STATE_PULSING, list(lk.lightingDict)[7], lkc.COLOR_RED)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[7], lkc.COLOR_OFF)

    if mixer.getTrackPeaks(index, 1) >= 0.150:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[8], lkc.COLOR_DARKERGREEN)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[8], lkc.COLOR_OFF)
    if mixer.getTrackPeaks(index, 1) >= 0.250:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[9], lkc.COLOR_DARKERGREEN)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[9], lkc.COLOR_OFF)
    if mixer.getTrackPeaks(index, 1) >= 0.375:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[10], lkc.COLOR_DARKGREEN)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[10], lkc.COLOR_OFF)
    if mixer.getTrackPeaks(index, 1) >= 0.500:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[11], lkc.COLOR_GREEN)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[11], lkc.COLOR_OFF)
    if mixer.getTrackPeaks(index, 1) >= 0.625:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[12], lkc.COLOR_YELLOW)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[12], lkc.COLOR_OFF)
    if mixer.getTrackPeaks(index, 1) >= 0.750:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[13], lkc.COLOR_ORANGE)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[13], lkc.COLOR_OFF)
    if mixer.getTrackPeaks(index, 1) >= 0.875:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[14], lkc.COLOR_PUREORANGE)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[14], lkc.COLOR_OFF)
    if mixer.getTrackPeaks(index, 1) > 1:
        l.lightPad(lkc.STATE_PULSING, list(lk.lightingDict)[15], lkc.COLOR_RED)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[15], lkc.COLOR_OFF)

def mixerPeakInterface1Master():
    if mixer.getTrackPeaks(0, 0) >= 0.150:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[0], lkc.COLOR_DARKERGREEN)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[0], lkc.COLOR_OFF)
    if mixer.getTrackPeaks(0, 0) >= 0.250:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[1], lkc.COLOR_DARKERGREEN)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[1], lkc.COLOR_OFF)
    if mixer.getTrackPeaks(0, 0) >= 0.375:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[2], lkc.COLOR_DARKGREEN)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[2], lkc.COLOR_OFF)
    if mixer.getTrackPeaks(0, 0) >= 0.500:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[3], lkc.COLOR_GREEN)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[3], lkc.COLOR_OFF)
    if mixer.getTrackPeaks(0, 0) >= 0.625:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[4], lkc.COLOR_YELLOW)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[4], lkc.COLOR_OFF)
    if mixer.getTrackPeaks(0, 0) >= 0.750:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[5], lkc.COLOR_ORANGE)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[5], lkc.COLOR_OFF)   
    if mixer.getTrackPeaks(0, 0) >= 0.875:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[6], lkc.COLOR_PUREORANGE)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[6], lkc.COLOR_OFF) 
    if mixer.getTrackPeaks(0, 0) > 1:
        l.lightPad(lkc.STATE_PULSING, list(lk.lightingDict)[7], lkc.COLOR_RED)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[7], lkc.COLOR_OFF)

    if mixer.getTrackPeaks(0, 1) >= 0.150:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[8], lkc.COLOR_DARKERGREEN)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[8], lkc.COLOR_OFF)
    if mixer.getTrackPeaks(0, 1) >= 0.250:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[9], lkc.COLOR_DARKERGREEN)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[9], lkc.COLOR_OFF)
    if mixer.getTrackPeaks(0, 1) >= 0.375:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[10], lkc.COLOR_DARKGREEN)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[10], lkc.COLOR_OFF)
    if mixer.getTrackPeaks(0, 1) >= 0.500:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[11], lkc.COLOR_GREEN)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[11], lkc.COLOR_OFF)
    if mixer.getTrackPeaks(0, 1) >= 0.625:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[12], lkc.COLOR_YELLOW)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[12], lkc.COLOR_OFF)
    if mixer.getTrackPeaks(0, 1) >= 0.750:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[13], lkc.COLOR_ORANGE)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[13], lkc.COLOR_OFF)
    if mixer.getTrackPeaks(0, 1) >= 0.875:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[14], lkc.COLOR_PUREORANGE)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[14], lkc.COLOR_OFF)
    if mixer.getTrackPeaks(0, 1) > 1:
        l.lightPad(lkc.STATE_PULSING, list(lk.lightingDict)[15], lkc.COLOR_RED)
    else:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[15], lkc.COLOR_OFF)

def mixerBtnPress(event):
    global mixerTrackLaunchKeyIndex

    #move up selected track
    if event.data1 == 106 and event.data2 == 127:
        if mixerTrackLaunchKeyIndex == 118:
            s.sendMessageTopRow("You cannot go")
            s.sendMessageBottomRow("above track 125")
        else:
            mixerTrackLaunchKeyIndex = mixerTrackLaunchKeyIndex + 1
            s.sendMessageTopRow("Selection:")
            s.sendMessageBottomRow("Tracks " + str(mixerTrackLaunchKeyIndex) + " - " + str(mixerTrackLaunchKeyIndex+7))
            mixerInterface()

        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[16], lkc.COLOR_WHITE)
    elif event.data1 == 106 and event.data2 == 0:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[16], lkc.COLOR_DARKER)

    #move down selected track
    if event.data1 == 107 and event.data2 == 127:
        if mixerTrackLaunchKeyIndex == 1:
            s.sendMessageTopRow("You cannot go to")
            s.sendMessageBottomRow("track 0")
        else:
            mixerTrackLaunchKeyIndex = mixerTrackLaunchKeyIndex - 1
            s.sendMessageTopRow("Selection:")
            s.sendMessageBottomRow("Tracks " + str(mixerTrackLaunchKeyIndex) + " - " + str(mixerTrackLaunchKeyIndex+7))
            mixerInterface()
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[17], lkc.COLOR_WHITE)
    elif event.data1 == 107 and event.data2 == 0:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[17], lkc.COLOR_DARKER)


    #mute master
    if event.data1 == 45 and event.data2 == 127:
        mixer.muteTrack(0)

    #mute a track
    for i in range(0, 8):
        if event.data1 == 37+i and event.data2 == 127:
            mixer.muteTrack(mixerTrackLaunchKeyIndex+i)
    
    #quit program menu (will be quit mode when implemented)
    if event.data1 == 105 and event.status == 176 and event.data2 == 127:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[19], lkc.COLOR_RED)
        s.sendMessageTopRow("Quit program")
        s.sendMessageBottomRow("not implemented")
    elif event.data1 == 105 and event.status == 176 and event.data2 == 0:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[19], lkc.COLOR_DARKERRED)
    
    #settings menu
    if event.data1 == 104 and event.status == 176 and event.data2 == 127:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[18], lkc.COLOR_WHITE)
    elif event.data1 == 104 and event.status == 176 and event.data2 == 0:
        l.lightPad(lkc.STATE_STATIONARY, list(lk.lightingDict)[18], lkc.COLOR_DARKER)