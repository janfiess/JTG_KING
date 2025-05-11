from TDStoreTools import StorageManager
import TDFunctions as TDF

class Clipgun:

	def __init__(self, ownerComp):
		self.moviefilein = op("moviefilein")



	def OnParamChanged(self, par):
		if par.name == "Loop":
			self.moviefilein.par.play = 1
			self.moviefilein.par.cuepoint = 0
		if par.name == "Resetspeed":
			parent().par.Speed = 1


