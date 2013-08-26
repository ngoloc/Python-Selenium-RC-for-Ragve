import unittest
from gsheet import GSheet

class GSheetTest(unittest.TestCase):
	def setUp(self):
		self.gsheet = GSheet()

	def ttest_init(self):
		self.gsheet.setSpreadSheet('D2L Courses')
		self.gsheet.setWorkSheet('test')
		self.assertTrue(self.gsheet.curr_wksht_id == 'ocx')
		
if __name__ == '__main__':
	unittest.main()	
