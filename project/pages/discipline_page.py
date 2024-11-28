from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
from .base_page import BasePage  # Adjust the import path as necessary
  
class DisciplinePage(BasePage):  
    def __init__(self, driver):  
        self.driver = driver  
        self.wait = WebDriverWait(self.driver, 20)

    def add_discipline(self, name, course_id):  
        self.wait.until(EC.presence_of_element_located((By.ID, "discipline-nome")))  
        self.driver.find_element(By.ID, "discipline-nome").send_keys(name)  
        self.driver.find_element(By.ID, "course-discipline-id").send_keys(course_id)  
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[py-click='add_discipline()']"))).click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".py-p")))

    def clear_course_discipline_id_field(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "course-discipline-id")))
        self.driver.find_element(By.ID, "course-discipline-id").clear()
    
    def clear_discipline_nome_field(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "discipline-nome")))
        self.driver.find_element(By.ID, "discipline-nome").clear()

    def clear_subscribe_student_id_field(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "subscribe-student-id")))
        self.driver.find_element(By.ID, "subscribe-student-id").clear()

    def clear_subscribe_discipline_id_field(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "subscribe-discipline-id")))
        self.driver.find_element(By.ID, "subscribe-discipline-id").clear()