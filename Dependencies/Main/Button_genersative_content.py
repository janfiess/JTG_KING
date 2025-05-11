from TDStoreTools import StorageManager
import TDFunctions as TDF

class Buttonflash:
	def __init__(self, ownerComp):
		return

	# wird von innerhalb der einzelnen Video-Button-Container 
	# und von Play_individual_clip() in op.Clipgun_flash_individual getriggert
	
	def Play(self):
		print("Button_generative_content")
		next_player_id = parent(3).par.Nextplayerid
		clipname = parent().name


		# print(f"clip to play: {clipname}")
		
		op.Clipgun_collective.pars(f"Latestkeypressed{next_player_id}")[0].val = clipname
		
		if op.Clipgun_collective.par.Mutezone0 == 0: #if tetraeder not muted

			# print("tetraeder not muted")
	
			moviefile_cwww_zone0 = op.Clipgun_collective.op(f"moviefilein_zone0_cwww_{int(next_player_id)}")
			# print(f"moviefile_cwww_zone0: {moviefile_cwww_zone0}")
			self.startVideo(moviefile_cwww_zone0)
			
			moviefile_rgb_zone0 = op.Clipgun_collective.op(f"moviefilein_zone0_rgb_{int(next_player_id)}")
			# print(f"moviefile_rgb_zone0: {moviefile_rgb_zone0}")
			self.startVideo(moviefile_rgb_zone0)

		if op.Clipgun_collective.par.Mutezone1 == 0: #if sticks not muted

			# print("sticks not muted")

			moviefile_cwww_zone1 = op.Clipgun_collective.op(f"moviefilein_zone1_cwww_{int(next_player_id)}")
			self.startVideo(moviefile_cwww_zone1)
			
			moviefile_rgb_zone1 = op.Clipgun_collective.op(f"moviefilein_zone1_rgb_{int(next_player_id)}")
			self.startVideo(moviefile_rgb_zone1)

	
	def startVideo(self, moviefile):
		target = op.Pixelmapping.op('get_color_overlay/select_generative_overlay')
		content =  op.Clipgun_collective.op(f"clips/{parent().name}/null_content")
		# print(f"target: {target}")
		# print(f"content: {content}")
		target.par.top = content