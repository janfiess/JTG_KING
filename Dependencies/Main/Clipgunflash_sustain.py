from TDStoreTools import StorageManager
import TDFunctions as TDF
import random

class Clipgunflash:

	def __init__(self, ownerComp):

		# [variation][color]
		self.clips = [
			
			# variation 0
			[
				"video1", # red
				"video2", # green
				"video3", # blue
				"video4", # weiss
				"video9"  # black
			],
			# variation 1
			[
				"video1", # red
				"video2", # green
				"video3", # blue
				"video4", # weiss
				"video9"  # black
			]
		]


	def OnParamChanged(self, par):
		return
		
	
	# wird aufgerufen in op.OSC_in: op.Clipgun_sustain.Play(2, value) # 0: rot, 2: blau, value: Tetraeder 0 - 7
	def Play(self, color, tetraeder_id):
		# print("[Clipgun_sustain]: spiele individual and loop it until interrupt")

		# variation = parent().par.Nextvariation
		variation = random.randint(0, len(self.clips) - 1)
		tetraeder_id = int(tetraeder_id)

		# [variation][color]
		myClip_container = self.clips[variation][color]
		myClipfile = op(myClip_container).par.Filergb
		myMoviePlayer = op(f"moviefilein_rgb_{tetraeder_id}")
		myMoviePlayer.par.file = myClipfile
		myMoviePlayer.par.cuepulse.pulse()
		# print(f"sustain: myClipfile: {myClipfile}")
