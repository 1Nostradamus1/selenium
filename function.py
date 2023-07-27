from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


s = Service(executable_path="C:\chromedriver")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://novosibirsk-vocal-dev.soft.study/log-in")


def Autorization(login: str, password: str):
    time.sleep(2)
    login_input = driver.find_element(By.ID, "normalLogin_username")
    login_input.send_keys(login)
    password_input = driver.find_element(By.ID, "normalLogin_password")
    password_input.send_keys(password)
    time.sleep(2)
    password_input.send_keys(Keys.ENTER)
    time.sleep(4)


def  Add_new_student(surname: str, name: str, phone: int):
    driver.find_element(By.PARTIAL_LINK_TEXT, "Add student").click()
    time.sleep(2)
    surname_input = driver.find_element(By.ID, "create-student_name_surname")
    surname_input.send_keys(surname)
    time.sleep(2)
    name_input = driver.find_element(By.ID, "create-student_name_name")
    name_input.send_keys(name)
    time.sleep(2)
    phone_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/form/div[1]/div/div[3]/div/div[2]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div[2]/input")
    phone_input.clear()
    phone_input.click()
    phone_input.send_keys(phone)
    time.sleep(2)
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    time.sleep(1)
    add_student_button = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/div/form/div[5]/div/div/div/div/div/div/button/span")
    add_student_button.click()
    time.sleep(5)

