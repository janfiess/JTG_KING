from TDStoreTools import StorageManager
import TDFunctions as TDF

class Buttonbase:
	def __init__(self, ownerComp):
		return

	def Play(self):
		print("button base")
		moviefile = op("../moviefilein_rgb")
		parent(2).par.Latestkeypressed = parent().name
		
		moviefile.par.cuepoint = 0
		moviefile.par.cuepulse.pulse()
		moviefile.par.play = 1
