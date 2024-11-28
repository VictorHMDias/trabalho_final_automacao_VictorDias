from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
import datetime
  
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".py-body")))  # Wait for the main body to load

  
    def load(self):  
        self.driver.get("https://tdd-detroid.onrender.com/")  
        self.wait = WebDriverWait(self.driver, 30)
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".py-body")))  # Wait for the main body to load
        
    def get_alert_message(self):  
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "local-terminal")))  
        alert_message = self.driver.find_element(By.ID, "local-terminal").text
        actual_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        assert actual_date in alert_message
        return alert_message