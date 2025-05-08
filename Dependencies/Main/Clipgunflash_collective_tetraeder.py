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
				"video4"  # white
			],
			# variation 1
			[
				"video1", # red
				"video2", # green
				"video3", # blue
				"video4"  # white
			],

			# variation 2
			[
				"video1", # red
				"video2", # green
				"video3", # blue
				"video4"  # white
			],

			# variation 3: overall flash "synchronous" -> wird abgespielt, wenn K: /Tetraeder/All V: 1 kommt
			[
				"video9", # red
				"video10", # green
				"video11", # blue
				"video12"  # white
			]
		]

	def OnParamChanged(self, par):
		return
		
	# called in Oscin.py or Keyboardi.py: op.Clipgun_flash_collective_tetraeder.Play(0, "left")
	def Play(self, color, startpos):   # color: (0 -> red or 2 -> blue),   next start pos: "left" or "right"
		# print("[Clipgun_collective]: spiele collective clip")
		if parent().par.Mute == 1:	
			return
		
		# Es wird abwechselnd ein anderer Player verwendet, damit sich die Video bei schneller Interaktion nicht unterbrechen, sondern überlagern.
		parent().par.Nextplayerid = (parent().par.Nextplayerid + 1) % 2
		variation = random.randint(0, len(self.clips) - 2)
		# variation = 0

		if startpos == "synchronous":
			variation = 3

		# [variation][color]
		myClip = self.clips[variation][color]
		# print(f"myClip: {myClip}")
		# print(f"variation: {variation},   color: {color}, collective: myClip: {myClip}")
		parent().par.Startpos = startpos
		
		# spiele clip im richtigen Player (links beginnend oder horiz gespiegelt rechts beginnend) anhand von start_position
		op(myClip).Play()
