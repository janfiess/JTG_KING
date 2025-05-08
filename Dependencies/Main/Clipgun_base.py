from TDStoreTools import StorageManager
import TDFunctions as TDF

class Clipgun:

	def __init__(self, ownerComp):
		self.moviefilein = op("moviefilein")


		self.clips = [
			"video1", # standard noise
			"video2", # stripes
			"video3", # x
			"video4"  # y
		]


	def OnParamChanged(self, par):
		if par.name == "Loop":
			self.moviefilein.par.play = 1
			self.moviefilein.par.cuepoint = 0
		if par.name == "Resetspeed":
			parent().par.Speed = 1

	def Pause(self):
		self.moviefile.par.play = 0
		
	# called in Oscin.py
	def Play(self, videonr):   # color: (0 -> red or 2 -> blue),   next start pos: "left" or "right"
		# print("[Baseanim]")

		myClip = self.clips[int(videonr)]
		op(myClip).Play()