from TDStoreTools import StorageManager
import TDFunctions as TDF



class Oscin:

	def __init__(self, ownerComp):
		return
		
	def Triggeraction(self, key, value):
		parent().par.Prevosckey = parent().par.Latestosckey
		parent().par.Latestosckey = key

		if key == "/testosc":
			print("Test erfolgreich")
			op.Clipgun_flash_individual.op("video2").Play()
		
		# Message kommt vom Max
		# FLASH COLLECTIVE: Video wird über alle Tetraeder abgespielt, aber nur, wenn individual mode eingestellt ist.
		elif key == "/Tetraeder/Collective":
			if parent().par.Prevosckey != parent().par.Latestosckey:
				self.turn_sustain_anims_black()
			if value == "red":
				op.Clipgun_flash_collective_tetraeder.Play(0, "left")   # 0 -> red, "left" -> next start pos
			elif value == "blue":
				op.Clipgun_flash_collective_tetraeder.Play(2, "right")   # 2 -> blue, "right" -> next start pos

		elif key == "/Tetraeder/All":
			if int(value) == 1:
				op.Clipgun_flash_collective_tetraeder.Play(3, "synchronous") # 3 -> white, "synchronous" -> next start pos: alle synchron
			
			if int(value) == 0:
				self.turn_sustain_anims_black()

		# Message kommt von Max (Audio), zuvor hat Max ein Signal vom Buzzer erhalten
		# FLASH INDIVIDUAL: einzelne Tetraeder erleuchten
		elif key == "/Tetraeder/Index/Red":
			if parent().par.Prevosckey != parent().par.Latestosckey:
				self.turn_sustain_anims_black()
			op.Clipgun_flash_individual.Play(0, value)    # 0 -> red,  value ist id (0-7) des Tetraeders
		elif key == "/Tetraeder/Index/Blue":
			if parent().par.Prevosckey != parent().par.Latestosckey:
				self.turn_sustain_anims_black()
			op.Clipgun_flash_individual.Play(2, value)    # 2 -> blue,  value ist id (0-7) des Tetraeders

		
		# Message kommt von Max (Audio), zuvor hat Max ein Signal vom Buzzer erhalten
		# SUSTAIN: einzelne Tetraeder gehen an und toggeln dann zwischen rot und blau
		elif key == "/Tetraeder/Sustain/Red":
			op.Clipgun_sustain.Play(0, value)    # 0 -> red,  value ist id (0-7) des Tetraeders
		elif key == "/Tetraeder/Sustain/Blue":
			op.Clipgun_sustain.Play(2, value)    # 2 -> blue,  value ist id (0-7) des Tetraeders

		# Base Anim
		elif key == "/Tetraeder/Baseanim":
			op.Clipgun_base.Play(value)  # value ist video ID
		
			

	def turn_sustain_anims_black(self):
		for tetraeder_id in range(8):
			op.Clipgun_sustain.Play(4, tetraeder_id)    # 4 -> black,  value ist id (0-7) des Tetraeders
	
	def OnParamChanged(self, par):
		if par.name == "Active":
			op.MQTT_out.SendMQTT_retained( op.MQTT_in.par.Topicprefix + "udpin/active", int(par))
			op.Logger.Debug(f"[OSC_in]: OSC IN ative: {int(par)}")
			