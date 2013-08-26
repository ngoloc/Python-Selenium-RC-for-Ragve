'''
Created on Sep 13, 2011

@author: dennis
'''
import unittest
from xml4Parser import XML4Parser
import json

class XML4ParserTest(unittest.TestCase):


	def setUp(self):
		self.xml4Parser = XML4Parser(xml4_file=['/vol/d2l/ragve/lib/unit-test/ggexdrop.xml',
									 				'/vol/d2l/ragve/lib/unit-test/ggexadd.xml' ])
		
		self.memberships = self.xml4Parser.get_memberships()
		self.offerings = self.xml4Parser.get_offerings()

	def tearDown(self):
		pass


	def testOfferings(self):
		self.assertTrue(self.offerings.has_key('OFFERING_CI-810-633_201103'))

	def testMemberships(self):
		self.assertFalse(self.memberships.has_key('SECTION_D2LSRC'))
		self.assertTrue(self.memberships.has_key('SECTION_84188.201103'))
		
	def testMember(self):
		self.assertTrue(self.memberships['SECTION_84188.201103'].has_key('PERSON_31472'))
		self.assertFalse(self.memberships['SECTION_84188.201103'].has_key('PERSON_guest84188'))
		member = self.memberships['SECTION_84188.201103']['PERSON_31472']
		self.assertTrue(member['role'] == 'Student')
		self.assertTrue(member['sourced_id'] == 'PERSON_31472')

	def testAddDrop(self):
		member_drop = self.memberships['SECTION_84188.201103']['PERSON_41472']
		self.assertTrue(member_drop['action'] == 'drop')
		
		member_add = self.memberships['SECTION_84188.201103']['PERSON_31472']
		self.assertTrue(member_add['action'] == 'add')

		member_add = self.memberships['SECTION_84188.201103']['PERSON_31474']
		self.assertTrue(member_add['action'] == 'drop')
		
	def testRole(self):
		member = self.memberships['SECTION_84188.201103']['PERSON_31473']
		self.assertTrue(member['role'] == 'Instructor')

		member = self.memberships['SECTION_84188.201103']['PERSON_31474']
		self.assertTrue(member['role'] == 'Instructor')

	def testStructure(self):
		memberships = json.dumps(self.memberships, indent=4, sort_keys=True)
		offerings = json.dumps(self.offerings, indent=4, sort_keys=True)
		
		memb = open('/vol/d2l/ragve/lib/unit-test/xml4MembershipsStruct.json', 'r').read()
		#open('/vol/d2l/ragve/lib/unit-test/xml4MembershipsStruct.json', 'w').write(memberships)
		off = open('/vol/d2l/ragve/lib/unit-test/xml4OfferingsStruct.json', 'r').read()
		#open('/vol/d2l/ragve/lib/unit-test/xml4OfferingsStruct.json', 'w').write(offerings)

		self.assertTrue(memberships == memb)
		self.assertTrue(offerings == off)

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()
