from TDStoreTools import StorageManager
import TDFunctions as TDF

class Clipguncollective:

	def __init__(self, ownerComp):

		self.clips = {
			# variation 0
			"ramp_right": ["video1", "video2", "video3", "video4", "video5"], # r, g, b, cw, ww
			"ramp_left": ["video4", "video2", "video3", "video4", "video5"],
			"flashAll": ["video1", "video2", "video3", "video4", "video5"],
			"solid": ["video1", "video2", "video3", "video4", "video5"]
		}
		return

	def OnParamChanged(self, par):
		return
		
	def Huhu(self):
		print("huhu")
		
	# called in Oscin.py or Keyboardi.py: op.Clipgun_flash_collective_tetraeder.Play(0, "left")
	def Play(self, anim, color):   # color: (0 -> red or 2 -> blue),   next start pos: "left" or "right"
		print("[Clipgun_collective]: spiele collective clip")
		if parent().par.Mutezone0 == 1 and parent().par.Mutezone1 == 1:
			return
		
		# Es wird abwechselnd ein anderer Player verwendet, damit sich die Video bei schneller Interaktion nicht unterbrechen, sondern überlagern.
		parent().par.Nextplayerid = (parent().par.Nextplayerid + 1) % 2

		myClip = self.clips[anim][color]
		print(f"myClip: {myClip}")
		op("clips").op(myClip).Play()
