from TDStoreTools import StorageManager
import TDFunctions as TDF

class Buttonbase:
	def __init__(self, ownerComp):
		return

	def Play(self):
		print("button base")
		moviefile = op.Clipgun_base.op("moviefilein_rgb")
		op.Clipgun_base.par.Latestkeypressed = parent().name
		
		moviefile.par.cuepoint = 0
		moviefile.par.cuepulse.pulse()
		moviefile.par.play = 1
