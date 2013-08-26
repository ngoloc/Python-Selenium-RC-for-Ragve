'''
Created on Jan 4, 2012

@author: dennis
'''
import unittest
from D2LAgent import D2LAgent
from DestinyAgent import DestinyAgent
from mq.d2lAgentPublish import heartbeat
from mq.destinyAgent import publish_one

class MQTest(unittest.TestCase):


	def setUp(self):
		pass


	def tearDown(self):
		pass


	def testName(self):
		pass

	def testDestinyAgentPublish(self):
		try:
			destiny_agent = DestinyAgent()
			for i in range(1, 5):
				destiny_agent.log.info('calling publish_one()')
				publish_one(destiny_agent, 'destiny_d2l_ceed', 'heartbeat: 11111111')
			self.assertTrue(True)
		except:
			self.assertTrue(False)

	def ttestD2LAgentPublish(self):
		try:
			d2l_agent = D2LAgent(action='provision', instance='ceed')
			for i in range(1, 5):
				heartbeat(d2l_agent)
			self.assertTrue(True)
		except:
			self.assertTrue(False)


if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()
