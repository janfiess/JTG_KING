from TDStoreTools import StorageManager
import TDFunctions as TDF

class Startup:
	def __init__(self, ownerComp):
		return
		
	def Step1(self):

		# activate mqtts
		op.MQTT_in.par.Active = 1
	
		
	def Step2(self):
		# ui.openTextport()
		op.Clipgun_base.op('video1/triggerbutton').click()
	
	def Step3(self):
		# op.Logger.Info("[Startup]: startup part 3")
		# disable black display and mute audio if enabled for any reason
		# op.Display_out.par.Displayblack = 0 
		return
		
	def OnParamChanged(self, par):
		#if par.name == "Timelineactive":
			#me.time.play = int(par)
		return