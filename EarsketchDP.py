#		python code
#		script_name:
#
#		author:
#		description:
#

from earsketch import *

init()
setTempo(140)
 
fitMedia(RD_TRAP_BELLLEAD_1, 1, 1, 7) 
setTempo(140)
fitMedia(RD_ELECTRO_DRUMROLLBREAK_1, 3, 3, 7)
setEffect(3, VOLUME, GAIN, -60, 1, 3, 7)
fitMedia(DUBSTEP_PERCDRUM_006, 1, 7, 15)
setTempo(145)
fitMedia(ELECTRO_DRUM_MAIN_LOOPPART_001, 2, 6, 15)

finish()