from TDStoreTools import StorageManager
import TDFunctions as TDF



class Midiin:

	def __init__(self, ownerComp):
		return
		
	def Triggeraction(self, key):
		# parent().par.Prevosckey = parent().par.Latestosckey
		# parent().par.Latestosckey = key
		print(f"key: {key}")

		# Zonenwahl

		if key == "ch1n33":
			op.ScenePlayer.op('simulator/collective1/selectlats1').click()
		elif key == "ch1n34":
			op.ScenePlayer.op('simulator/collective1/selectlats2').click()
		elif key == "ch1n35":
			op.ScenePlayer.op('simulator/collective1/selectlats3').click()

		# Base / Background anims

		elif key == "ch1n40":
			op.Clipgun_base.op("clips/video10").par.Trigger.pulse()

		# Foreground anims: collective flashes

		elif key == "ch1n25":
			op.Clipgun_collective.op("clips/video5").par.Trigger.pulse()
		elif key == "ch1n26":
			op.Clipgun_collective.op("clips/video1").par.Trigger.pulse()
		elif key == "ch1n27":
			op.Clipgun_collective.op("clips/video2").par.Trigger.pulse()
		elif key == "ch1n28":
			op.Clipgun_collective.op("clips/video3").par.Trigger.pulse()

		elif key == "ch1n29":
			op.Clipgun_collective.op("clips/video8").par.Trigger.pulse()
		elif key == "ch1n30":
			op.Clipgun_collective.op("clips/video9").par.Trigger.pulse()
		elif key == "ch1n31":
			op.Clipgun_collective.op("clips/video6").par.Trigger.pulse()
		elif key == "ch1n32":
			op.Clipgun_collective.op("clips/video10").par.Trigger.pulse()

		# Foreground anims: Individual flashes

		elif key == "ch1n1":
			op.Clipgun_flash_individual.op("UI/selectlats33").click()
		elif key == "ch1n2":
			op.Clipgun_flash_individual.op("UI/selectlats34").click()
		elif key == "ch1n3":
			op.Clipgun_flash_individual.op("UI/selectlats35").click()
		elif key == "ch1n4":
			op.Clipgun_flash_individual.op("UI/selectlats36").click()
		elif key == "ch1n5":
			op.Clipgun_flash_individual.op("UI/selectlats37").click()
		elif key == "ch1n6":
			op.Clipgun_flash_individual.op("UI/selectlats38").click()
		elif key == "ch1n7":
			op.Clipgun_flash_individual.op("UI/selectlats39").click()
		elif key == "ch1n8":
			op.Clipgun_flash_individual.op("UI/selectlats40").click()

		elif key == "ch1n9":
			op.Clipgun_flash_individual.op("UI/selectlats25").click()
		elif key == "ch1n10":
			op.Clipgun_flash_individual.op("UI/selectlats26").click()
		elif key == "ch1n11":
			op.Clipgun_flash_individual.op("UI/selectlats27").click()
		elif key == "ch1n12":
			op.Clipgun_flash_individual.op("UI/selectlats28").click()
		elif key == "ch1n13":
			op.Clipgun_flash_individual.op("UI/selectlats29").click()
		elif key == "ch1n14":
			op.Clipgun_flash_individual.op("UI/selectlats30").click()
		elif key == "ch1n15":
			op.Clipgun_flash_individual.op("UI/selectlats31").click()
		elif key == "ch1n16":
			op.Clipgun_flash_individual.op("UI/selectlats32").click()

		elif key == "ch1n17":
			op.Clipgun_flash_individual.op("UI/selectlats9").click()
		elif key == "ch1n18":
			op.Clipgun_flash_individual.op("UI/selectlats10").click()
		elif key == "ch1n19":
			op.Clipgun_flash_individual.op("UI/selectlats11").click()
		elif key == "ch1n20":
			op.Clipgun_flash_individual.op("UI/selectlats12").click()
		elif key == "ch1n21":
			op.Clipgun_flash_individual.op("UI/selectlats13").click()
		elif key == "ch1n22":
			op.Clipgun_flash_individual.op("UI/selectlats14").click()
		elif key == "ch1n23":
			op.Clipgun_flash_individual.op("UI/selectlats15").click()
		elif key == "ch1n24":
			op.Clipgun_flash_individual.op("UI/selectlats16").click()


		
			

	def turn_sustain_anims_black(self):
		for tetraeder_id in range(8):
			op.Clipgun_sustain.Play(4, tetraeder_id)    # 4 -> black,  value ist id (0-7) des Tetraeders
	
	def OnParamChanged(self, par):
		if par.name == "Active":
			op.MQTT_out.SendMQTT_retained( op.MQTT_in.par.Topicprefix + "udpin/active", int(par))
			op.Logger.Debug(f"[OSC_in]: OSC IN ative: {int(par)}")
			