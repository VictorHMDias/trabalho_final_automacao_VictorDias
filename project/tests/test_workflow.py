import sys  
import os  
import unittest
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import time

from pages.base_page import BasePage  
from pages.student_page import StudentPage  
from pages.course_page import CoursePage  
from pages.discipline_page import DisciplinePage  

class TestWorkflow(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://tdd-detroid.onrender.com/")
        self.wait = WebDriverWait(self.driver, 30)
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".py-body")))  # Adding to Wait for the main body to load since there is a splash load screen
        self.base_page = BasePage(self.driver)
        self.discipline_page = DisciplinePage(self.driver)
        self.student_page = StudentPage(self.driver)
        self.course_page = CoursePage(self.driver)

    def test_student_course_discipline_workflow(self):
        # Add student
        self.student_page.add_student("Victor")
        assert "Added student id: 1, Name: Victor" in self.base_page.get_alert_message()

        # Add courses
        time.sleep(2)  # Add a delay of 2 seconds
        self.course_page.add_course("Sistemas")
        assert "Added course id: 1, Nome: Sistemas" in self.base_page.get_alert_message()

        # Subscribe student to course
        time.sleep(2)  # Add a delay of 2 seconds
        self.student_page.subscribe_student_to_course("1", "1")
        assert "Student id 1 subscribed to course id 1" in self.base_page.get_alert_message()

        # Add more courses
        time.sleep(2)  # Add a delay of 2 seconds
        self.course_page.clear_course_name_field()
        self.course_page.add_course("Direito")
        assert "Added course id: 2, Nome: Direito" in self.base_page.get_alert_message()

        time.sleep(2)  # Add a delay of 2 seconds
        self.course_page.clear_course_name_field()
        self.course_page.add_course("Enfermagem")
        assert "Added course id: 3, Nome: Enfermagem" in self.base_page.get_alert_message()



        # Add discipline to course
        time.sleep(2)  # Add a delay of 2 seconds
        self.discipline_page.add_discipline("Automacao", "1")
        assert "Added discipline id: 1, Name: Automacao, Course: 1" in self.base_page.get_alert_message()

        # Add more disciplines
        time.sleep(2)  # Add a delay of 2 seconds
        self.discipline_page.clear_course_discipline_id_field()
        self.discipline_page.clear_discipline_nome_field()
        self.discipline_page.add_discipline("Devops", "1")
        assert "Added discipline id: 2, Name: Devops, Course: 1" in self.base_page.get_alert_message()

        time.sleep(2)  # Add a delay of 2 seconds
        self.discipline_page.clear_course_discipline_id_field()
        self.discipline_page.clear_discipline_nome_field()      
        self.discipline_page.add_discipline("CICD", "1")
        assert "Added discipline id: 3, Name: CICD, Course: 1" in self.base_page.get_alert_message()

        # Subscribe student to discipline
        time.sleep(2)  # Add a delay of 2 seconds
        self.student_page.subscribe_student_to_discipline("1", "1")
        assert "Aluno deve se inscrever em 3 materias no minimo" in self.student_page.get_alert_message()
        

        # Subscribe student to more disciplines
        time.sleep(2)  # Add a delay of 2 seconds
        self.discipline_page.clear_subscribe_discipline_id_field()
        self.discipline_page.clear_subscribe_student_id_field()
        self.student_page.subscribe_student_to_discipline("1", "2")
        assert "Student id 1, Name Victor subscribed to discipline id 2" in self.student_page.get_alert_message()
        
        time.sleep(2)  # Add a delay of 2 seconds
        self.discipline_page.clear_subscribe_discipline_id_field()
        self.discipline_page.clear_subscribe_student_id_field()
        self.student_page.subscribe_student_to_discipline("1", "3")
        assert "Student id 1, Name Victor subscribed to discipline id 3" in self.student_page.get_alert_message()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()