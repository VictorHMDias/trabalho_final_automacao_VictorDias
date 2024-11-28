from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
from .base_page import BasePage
  
class StudentPage(BasePage):
    def __init__(self, driver):  
        super().__init__(driver)

    def add_student(self, student_name):
        self.driver.find_element(By.ID, "student-nome").send_keys(student_name)
        # Wait for the overlay to disappear
        self.wait.until(EC.invisibility_of_element_located((By.ID, "pyscript_loading_splash")))
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[py-click='add_student()']"))).click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".py-p")))

    def subscribe_student_to_discipline(self, student_id, discipline_id):
        self.driver.find_element(By.ID, "subscribe-student-id").send_keys(student_id)
        self.driver.find_element(By.ID, "subscribe-discipline-id").send_keys(discipline_id)
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[py-click='subscribe_discipline()']"))).click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".py-p")))

    def subscribe_student_to_course(self, student_id, course_id):
        self.driver.find_element(By.ID, "student-id").send_keys(student_id)
        self.driver.find_element(By.ID, "course-id").send_keys(course_id)
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[py-click='subscribe_course()']"))).click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".py-p")))

    def clear_discipline_id_field(self):
        self.driver.find_element(By.ID, "subscribe-discipline-id").clear()