import unittest
from django.test import Client
from ImportService import ImportService
from polestarapplication.constant import constant
from polestarapplication.models import ShipPositionDetails, ShipDetail
"""
Test class will cover the unit test scenarios of import functionality.
"""
# Since the application does not allow the user input, testcase execution preserve the data
# Eventhough unique constraints enabled, testcase first remove the data and insert.
# To retain the test execution order provided the testname followed by sequential number.


class TestImportService(unittest.TestCase):
    ImportData = None

    """Setup method instanitated before testcase execution,create the instance"""

    def setUp(self):
        self.ImportService = ImportService()
        self.client = Client()

    """Testcase to clean the data from the database and load the position data from the csv to DB."""

    def test1(self):
        self.ImportService.deleteimporteddata(ShipDetail)
        print("Ship Data Removed Successfuly")
        self.ImportService.importshipdata()
        self.assertEqual(ShipDetail.objects.count(),
                         constant.NUMBER_OF_SHIP_ROWS_TO_IMPORT)
        print("Ship Data Load Successfuly from Testcase")

    """Testcase to clean the data from the database and load the position data from the csv to DB."""

    def test2(self):
        self.ImportService.deleteimporteddata(ShipPositionDetails)
        print("Position Data Removed Successfuly")
        self.ImportService.importpositiondata()
        self.assertEqual(ShipPositionDetails.objects.count(),
                         constant.NUMBER_OF_POS_ROWS_TO_IMPORT)
        print("Position Data Load Successfuly from Testcase")
    """Testcase to validate get api/ship end point"""

    def test3(self):
        response = self.client.get(constant.GET_SHIP_DETAILS_API_END_POINT)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual("[]", response.content)
        print("Get ship details end point execution sucessful")
    """Testcase to validate get api/position/imo end point"""

    def test4(self):
        response = self.client.get(
            constant.GET_SHIP_POSITION_API_END_POINT+constant.IMO)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual("[]", response.content)
        print("Get position details end point execution sucessful")
