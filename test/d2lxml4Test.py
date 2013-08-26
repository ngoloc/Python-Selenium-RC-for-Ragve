'''
Created on Nov 20, 2011

@author: dennis
'''
import unittest
from d2lxml4 import D2LXML4
import xml.etree.ElementTree as ET
#import lxml.etree as etree
import json

class d2lxml4Test(unittest.TestCase):


	def setUp(self):
		self.d2lxml4 = D2LXML4()
		self.all_req = ET.parse('/vol/d2l/ragve/lib/unit-test/all_req.xml')

	def tearDown(self):
		pass

	def test_xml_to_json(self):
		'''
			Test the conversion of an XML IMS description into a data-structure which is
			convertable directly into JSON.
		'''
		job = ET.tostring(self.all_req.getroot())
		job_struct = self.d2lxml4.xml4_to_struct(job)
		job_json = json.dumps(job_struct, indent=4)
		#print job_json
		#f = open('/vol/d2l/ragve/lib/unit-test/all_req.json', 'w');	f.write(job_json); 	f.close()
		job_json_test = open('/vol/d2l/ragve/lib/unit-test/all_req.json', 'r').read()
		self.assertTrue(job_json == job_json_test)

	def test_json_to_xml(self):
		'''
			Test the conversion to an XML IMS description from a JSON representation
		'''
		f = open('/vol/d2l/ragve/lib/unit-test/all_req.json', 'r')
		job_json = json.load(f)# indent=4)
		
		# Convert data structure to xml.
		job_xml = self.d2lxml4.struct_to_xml4(job_json)

		job_xml_pretty = self.d2lxml4.pretty_xml(job_xml)
		#f = open('/vol/d2l/ragve/lib/unit-test/all_req.xml', 'w');	f.write(job_xml_pretty); 	f.close()
		job_xml_expected = open('/vol/d2l/ragve/lib/unit-test/all_req.xml', 'r').read()
		print job_xml_pretty
		self.assertTrue(job_xml_pretty == job_xml_expected) 
		#self.assertTrue(job_xml_expected in job_xml_pretty)
		#t = etree.parse(job_xml)
		#print etree.tostring(t, pretty_print=True)
		#job_xml_pretty = parseString(job_xml).toprettyxml(indent = '    ')
		#f = open('/vol/d2l/ragve/lib/unit-test/all_req.xml', 'w');	f.write(job_xml); 	f.close()
		
		
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()
