import time
from selenium import selenium
import logging
from psuproperties import Property

class DestinyWebSectionAdd:
    
    def __init__(self, host, username, password, log):
        try:
            self.username = username
            self.password = password
            self.log = log
            self.selenium = selenium("localhost", 4444, "*firefox", host)
            self.selenium.start()
            self.selenium.open("/")
            self.selenium.window_maximize()
            self.selenium.wait_for_page_to_load("30000")
            
        except Exception as e:
            self.log.debug("Encounter exception " + str(e))
            self.tearDown()
        
    def login(self):
        sel = self.selenium
        try:
            sel.type("id=loginId", self.username)
            sel.type("id=password", self.password)
            time.sleep(0.5)
            sel.click("css=input[type=\"image\"]")
            sel.wait_for_page_to_load("30000")

        except Exception as e:
            self.log.debug("Encounter exception " + str(e))
            self.tearDown()
            return False
        return True
    
    def logout(self):
        sel = self.selenium 
        try:
            sel.click("//div[2]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td[7]/a/img")
            sel.wait_for_page_to_load("30000")
            time.sleep(0.5)
        except Exception as e:
            self.log.debug("Encounter exception " + str(e))
            self.tearDown()
            return False
        
        return True
    
    def tearDown(self):
        self.selenium.stop()
        
    def addSection(self):
        if self.login() == False:   
            return False
        sel = self.selenium
        
        sel.open("http://50.18.182.195:27070/srs/currmgr/course/courseProfile.do?method=preUpdate&courseId=54658#pinEditFields")
        sel.wait_for_page_to_load("30000")
        time.sleep(1)
        sel.click("id=addNewSection")
        sel.wait_for_page_to_load("30000")
        time.sleep(1)
        #Section Title
        sel.type("name=courseSectionProfile.sectionTitle", "Section Title")
        time.sleep(1)
        #Transcript Title
        sel.type("courseSectionProfile.transcriptTitle", "Transcript Title")
        time.sleep(1)
        #Term
        sel.select("name=semesterString", "2009-2010 - Winter (2010)")
        time.sleep(1)
        #CRN
        sel.type("courseSectionProfile.campusFisId", "999")
        time.sleep(1)
        #Former No
        sel.type("courseSectionProfile.formerSCSNumber", "111")
        time.sleep(1)
        #Max Enrollment Size
        sel.type("name=courseSectionProfile.maxEnrollmentSize", "50")
        time.sleep(1)
        #Min Enrollment Size
        sel.type("name=courseSectionProfile.minEnrollmentSize", "1")
        time.sleep(1)
        #Max Wait List Size
        sel.type("courseSectionProfile.maxWaitListSize", "5")
        time.sleep(1)
        
        time.sleep(5)
        if self.logout() == False:
            return False
        
        self.tearDown()
        return True

if __name__ == '__main__':
    prop = Property()
    host = prop.getProperty('destinyAgent.web_host.test')
    username = prop.getProperty('destinyAgent.web_login.test')
    password = prop.getProperty('destinyAgent.web_password.test')

    log = logging.getLogger('ragve.destiny_section_add.ceed')
    log.setLevel(logging.DEBUG)
    
    
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    hdlr = logging.FileHandler('/home/locngo/Documents/DestinyCourseSectionAddLog/destiny_section_add.log', mode='w')
    hdlr.setLevel(logging.DEBUG)
    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    ch.setFormatter(formatter)
    hdlr.setFormatter(formatter)

    log.addHandler(ch)
    log.addHandler(hdlr)
    
    log.debug("Start adding section XXX")
    
    dwsa = DestinyWebSectionAdd(host, username, password, log)
    
    if dwsa.addSection():
        log.debug("Add section successfully")
    else:
        log.debug("Cannot add the section")
    
    exit(0);
