from firebase import firebase

import logging
import traceback
import math
import time
import json

module_logger = logging.getLogger('myApp')

class Database_Manager:

	def __init__(self):
		self.apiKey = ""
		self.credentials = ""
		self.dbURL = "https://final-year-project-f08b2.firebaseio.com/"
		self.firebase = firebase.FirebaseApplication(self.dbURL, None)
		self.dataDir = 'Output_data'
		self.fileType = '.txt'
	
	def get(self):
		try:
			result = self.firebase.get('/cards', None)
			myJSON = json.dumps(result)
			timestamp = str(math.trunc(time.time()))
			with open(self.dataDir + '/FirebaseCards_' + timestamp +self.fileType, mode='a+') as localfile:     
				localfile.write(myJSON)	 
		except :
			print('Error fetching data from firebase: ' + str(traceback.format_exc()))
		
	def push(self, data):
		try:
			ref = self.firebase.post('/cards',data)
		except :
			print('Error pushing data to firebase: '+ str(traceback.format_exc()))
	
	def put(self, id, data):
		try:
			self.firebase.put('/cards',id,data)		
		except :
			print('Error putting data to firebase: '+ str(traceback.format_exc()))

			
	def delete(self, id):
		try:		
			self.firebase.delete('/cards', id)
		except :
			print('Error deleting data from firebase: ' + str(traceback.format_exc()))		
