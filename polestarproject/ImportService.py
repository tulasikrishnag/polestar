import csv
import datetime
import os
from django.utils.timezone import make_aware
from django.db import transaction
from polestarapplication.models import ShipPositionDetails, ShipDetail

"""Import data class designed to group the import csv functionality
"""


class ImportService:
    """
     Description:This method is responsible to process the position.csv reads the header 
     process the data and store into the database.
     Params: self
    """

    def importpositiondata(self):
        try:
            position_obj_list = []
            with open(os.getcwd() + '/positions.csv') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    # To resolve the blocker UTC_TZ removing the timezone +00 from the date string.
                    # All the rows has the same value hence removing it assuming no impact
                    # Using aware function to intact the date with timezone
                    formatteddate = datetime.datetime.strptime(
                    	row['position_dt_tm'][:-3], '%Y-%m-%d %H:%M:%S')
                    position_obj_list.append(ShipPositionDetails(
                        imo=row['imo'],
                        position_dt_tm=make_aware(formatteddate),
                        latitude=row['latitude'],
                        longitude=row['longitude']
                    ))
                # For better performance used bulk_create to sent the list of objects once to DB and commit.
                ShipPositionDetails.objects.bulk_create(position_obj_list)

        except IntegrityError:
            print("Data IntegrityError caused while processing the data.")
            raise

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
            with open(os.getcwd() + '/ships.csv') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    ship_obj_model = ShipDetail(
                        name=row['name'],
                        imo=row['imo']
                    )
                    ship_obj_model.save()

        except IntegrityError:
            print("Data IntegrityError caused while processing the data.")
            raise

        except:
            print("Error occured while processing ship csv data")
            raise

    """
    Description:This method is responsible to remove all the rows from the model
    Params: self, datamodel 
    """

    def deleteimporteddata(self, model):
        try:
            model_obj = model.objects.all();
            model_obj.delete();
        except:
            print("Error occured while removing the data from the table")
            raise




