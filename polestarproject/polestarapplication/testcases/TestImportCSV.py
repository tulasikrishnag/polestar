import unittest
from django.test import Client
from ImportData import ImportData
from polestarapplication.constant import constant
from polestarapplication.models import ShipPositionDetails,ShipDetail
"""
Test class will cover the unit test scenarios of import functionality.
"""
class TestImportCSV(unittest.TestCase):
	ImportData=None;

	
	#Setup method instanitated before testcase execution,create the instance
	def setUp(self):
		self.ImportData= ImportData()
		self.client=Client()
		print('setup')

	#Testcase to clean the data from the database and load the position data from the csv to DB.
	def test_load_position_data(self):
		print("Position Data Removal");
		self.ImportData.deleteimporteddata(ShipPositionDetails);
		print("Position Data Load from Testcase");
		self.ImportData.importpositiondata();
		self.assertEqual(ShipPositionDetails.objects.count(),constant.NUMBER_OF_POS_ROWS_TO_IMPORT)


#Testcase to clean the data from the database and load the position data from the csv to DB.
	
	def test_load_ship_data(self):
		print("Ship Data Removal");
		self.ImportData.deleteimporteddata(ShipDetail);
		print("Ship Data Load from Testcase");
		self.ImportData.importshipdata();
		self.assertEqual(ShipDetail.objects.count(),constant.NUMBER_OF_SHIP_ROWS_TO_IMPORT)

	def test_api_get_ship_details(self):
		print(constant.GET_SHIP_DETAILS_API_END_POINT)
		response = self.client.get(constant.GET_SHIP_DETAILS_API_END_POINT)
		#print(response.content)
		#self.assertEqual(response.status_code, 200)
		#self.assertNotEqual("[]", response.content)

	def test_api_get_position_details(self):
		#print(constant.GET_SHIP_POSITION_API_END_POINT+constant.IMO)
		response = self.client.get(constant.GET_SHIP_POSITION_API_END_POINT+constant.IMO)
		#print(response.content)
		#self.assertEqual(response.status_code, 200)
		#self.assertNotEqual("[]", response.content)


	def build_test_suite():
		test_suite= unittest.TestSuite()
		test_suite.addTest(self.ImportDataCSV('test_load_ship_data'))
		test_suite.addTest(self.ImportDataCSV('test_load_position_data'))
		return test_suite


if __name__ == '__main__':
	unittest.main()





