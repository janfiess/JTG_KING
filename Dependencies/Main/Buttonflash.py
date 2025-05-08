from TDStoreTools import StorageManager
import TDFunctions as TDF

class Buttonflash:
	def __init__(self, ownerComp):
		return

	# wird von innerhalb der einzelnen Video-Button-Container 
	# und von Play_individual_clip() in op.Clipgun_flash_individual getriggert
	
	def Play(self):
		next_player_id = parent(2).par.Nextplayerid
		clipname = parent().name
		
		parent(2).pars(f"Latestkeypressed{next_player_id}")[0].val = clipname
		
		moviefile_cwww = parent(2).op(f"moviefilein_cwww_{next_player_id}")
		#print(f"moviefilein{next_player_id}")
		moviefile_cwww.par.cuepoint = 0
		moviefile_cwww.par.cuepulse.pulse()
		moviefile_cwww.par.play = 1
		
		moviefile_rgb = parent(2).op(f"moviefilein_rgb_{next_player_id}")
		moviefile_rgb.par.cuepoint = 0
		moviefile_rgb.par.cuepulse.pulse()
		moviefile_rgb.par.play = 1

