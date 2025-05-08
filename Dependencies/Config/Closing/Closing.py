from TDStoreTools import StorageManager
import TDFunctions as TDF

import os

class Closing:
	def __init__(self, ownerComp):
		return
	
	# executed in op("execute_save_tox")
	def SaveAllTox(self):
		op.Logger.Debug("Closing -- Save all .tox")
		# Clear all project paths
		project.paths.clear()
		try:
			op.local.unstore('metadata')
		except Exception as e:
			# do nothing
			pass
	
		# Check all tox if they are external and save only if changed
	    
		for ext_op in parent.Project.findChildren(parExpr="*'.tox'"):
			if ext_op.dirty:
				a = ui.messageBox('Saving modified Tox', ext_op.name, buttons=['Cancel','Ok'])
				if bool(a): # if pressed ok
					ext_op.save(ext_op.par.externaltox.eval())
					debug("Saving tox:", ext_op.name)
		
	def ShutDownPC(self):
		op.Logger.Info("[Closing]: Force shutdown PC in 10s")
		os.system('shutdown -s -t 10')
		
	def Stop_ShutDownPC(self):
		op.Logger.Info("[Closing]: Stop shutdown")
		os.system('shutdown -a')
		
	# executed in op("execute_save_tox")
	#def MakeDisplaysBlack(self):
		# display black before ending
		#op.Display_out.par.Displayblack = 1 
		#op.ScenePlayer.par.Fadebrightness = 0
		#op.ScenePlayer.par.Pause = 1
		#op.ScenePlayer.par.Isplaying = 0
		
	def OnParamChanged(self, par):
		#if par.name == Timelineactive
			#me.time.play = int(par)
		return
