import unittest
import tunedude
import json

with open('config.json') as json_data_file:
    config = json.load(json_data_file)
TEST_SPREADSHEET_ID = config['TEST']['TEST_SPREADSHEET_ID']

class TestTD(unittest.TestCase):

    def SetUp(self):
        tunedude.getInProgressSpreadSheet(TEST_SPREADSHEET_ID,'In Progress!A2:E')




if __name__ == '__main__':
    unittest.main()