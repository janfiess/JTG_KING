from TDStoreTools import StorageManager
import TDFunctions as TDF

class MQTTin:
	def __init__(self, ownerComp):
		self.topic_prefix = parent().par.Topicprefix
		
	def OnParamChanged(self, par):
		
		if par.name == "Active":
			if par == 1:
				op.Logger.Info("[MQTT_in]: Activated MQTT")
			elif par == 0:
				op.Logger.Info("[MQTT_in]: Deactivated MQTT")
			
		elif par.name == "Reconnect":
			op.Logger.Info(f"[MQTT_in]: Reconnecting to MQTT broker")
			
		elif par.name == "Broker":
			op.Logger.Info(f"[MQTT_in]: Selected MQTT brokerchanged to: {par}")

		elif par.name == "Topicprefix":
			op.Logger.Info(f"[MQTT_in]: mqtt_topic_prefix changed to: {par}")
			op.MQTT_in.par.Topicprefix = str(par)



	def Process_mqtt_action(self, topic, payload, retained):
		if len(payload):
			payload = payload.decode("utf-8")   # convert byte to string
			if topic != f"{op.MQTT_in.par.Topicprefix}radwinkel":
				op.Logger.Info(f"[MQTT_in]: topic: {topic}   |   payload: {payload}")

					
			op.MQTT_in.par.Prevmqtttopic = op.MQTT_in.par.Latestmqtttopic
			op.MQTT_in.par.Prevmqttpayload = op.MQTT_in.par.Latestmqttpayload
			op.MQTT_in.par.Latestmqtttopic = topic
			op.MQTT_in.par.Latestmqttpayload = payload
			op.MQTT_in.par.Latestmqtttime = absTime.seconds
			# op.Logger.MQTT_in(topic, payload)
			self.Triggeraction(topic, payload)

	def Triggeraction(self, topic, payload):

		if(topic == self.topic_prefix + "scene_done"): 
			return

		# HTTP in

		elif (topic == self.topic_prefix + "httpin/active"): # retained
			if op.HTTP_in.par.Active is not None:	
				if int(op.HTTP_in.par.Active) != int(payload):
					op.HTTP_in.par.Active = int(payload)				
		
		# Display_out
		
		elif(topic == self.topic_prefix + "display"):
			if(payload == "reactivate"):
				op.Display_out.par.Reactivatedisplay.pulse()
				
		elif(topic == self.topic_prefix + "display/black"):
			op.Display_out.par.Displayblack = int(payload)

		elif(topic == self.topic_prefix + "display/brightness"): # retained
			payload = round(float(payload), 2)
			if op.Display_out.par.Brightness is not None:	
				if round(float(op.Display_out.par.Brightness),2) != payload:
					op.Display_out.par.Brightness = payload
					op.Display_out.par.Nextbrightness = payload




