import csv
import datetime
import os
from django.utils.timezone import make_aware
from polestarapplication.models import ShipPositionDetails,ShipDetail

"""Import data class designed to group the import csv functionality
"""
class ImportData:
	"""
	 Description:This method is responsible to process the position.csv reads the header data 
	 process the data and store into the database.
     Params: self
	"""
	
	def importpositiondata(self):
		try:
			with open(os.getcwd()+'/positions.csv') as csvfile:
				reader = csv.DictReader(csvfile)
				for row in reader:
				#To resolve the blocker UTC_TZ removing the timezone +00 from the date string.
				#All the rows has the same value hence removing it assuming no impact
					formatteddate = datetime.datetime.strptime(row['position_dt_tm'][:-3], '%Y-%m-%d %H:%M:%S')
					position_obj_model = ShipPositionDetails(
					imo = row['imo'], 
					position_dt_tm = make_aware(formatteddate),
					latitude = row['latitude'], 
					longitude = row['longitude']
					)
					position_obj_model.save()
		except:
			print("Error occured while processing position csv data")
			raise
	"""
	 Description:This method is responsible to process the ships.csv reads the header data 
	 process the data and store into the database.
     Params: self
	"""
	
	def importshipdata(self):
		try:
			with open(os.getcwd()+'/ships.csv') as csvfile:
				reader = csv.DictReader(csvfile)
				for row in reader:
					ship_obj_model = ShipDetail(
						name = row['name'],
						imo = row['imo']
						)
					ship_obj_model.save()
		except:
			print("Error occured while processing ship csv data")
			raise
	"""
	Description:This method is responsible to remove all the rows from the model
	Params: self  
	"""
	def deleteimporteddata(self , model):
		model_obj = model.objects.all();
		model_obj.delete();


				

