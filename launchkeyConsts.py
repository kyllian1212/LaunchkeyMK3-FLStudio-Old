'''
consts for the launchkey mk3!
used this as a reference: 
https://fael-downloads-prod.focusrite.com/customer/prod/s3fs-public/downloads/Launchkey_MK3_Programmers_Reference.pdf
'''

'''
colors:
only the first 64 colors are written here im lazy for the rest LOL
colors ref for the first 64 colors (except black & white): light > normal > dark > darker
'''
#black & white
COLOR_OFF = 0x00
COLOR_DARKER = 0x01
COLOR_DARK = 0x02
COLOR_WHITE = 0x03

#red
COLOR_LIGHTRED = 0x04
COLOR_RED = 0x05
COLOR_DARKRED = 0x06
COLOR_DARKERRED = 0x07

#orange
COLOR_LIGHTORANGE = 0x08
COLOR_ORANGE = 0x09
COLOR_DARKORANGE = 0x0A
COLOR_DARKERORANGE = 0x0B #substitute to brown

#yellow
COLOR_LIGHTORANGE = 0x0C
COLOR_ORANGE = 0x0D
COLOR_DARKORANGE = 0x0E
COLOR_DARKERORANGE = 0x0F 

#lime green
COLOR_LIGHTLIMEGREEN = 0x10
COLOR_LIMEGREEN = 0x11
COLOR_DARKLIMEGREEN = 0x12
COLOR_DARKERLIMEGREEN = 0x13

#green
COLOR_LIGHTGREEN = 0x14
COLOR_GREEN = 0x15
COLOR_DARKGREEN = 0x16
COLOR_DARKERGREEN = 0x17

#blue green
COLOR_LIGHTBLUEGREEN = 0x18
COLOR_BLUEGREEN = 0x19
COLOR_DARKBLUEGREEN = 0x1A
COLOR_DARKERBLUEGREEN = 0x1B

#aqua
COLOR_LIGHTAQUA = 0x1C
COLOR_AQUA = 0x1D
COLOR_DARKAQUA = 0x1E
COLOR_DARKERAQUA = 0x1F 

#cyan
COLOR_LIGHTCYAN = 0x20
COLOR_CYAN = 0x21
COLOR_DARKCYAN = 0x22
COLOR_DARKERCYAN = 0x23

#turquoise
COLOR_LIGHTTURQUOISE = 0x24
COLOR_TURQUOISE = 0x25
COLOR_DARKTURQUOISE = 0x26
COLOR_DARKERTURQUOISE = 0x27

#azure
COLOR_LIGHTAZURE = 0x28
COLOR_AZURE = 0x29
COLOR_DARKAZURE = 0x2A
COLOR_DARKERAZURE = 0x2B

#blue
COLOR_LIGHTBLUE = 0x2C
COLOR_BLUE = 0x2D
COLOR_DARKBLUE = 0x2E
COLOR_DARKERBLUE = 0x2F

#cobalt
COLOR_LIGHTCOBALT = 0x30
COLOR_COBALT = 0x31
COLOR_DARKCOBALT = 0x32
COLOR_DARKERCOBALT = 0x33

#purple
COLOR_LIGHTPURPLE = 0x34
COLOR_PURPLE = 0x35
COLOR_DARKPURPLE = 0x36
COLOR_DARKERPURPLE = 0x37

#pink
COLOR_LIGHTPINK = 0x38
COLOR_PINK = 0x39
COLOR_DARKPINK = 0x3A
COLOR_DARKERPINK = 0x3B

#alt colors
COLOR_PUREORANGE = 0x38
COLOR_YELLOWORANGE = 0x39
COLOR_YELLOWGREEN = 0x3A
COLOR_APPLEGREEN = 0x3B

'''
color mode:
corresponds to the way it's flashing
'''
COLORMODE_STATIONARY = 0x00
COLORMODE_FLASHING = 0x01 #broken? i never got it to work
COLORMODE_PULSING = 0x02
COLORMODE_STATIONARYGRAYSCALE = 0x0F #CC associated controls only

'''
pads & buttons location:
pads 1-8 is top row of pads, excluding up arrow (top left) and right arrow (top right)
pads 9-16 is bottom row of pads, excluding down arrow (bottom left) and stop/solo/mute (bottom right)
fader buttons 1-8 is fader buttons (except arm/select)

this applies to SESSION MODE only
'''
#pads (note on)
PAD_1 = 0x60
PAD_2 = 0x61
PAD_3 = 0x62
PAD_4 = 0x63
PAD_5 = 0x64
PAD_6 = 0x65
PAD_7 = 0x66
PAD_8 = 0x67
PAD_9 = 0x70
PAD_10 = 0x71
PAD_11 = 0x72
PAD_12 = 0x73
PAD_13 = 0x74
PAD_14 = 0x75
PAD_15 = 0x76
PAD_16 = 0x77

#pads (cc)
PAD_RIGHTARROW = 0x68
PAD_STOPSOLOMUTE = 0x69
PAD_UPARROW = 0x6A
PAD_DOWNARROW = 0x6B

#fader buttons (cc)
FADERBUTTON_1 = 0x25
FADERBUTTON_2 = 0x26
FADERBUTTON_3 = 0x27
FADERBUTTON_4 = 0x28
FADERBUTTON_5 = 0x29
FADERBUTTON_6 = 0x2A
FADERBUTTON_7 = 0x2B
FADERBUTTON_8 = 0x2C
FADERBUTTON_ARMSELECT = 0x2D

#general buttons (cc)
BTN_SHIFT = 0x6C
BTN_TRACKLEFT = 0x67 #they swapped both track left and track right prob accidentally lol
BTN_TRACKRIGHT = 0x66
BTN_CAPTUREMIDI = 0x4A
BTN_QUANTISE = 0x4B
BTN_CLICK = 0x4C
BTN_UNDO = 0x4D
BTN_PLAY = 0x73
BTN_STOP = 0x74
BTN_RECORD = 0x75
BTN_PATTERN = 0x76


'''
sysex messages:
allows to show stuff on the 16x2 chars screen

how to show messages: 
device.midiOutSysex([consts.SYSEX_BEGIN_TOP/consts.SYSEX_BEGIN_BOTTOM] + str.encode([your message here]) + consts.SYSEX_END)
'''
SYSEX_BEGIN_TOP = bytes([0xF0, 0x00, 0x20, 0x29, 0x02, 0x0F, 0x04, 0])
SYSEX_BEGIN_BOTTOM = bytes([0xF0, 0x00, 0x20, 0x29, 0x02, 0x0F, 0x04, 1])
SYSEX_END = bytes([0xF7])
SYSEX_CLEAR = bytes([0xF0, 0x00, 0x20, 0x29, 0x02, 0x0F, 0x06, 0xF7])