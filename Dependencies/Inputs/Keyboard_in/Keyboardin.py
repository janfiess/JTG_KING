from TDStoreTools import StorageManager
import TDFunctions as TDF



class Keyboardin:

	def __init__(self, ownerComp):
		return
		
	def Triggeraction(self, key):
		# parent().par.Prevosckey = parent().par.Latestosckey
		# parent().par.Latestosckey = key

		if key == "kq":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
			op.Clipgun_flash_collective_tetraeder.Play(0, "left")
			op.ScenePlayer.ControlTetraederOnly()
		elif key == "kw":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
			op.ScenePlayer.ControlSticksOnly()
		if key == "ke":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
			op.ScenePlayer.ControlAll()
		if key == "kr":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
		if key == "kt":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
		if key == "kz":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
		if key == "ku":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
		if key == "ki":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
		if key == "ko":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
		if key == "kp":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
		if key == "ka":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
			
		if key == "ks":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
		if key == "kd":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
		if key == "kf":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
		if key == "kg":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
		if key == "kh":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
		if key == "kj":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
		if key == "kk":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
		if key == "kl":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
		if key == "ky":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
		
		if key == "kx":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
		if key == "kc":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
		if key == "kv":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
		if key == "kb":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
		if key == "kn":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
		if key == "km":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
		

		
		

		
			

	def turn_sustain_anims_black(self):
		for tetraeder_id in range(8):
			op.Clipgun_sustain.Play(4, tetraeder_id)    # 4 -> black,  value ist id (0-7) des Tetraeders
	
	def OnParamChanged(self, par):
		if par.name == "Active":
			op.MQTT_out.SendMQTT_retained( op.MQTT_in.par.Topicprefix + "udpin/active", int(par))
			op.Logger.Debug(f"[OSC_in]: OSC IN ative: {int(par)}")
			