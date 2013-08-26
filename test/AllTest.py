'''
Created on Sep 16, 2011

@author: dennis
'''
import unittest
from test.GrumpTest import GrumpTest
from test.XML4ParserTest import XML4ParserTest

class AllTest(unittest.TestSuite):
	def testAll(self):
		self.addTests(unittest.TestLoader().loadTestsFromTestCase(GrumpTest))
		self.addTests(unittest.TestLoader().loadTestsFromTestCase(XML4ParserTest))
		unittest.TextTestRunner(verbosity=2).run(self)

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()
