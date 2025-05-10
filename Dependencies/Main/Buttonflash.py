from TDStoreTools import StorageManager
import TDFunctions as TDF

class Buttonflash:
	def __init__(self, ownerComp):
		return

	# wird von innerhalb der einzelnen Video-Button-Container 
	# und von Play_individual_clip() in op.Clipgun_flash_individual getriggert
	
	def Play(self):
		next_player_id = parent(3).par.Nextplayerid
		clipname = parent().name
		print(f"clip to play: {clipname}")
		
		parent(3).pars(f"Latestkeypressed{next_player_id}")[0].val = clipname
		
		moviefile_cwww_zone0 = parent(3).op(f"moviefilein_cwww_{next_player_id}")
		#print(f"moviefilein{next_player_id}")
		self.startVideo(moviefile_cwww_zone0)
		
		moviefile_rgb_zone0 = parent(3).op(f"moviefilein_rgb_{next_player_id}")
		self.startVideo(moviefile_rgb_zone0)

		moviefile_cwww_zone1 = parent(3).op(f"moviefilein_cwww_{next_player_id}")
		self.startVideo(moviefile_cwww_zone1)
		
		moviefile_rgb_zone1 = parent(3).op(f"moviefilein_rgb_{next_player_id}")
		self.startVideo(moviefile_rgb_zone1)

	
	def startVideo(self, moviefile):
		moviefile.par.cuepoint = 0
		moviefile.par.cuepulse.pulse()
		moviefile.par.play = 1