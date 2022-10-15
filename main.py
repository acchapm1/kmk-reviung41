### START
print("Starting")

from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.hid import HIDModes
from kmk.modules.capsword import CapsWord
from kmk.modules.combos import Combos, Chord, Sequence
from kmk.modules.oneshot import OneShot
from kmk.modules.mouse_keys import MouseKeys
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.tapdance import TapDance
from kmk.handlers.sequences import compile_unicode_string_sequences as cuss
from kmk.handlers.sequences import simple_key_sequence, send_string
from kmk.extensions.peg_oled_display import Oled,OledDisplayMode,OledReactionType,OledData

import supervisor

print("All Imports finished")

### DEF BARE KEYBOARD
keyboard = KMKKeyboard()

### Module Configuration
## TAPDANCE Init
tapdance = TapDance()
tapdance.tap_time = 500
keyboard.modules.append(tapdance)

## ONESHOT Init
oneshot = OneShot()
keyboard.modules.append(oneshot)

## COMBO Init
combos = Combos()
keyboard.modules.append(combos)

## ModTap Init
modtap = ModTap()
modtap.tap_time=300
keyboard.modules.append(modtap)

## CapsWord Init
caps_word=CapsWord()
# change inactivity timeout
caps_word=CapsWord(timeout=5000) 
# add additional ignored keys
caps_word.keys_ignored.append(KC.COMMA) 
keyboard.modules.append(caps_word)

## MediaKeys Init
media = MediaKeys()
keyboard.extensions.append(media)

## MouseKeys init
mkeys = MouseKeys()
keyboard.modules.append(mkeys)

## LAYERS Init
keyboard.modules.append(Layers())

print("Modules Loaded")

oled_ext = Oled(
    OledData(
        corner_one={0:OledReactionType.STATIC,1:["Layer  -"]},
        corner_two={0:OledReactionType.LAYER,1:["1","2","3","4","5"]},
        corner_three={0:OledReactionType.LAYER,1:["Base","Numbers","Symbols","Mouse","Functions"]},
        corner_four={0:OledReactionType.LAYER,1:["QWERTY","Vim Nav","{}[]()","Control","+ Extras"]}
        ),
        toDisplay=OledDisplayMode.TXT,flip=False)
keyboard.extensions.append(oled_ext)

# codeblock
## Combos
"""
mvp combos
(q,e) -> esc
(h,k) -> :
(e,t) -> ~
"""
combos.combos = [
    Chord((KC.Q, KC.E), KC.ESC),
    Chord((KC.H, KC.K), KC.COLN),
    Chord((KC.E, KC.T), KC.TILD)
]

# media keys
MUTE = KC.MUTE
VUP = KC.VOLU
VDOWN = KC.VOLD
PLAY = KC.MPLY
# end media keys

# mouse aliases
LBTN = KC.MB_LMB
MBTN = KC.MB_MMB
RBTN = KC.MB_RMB
WUP = KC.MW_UP
WDN = KC.MW_DN
MLEFT = KC.MS_LT
MRIGHT = KC.MS_RT
MUP = KC.MS_UP
MDN = KC.MS_DN
## end mouse aliases

## modtap
# KC.MT(KC.TAP, KC.HOLD, prefer_hold=True, tap_interrupted=False, tap_time=None)
TABTILD = KC.MT(KC.TAB, KC.TILD)
BACKPIPE = KC.MT(KC.BSPC, KC.PIPE)
ZSYM = KC.MT(KC.Z, KC.MO(2))
LSYM = KC.MT(KC.L, KC.MO(2))
XMOUSE = KC.MT(KC.X, KC.MO(3))
CFUNC = KC.MT(KC.C, KC.MO(4))
FNAV  = KC.MT(KC.F, KC.MO(1))
aA = KC.MT(KC.A, KC.LSFT(KC.A))
## End modtap

## Send Strings
Agave = simple_key_sequence((KC.S,KC.S,KC.H,KC.SPC,KC.A,KC.G,KC.A,KC.V,KC.E,KC.ENT,))
Sol = simple_key_sequence((KC.S,KC.S,KC.H,KC.SPC,KC.S,KC.O,KC.L,KC.ENT,))
ADMIN = simple_key_sequence((KC.S,KC.S,KC.H,KC.SPC,KC.A,KC.D,KC.M,KC.I,KC.N,KC.ENT,))
BRCS = simple_key_sequence((KC.LBRC,KC.RBRC,KC.LEFT))
PRNS = simple_key_sequence((KC.LPRN,KC.RPRN,KC.LEFT))
CBRS = simple_key_sequence((KC.LCBR,KC.RCBR,KC.LEFT))

emoticons = cuss({
    'CRAZY_EYES': r'🤪',
    'HAND_WAVE': r'👋',
    })
## End Send Strings

## Tap Dance
QTCW = KC.TD(KC.QUOTE, KC.CW, KC.MT(KC.GRV, send_string(':sui'), prefer_hold=False),)
## End Tap Dance

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO
LOWER = KC.MO(1)
RAISE = KC.MO(2)
MOUSE = KC.MO(4)
RSFT_ENT = KC.MT(KC.ENT, KC.RSFT)
RSFT_SPC = KC.MT(KC.SPC, KC.RSFT)
RAY = KC.LALT(KC.SPC)

## Layer key names
BASE = KC.TO(0)
NUM = KC.TO(1)
SYMB = KC.TO(2)
MOUSE = KC.TO(3)
FUNC = KC.TO(4)

print("Keys Initiated")
# codeblock
# Keymap
keyboard.keymap = [
    [  #QWERTY Layer 0
        TABTILD,   KC.Q,      KC.W,  KC.E,    KC.R,    KC.T,                       KC.Y,    KC.U,    KC.I,    KC.O,   KC.P,    BACKPIPE,
        KC.LCTL,   aA,        KC.S,  KC.D,    FNAV,    KC.G,                       KC.H,    KC.J,    KC.K,    LSYM,   KC.SCLN, QTCW,
        KC.LSFT,   ZSYM,    XMOUSE, CFUNC,    KC.V,    KC.B,                       KC.N,    KC.M,    KC.COMM, KC.DOT, KC.SLSH, KC.RSFT,
                                               RAY,  KC.ENT,       KC.LGUI,        KC.SPC,   NUM,
    ], 
    [  #NUM_NAV Layer 1
        KC.ESC,   KC.N1,   KC.N2,   KC.N3,   KC.N4,    KC.N5,                      KC.N6,   KC.N7,  KC.N8,   KC.N9,   KC.N0, KC.MINUS,
        KC.LCTL, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,    PLAY,                      KC.LEFT, KC.DOWN, KC.UP,   KC.RIGHT, XXXXXXX, XXXXXXX,
        KC.TRNS, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                      XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, RSFT_SPC,
                                              BASE,   KC.ENT,      KC.LGUI,        KC.SPC,   SYMB,
    ],
    [  #SYMB Layer 2 
        KC.ESC, KC.EXLM,   KC.AT, KC.HASH,  KC.DLR,  KC.PERC,                      KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN, KC.BSPC,
        KC.LCTL, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                      KC.MINS, KC.PLUS, KC.LCBR, KC.RCBR, KC.GRV,  KC.GRV,
        KC.LSFT, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                      KC.UNDS, KC.EQL,  KC.LBRC, KC.RBRC, KC.BSLS, KC.TILD,
                                               BASE,  KC.ENT,      KC.LGUI,        KC.SPC,  MOUSE,
    ],
    [  #MOUSE Layer 3
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                      XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, VUP,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,     WUP,                      MLEFT,   MDN,     MUP,     MRIGHT,  XXXXXXX, VDOWN,
        XXXXXXX, XXXXXXX, XXXXXXX, LBTN,    RBTN   ,     WDN,                      XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, MUTE,
                                               BASE,  KC.ENT,       KC.LGUI,       KC.SPC,   FUNC,
    ],
    [  #FUNC Layer 4
        KC.F1,     KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,                      KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                      XXXXXXX, PRNS,    BRCS,    CBRS,    XXXXXXX, XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                      XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
                                               BASE,  KC.ENT,       KC.LGUI,       KC.SPC,  BASE,
    ]
]
# Keymap

print("Good to Go!")

# Debug
# keyboard.debug_enabled = True

## Main Loop
if __name__ == '__main__':
    keyboard.go()
