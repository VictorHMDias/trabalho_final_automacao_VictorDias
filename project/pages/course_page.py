from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
  
class CoursePage:  
    def __init__(self, driver):  
        self.driver = driver  
  
    def add_course(self, name):  
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "course-nome")))  
        self.driver.find_element(By.ID, "course-nome").send_keys(name)  
        self.driver.find_element(By.ID, "course-btn").click()  

    def clear_course_name_field(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "course-nome")))
        self.driver.find_element(By.ID, "course-nome").clear()
    
    def clear_course_id_field(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "course-id")))
        self.driver.find_element(By.ID, "course-id").clear()