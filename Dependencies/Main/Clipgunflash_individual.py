from TDStoreTools import StorageManager
import TDFunctions as TDF
import random

class Clipgunflash:

	def __init__(self, ownerComp):
		
		self.table_player_placement = op("null_player_placement")

		# [variation][color]
		self.clips = [
			
			# variation 0
			[
				"video1", # red
				"video2", # green
				"video3", # blue
				"video4"  # weiss
			],
			# variation 1
			[
				"video5", # red
				"video6", # green
				"video7", # blue
				"video8"  # weiss
			],
			# variation 1
			[
				"video9", # red
				"video10", # green
				"video11", # blue
				"video12"  # weiss
			]
		]


	def OnParamChanged(self, par):
		return
		

	# wird aufgerufen in op.OSC_in. 
	def Play(self, color, tetraeder_id):
		# print("[Clipgun_flash_individual]: spiele individual clip von ableton")

		# Es wird abwechselnd ein anderer Player verwendet, damit sich die Video bei schneller Interaktion nicht unterbrechen, sondern überlagern.
		parent().par.Nextplayerid = (parent().par.Nextplayerid + 1) % 2
		next_player_id = parent().par.Nextplayerid

		variation = random.randint(0, len(self.clips) - 1)
		# variation = 0

		# color = int(parent(2).par.Nextcolor)
		tetraeder_id = int(tetraeder_id)

		# [variation][color]
		myClip = self.clips[variation][color]
		# print(f"individual: myClip: {myClip}")

		# spiele clip an der richtigen Position ab anhand von tetraeder_id (8 Tetraeder = 8 Positionen)
		next_player_id = parent().par.Nextplayerid
		op(f"placement_rgb{next_player_id}").par.tx = self.table_player_placement[tetraeder_id, 0]
		op(f"placement_rgb{next_player_id}").par.ty = self.table_player_placement[tetraeder_id, 1]
		op(f"placement_cwww{next_player_id}").par.tx = self.table_player_placement[tetraeder_id, 0]
		op(f"placement_cwww{next_player_id}").par.ty = self.table_player_placement[tetraeder_id, 1]
		op("clips").op(myClip).Play()    # triggert Script innerhalb der einzelnen Video-Button-Container
