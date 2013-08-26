'''
Created on Nov 22, 2011

@author: dennis
'''
import unittest
from MQAdapter import MQAdapter
from d2lweb import D2LWeb
import sys
import traceback
import time

class Test(unittest.TestCase):


	def setUp(self):
		pass


	def tearDown(self):
		pass

	def TestSendReceive(self):
		mq = MQAdapter()

		def _on_message_receipt(channel, method, header, msg):
			self.assertEqual(msg, 'heartbeat:  T E S T I N G')
			mq.log.info("_on_message_receipt(): received body: " + str(msg))
			if (str(msg).startswith('heartbeat')):
				mq.log.info("_on_message_receipt(): ACKing: " + str(msg))
				channel.basic_ack(delivery_tag=method.delivery_tag)
				channel.basic_cancel(method.delivery_tag)
				channel.close()
				#channel.stop_consuming()
				mq.log.info("_on_message_receipt(): Closing")

		mq.set_on_message_receipt(_on_message_receipt)
		#mq.post_message('heartbeat:  T E S T I N G')
		mq.wait_for_messages()

	def testSerialError(self):
		mq_error = MQAdapter(queue='test', error_queue=True, timeout=10)
		mq = MQAdapter(queue='test')

				
		def _on_message_receipt(channel, method, header, msg):
			mq.log.info("_on_message_receipt(): received body: " + str(msg))
			
			if (str(msg).startswith('heartbeat: Errored Message')):
				mq.log.info("_on_message_receipt(): repost: " + str(msg))
				#channel.basic_reject(delivery_tag = method.delivery_tag, requeue=True)
				#channel.basic_recover(_on_recover, False)
				mq_error.post_message(msg)
				mq.log.info("_on_message_receipt(): Closing")
				channel.basic_ack(delivery_tag=method.delivery_tag)
				channel.close()
			else:
				mq.log.info("_on_message_receipt(): ACKing: " + str(msg))
				channel.basic_ack(delivery_tag=method.delivery_tag)

		def _on_message_receipt_error(channel, method, header, msg):
			mq.log.info("_on_message_receipt(): received body: " + str(msg))
			
			if (str(msg).startswith('heartbeat: Errored Message')):
				mq.log.info("_on_message_receipt_error(): repost: " + str(msg))
				#channel.close()
				channel.basic_ack(delivery_tag=method.delivery_tag)
			else:
				mq.log.info("_on_message_receipt_error(): ACKing: " + str(msg))
				channel.basic_ack(delivery_tag=method.delivery_tag)

		mq.set_on_message_receipt(_on_message_receipt)
		mq.post_message('heartbeat: Errored Message')
		mq.post_message('heartbeat: Correct Message')
		#mq.channel.basic_recover(_on_recover, False)
		mq.wait_for_messages()
		mq_error.set_on_message_receipt(_on_message_receipt_error)
		mq_error.wait_for_messages()


if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testInit']
	unittest.main()
