from TDStoreTools import StorageManager
import TDFunctions as TDF

class ScenePlayer:
	def __init__(self, ownerComp):
		self.ownerComp = ownerComp

	# called with key q
	def ControlTetraederOnly(self):
		print("ControlTetraederOnly")
		
		# op.Clipgun_flash_collective_tetraeder.par.Mute = 0
		# op.Clipgun_flash_collective_sticks.par.Mute = 1

		op.Clipgun_collective.par.Mutezone0 = 0   # tetraeder unmuted
		op.Clipgun_collective.par.Mutezone1 = 1   # sticks muted
		
	# called with key w
	def ControlSticksOnly(self):
		print("ControlSticksOnly")
		# op.Clipgun_flash_collective_tetraeder.par.Mute = 1
		# op.Clipgun_flash_collective_sticks.par.Mute = 0

		op.Clipgun_collective.par.Mutezone0 = 1   # tetraeder muted
		op.Clipgun_collective.par.Mutezone1 = 0   # sticks unmuted
		
	# called with key e
	def ControlAll(self):
		print("ControlAll")
		op.Clipgun_collective.par.Mutezone0 = 0   # tetraeder unmuted
		op.Clipgun_collective.par.Mutezone1 = 0   # sticks unmuted