import json
import unittest
from DestinyWebAgent import DestinyWebAgent
from DestinyWebAgent import DAgent
from DestinyWebAgent import Instructor
from DestinyWebAgent import StudentGroup
from DestinyWebAgent import Building
from psuproperties import Property
import logging

class Test(unittest.TestCase):

    def setUp(self):
        self.prop = Property()
        self.host = self.prop.getProperty('destinyAgent.web_host')
        self.username = self.prop.getProperty('destinyAgent.web_login')
        self.password = self.prop.getProperty('destinyAgent.web_password')
        self.log = logging.getLogger('ragve.destiny_agent.ceed')
        self.log.setLevel(logging.DEBUG)
        
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        hdlr = logging.FileHandler('/home/locngo/Documents/ktraks/myapp.log')
        hdlr.setLevel(logging.DEBUG)
        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        ch.setFormatter(formatter)
        hdlr.setFormatter(formatter)
    
        self.log.addHandler(ch)
        self.log.addHandler(hdlr)
        
#    def testLogin(self):
#        da = DAgent(self.host,self.username,self.password)
#        dwa = DestinyWebAgent(da.log,da.host)
#        if dwa.login(da.username,da.password):
#            self.assertTrue(dwa.selenium.is_element_present("//div[2]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td[7]/a/img"))
#            dwa.tearDown()
#            self.assertTrue(True)
#        else:
#            self.assertTrue(dwa.selenium.sessionId==None)
#            self.assertTrue(False)
#
#    def testLogout(self):
#        da = DAgent(self.host,self.username,self.password)
#        dwa = DestinyWebAgent(da.log,da.host)
#        if dwa.login(da.username,da.password):
#            if(dwa.logout()):
#                dwa.tearDown()
#                self.assertTrue(True)
#            else:
#                self.assertTrue(False)
#        else:
#            self.assertTrue(True)         

#    def testBuildings(self):
#        json_data=open('/home/locngo/Documents/ktraks/building.json')
#        body = json.loads(json_data.read())
#        json_data.close()
#        
#        blds = body["items"]
#        da = DAgent(self.log,self.host,self.username,self.password)
#        
#        for key in blds.keys():
#            bld = blds[key]
#            da.log.info("Ready to add new building: " + key + " - " + str(bld))
#            sg = Building(bld["lcode"],bld["name"],bld["addr"],bld["city"],bld["state"],bld["zip"],bld["campus"])
#            
#            createBuilding = da.createBuilding(sg)
#            self.assertTrue(createBuilding)
#            if(createBuilding):
#                da.log.info("Successfully created building " + key)
#            else:
#                da.log.info("Couldn't create building " + key)
#                
#        if da.success == True:
#            da.destiny_web_agent.tearDown()
#            da.log.info("End of adding buildings")
            
#    def testStudentGroups(self):
#        json_data=open('/home/locngo/Documents/ktraks/group.json')
#        body = json.loads(json_data.read())
#        json_data.close()
#        
#        grs = body["items"]
#        da = DAgent(self.log,self.host,self.username,self.password)
#        
#        for key in grs.keys():
#            gr = grs[key]
#            da.log.info("Ready to add new group: " + key + " - " + str(gr))
#            sg = StudentGroup(gr["name"],gr["vendor_id"],gr["fed_tax_id"],gr["acode"],
#                              gr["addr1"],gr["addr2"],gr["city"],gr["state"],gr["zip"],
#                              gr["agency_phone_area"],gr["agency_phone_num"],gr["agency_phone_extn"],
#                              gr["agency_fax_area"],gr["agency_fax_num"],
#                              gr["person_phone_area"],gr["person_phone_num"],
#                              gr["person_fax_area"],gr["person_fax_num"],
#                              gr["person_email"],
#                              gr["person_name"],gr["www_home"],"",gr["reg_phrase"],gr["notes"])
#            
#            createGroup = da.createGroup(sg)
#            self.assertTrue(createGroup)
#            if(createGroup):
#                da.log.info("Successfully created student group " + key)
#            else:
#                da.log.info("Couldn't create student group " + key)
#                
#        if da.success == True:
#            da.destiny_web_agent.tearDown()
#            da.log.info("End of adding groups")

#    def testCreateNewInstructors(self):
#        json_data=open('/home/locngo/Documents/ktraks/instructor.json')
#        body = json.loads(json_data.read())
#        json_data.close()
#        
#        insts = body["items"]
#        da = DAgent(self.log,self.host,self.username,self.password)
#        
#        for key in insts.keys():
#            inst = insts[key]
#            da.log.info("Ready to add new instructor: " + key + " - " + str(inst))
#            instructor = Instructor(inst["type"],inst["lastname"],inst["firstname"],inst["minitial"],
#                                    inst["birthdate"],inst["active"],inst["psuid"],inst["tcode"],
#                                    inst["employer"],inst["position"],inst["acode"],inst["home"]["street1"],inst["home"]["street2"],
#                                    inst["home"]["city"],inst["home"]["state"],inst["home"]["country"],inst["home"]["zipcode"],
#                                    inst["office"]["street1"],inst["office"]["street2"],inst["office"]["city"],
#                                    inst["office"]["state"],inst["office"]["country"],inst["office"]["zipcode"],
#                                    inst["home"]["phone_area"],inst["home"]["phone_number"],inst["home"]["fax_area"],inst["home"]["fax_number"],inst["office"]["phone_area"],inst["office"]["phone_number"],inst["office"]["fax_area"],inst["office"]["fax_number"],
#                                    inst["home"]["email"],inst["office"]["email"],inst["bio"],inst["dist_qual"],
#                                    inst["degree"],inst["www_home"],inst["miscinfo"])
#            
#            createInstructor = da.createInstructor(instructor)
#            self.assertTrue(createInstructor)
#            if(createInstructor):
#                da.log.info("Successfully created instructor " + key)
#            else:
#                da.log.info("Couldn't create instructor " + key)
#        
#        if da.success == True:
#            da.destiny_web_agent.tearDown()
#            da.log.info("End of adding instructors")
            
    def tearDown(self):
        pass
        
if __name__ == '__main__':
    unittest.main()
