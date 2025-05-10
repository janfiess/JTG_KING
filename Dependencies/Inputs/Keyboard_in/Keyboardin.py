from TDStoreTools import StorageManager
import TDFunctions as TDF



class Keyboardin:

	def __init__(self, ownerComp):
		return
		
	def Triggeraction(self, key):

		print(f"key: {key}")
		# parent().par.Prevosckey = parent().par.Latestosckey
		# parent().par.Latestosckey = key

		# wähle Lats aus

		if key == "kq":
			op.ScenePlayer.op('simulator/collective1/selectlats1').click()
		elif key == "kw":
			op.ScenePlayer.op('simulator/collective1/selectlats2').click()
		if key == "ke":
			op.ScenePlayer.op('simulator/collective1/selectlats3').click()



		# spiele animationen ab
		# Collective
		
		return


		if key == "kr":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
			op.ScenePlayer.Anim_collective_ramp("left")
		if key == "kt":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
			op.ScenePlayer.Anim_collective_ramp("right")

		if key == "kz":
			# op.Clipgun_flash_individual.op("video2").Play()
			op.ScenePlayer.Anim_collective_flashAll(3)

			op.Clipgun_flash_collective_tetraeder.Play(3, "synchronous") # 3 -> white, "synchronous" -> next start pos: alle synchron



		# Individual


		if key == "ka":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
			op.Clipgun_flash_individual.Play(0, 0)    # arg1: red,  arg2: id (0-7) des Tetraeders

		if key == "ks":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
			op.Clipgun_flash_individual.Play(0, 1)    # arg1: red,  arg2: id (0-7) des Tetraeders

		if key == "kd":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
			op.Clipgun_flash_individual.Play(0, 2)    # arg1: red,  arg2: id (0-7) des Tetraeders

		if key == "kf":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
			op.Clipgun_flash_individual.Play(0, 3)    # arg1: red,  arg2: id (0-7) des Tetraeders

		if key == "kg":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
			op.Clipgun_flash_individual.Play(0, 4)    # arg1: red,  arg2: id (0-7) des Tetraeders

		if key == "kh":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
			op.Clipgun_flash_individual.Play(0, 5)    # arg1: red,  arg2: id (0-7) des Tetraeders

		if key == "kj":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
			op.Clipgun_flash_individual.Play(0, 6)    # arg1: red,  arg2: id (0-7) des Tetraeders

		if key == "kk":
			# op.Clipgun_flash_individual.op("video2").Play()
			print(f"key: {key}")
			op.Clipgun_flash_individual.Play(0, 7)    # arg1: red,  arg2: id (0-7) des Tetraeders





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
			