import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

login_prod = "********"
password_prod = "*********"

class Drums_testing(unittest.TestCase):
    def setUp(self):
        s = Service(executable_path="C:\chromedriver")
        self.driver = webdriver.Chrome(service=s)

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        driver.get("https://novosibirsk-drums-stage.soft.study/log-in")
        login_input = wait.until(EC.presence_of_element_located((By.ID, "normalLogin_username")))
        login_input.send_keys(login_prod)
        password_input = wait.until(EC.presence_of_element_located((By.ID, "normalLogin_password")))
        password_input.send_keys(password_prod)
        password_input.send_keys(Keys.ENTER)
        menu_bar = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/header/div[1]/div/div[1]/button/span[2]")))
        assert "Menu" in menu_bar.text


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()