import unittest
#from ldapPerson import *

class LdapPersonTest(unittest.TestCase):
	def setUp(self):
		self.fileFac = '/vol/d2l/ragve/lib/unit-test/ldapdiff.20270'

	def test_init(self):
		#cmd = createPeopleByFile( self.fileFac )
		#print cmd
		pass
		
if __name__ == '__main__':
	unittest.main()	
