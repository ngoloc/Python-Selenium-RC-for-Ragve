import time
from selenium import selenium
import logging
from psuproperties import Property

class DestinyWebCourseAdd:
    
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
        
    def addCourse(self):
        if self.login() == False:   
            return False
        sel = self.selenium
        
        sel.open("http://50.18.182.195:27070/srs/currmgr/course/courseProfile.do?method=preUpdate&courseId=54658#pinEditFields")
        sel.wait_for_page_to_load("30000")
        time.sleep(1)
        #update Course Title
        sel.type("id=courseProfileName", "Course Title")
        time.sleep(1)
        #select Program Office
#        sel.select("name=programOfficeString","Special Request - PO00SR")
#        time.sleep(1)
        #select Costing Unit
        sel.select("name=costingUnitString", "Adoptions Certificate - CU0006")
        time.sleep(1)
        #Course Hours
        sel.type("name=maximumCourseHours", "20.0")
        time.sleep(1)
        #Keywords
        sel.type("name=courseProfile.keywords", "courseProfile.keywords")
        time.sleep(1)
        #multi-select Interest Areas
        sel.add_selection("name=curSelectedInterestAreaStringArray", "Adoptions - IA0002")
        sel.add_selection("name=curSelectedInterestAreaStringArray", "Clinical Supervision - IA0006")
        time.sleep(1)
#        sel.click("//div[6]/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[4]/td[2]/div[6]/input")
#        time.sleep(1)
        #multi-select Course Categories
        sel.add_selection("name=courseCategoryStringArray", "4 Credit - CC0012")
        sel.add_selection("name=courseCategoryStringArray", "Hybrid - CC0004")
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
    
    log = logging.getLogger('ragve.destiny_course_add.ceed')
    log.setLevel(logging.DEBUG)
    
    
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    hdlr = logging.FileHandler('/home/locngo/Documents/DestinyCourseSectionAddLog/destiny_course_add.log', mode='w')
    hdlr.setLevel(logging.DEBUG)
    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    ch.setFormatter(formatter)
    hdlr.setFormatter(formatter)

    log.addHandler(ch)
    log.addHandler(hdlr)
    
    log.debug("Start adding course XXX")
    
    dwca = DestinyWebCourseAdd(host, username, password, log)
    
    if dwca.addCourse():
        log.debug("Add course successfully")
    else:
        log.debug("Cannot add the course")
    
    exit(0);
