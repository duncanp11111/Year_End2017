#		python code
#		script_name:
#
#		author:
#		description:
#

from earsketch import *

init()
setTempo(100)
BASS = HIPHOP_BASSSUB_003
PIANO = YG_ELECTRO_ELECTRIC_PIANO_2

BEAT2 = "-00000+0000-00-"

def Intro():
  fitMedia(BASS, 1, 1, 49.5)
  setEffect(1, VOLUME, GAIN, 0, 1, 0, 49.5)
  fitMedia(PIANO, 4, 1, 50)
  
  fitMedia(DUNCANP11_ROCKY_BALBOA_S_INSPIRATIONAL_SPEECH_TO_HIS_SON, 3, 1, 15)
  DRUMBASS = Y48_DRUMPAD_1
  setEffect(2, VOLUME, GAIN, -60, 3, -30, 15)
  
  for measure in range (1, 50):
    makeBeat(DRUMBASS, 2, measure, BEAT2)
  for measure in range (1, 30):
    fitMedia(TECHNO_WHITENOISESFX_002, 3, 13, 15)

def Mid():
  fitMedia(RD_CINEMATIC_SCORE_MAINDRUM_5, 5, 15, 40)
  fitMedia(RD_RNB_808MAINBEAT_5, 6, 17, 38)

def End():
  fitMedia(TECHNO_WHITENOISESFX_003, 7, 40, 42)
  fitMedia(Y05_CYMBAL_SWELL_1, 8, 49, 50)

Intro()
Mid()
End()

finish()
