from TDStoreTools import StorageManager
import TDFunctions as TDF

class ScenePlayer:
	def __init__(self, ownerComp):
		self.ownerComp = ownerComp

	# called with key q
	def ControlTetraederOnly(self):
		print("ControlTetraederOnly")
		
		op.Clipgun_flash_collective_tetraeder.par.Mute = 0
		op.Clipgun_flash_collective_sticks.par.Mute = 1
		
	# called with key w
	def ControlSticksOnly(self):
		print("ControlSticksOnly")
		op.Clipgun_flash_collective_tetraeder.par.Mute = 1
		op.Clipgun_flash_collective_sticks.par.Mute = 0
		
	# called with key e
	def ControlAll(self):
		print("ControlAll")
		op.Clipgun_flash_collective_tetraeder.par.Mute = 0
		op.Clipgun_flash_collective_sticks.par.Mute = 0


	# Anims

	def Anim_collective_ramp(self, startpos):
		print("Anim_lr_collective")
		op.Clipgun_flash_collective_tetraeder.Play(0, startpos)
		op.Clipgun_flash_collective_sticks.Play(0, startpos)

	def Anim_collective_flashAll(self, color):	
		print("Anim_flashAll_collective")
		op.Clipgun_flash_collective_tetraeder.Play(color, "synchronous")
		op.Clipgun_flash_collective_sticks.Play(color, "synchronous")