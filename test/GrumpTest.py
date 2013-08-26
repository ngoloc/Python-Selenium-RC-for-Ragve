'''
Created on Sep 13, 2011

@author: dennis
'''
import unittest
from grump import Grump
import json

class GrumpTest(unittest.TestCase):


	def setUp(self):
		self.grump = Grump()
		self.grump.init_scan(before='/vol/d2l/ragve/lib/unit-test/state.xml', state='/vol/d2l/ragve/lib/unit-test/state.xml', term_code='201103', xml4_files=['/vol/d2l/ragve/lib/unit-test/ggexdrop.xml', '/vol/d2l/ragve/lib/unit-test/ggexadd.xml'])

	def tearDown(self):
		pass
	
	def testInit(self):
		pass

	def testAddDrop(self):
		self.grump.gen_add_drop()
		tasks = self.grump.get_membership_tasks()
		#print 'calc group tasks: ', json.dumps(tasks, indent = 4), 'done'
		#open('/vol/d2l/ragve/lib/unit-test/grump_membership_tasks.json', 'w').write( json.dumps(tasks, indent = 4) )
		tasks_result = open('/vol/d2l/ragve/lib/unit-test/grump_membership_tasks.json', 'r').read()
		#print 'stored group tasks: ', json.dumps(tasks, indent = 4), tasks_result, 'done'
		self.assertTrue(json.dumps(tasks, indent=4) == tasks_result)

	def testAddCourse(self):
		self.grump.gen_groups()
		tasks = self.grump.get_group_tasks()
		print json.dumps(tasks, indent=4)
		#open('/vol/d2l/ragve/lib/unit-test/grump_group_tasks.json', 'w').write( json.dumps(tasks, indent = 4) )
		tasks_result = open('/vol/d2l/ragve/lib/unit-test/grump_group_tasks.json', 'r').read()
		self.assertTrue(json.dumps(tasks, indent=4) == tasks_result)

	def testCreateDelete(self):
		task = {'group_id': 'course-ece-550-999-group'
			, 'group_name': 'ECE-550-999 Fall 2011'
			, 'group_desc': 'ECE-550-999: OCTARINE STUDY'}
		email_permission = 'Owner'
		self.grump.create_google_group(task, email_permission)
		self.assertTrue(self.grump.google_group_exists(task))
		self.grump.delete_google_group(task)
		self.assertFalse(self.grump.google_group_exists(task))
		

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()
