from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



s = Service(executable_path="C:\chromedriver")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://novosibirsk-drums-stage.soft.study/log-in")

wait = WebDriverWait(driver, 10)

def Autorization(login: str, password: str):
    login_input = wait.until(EC.presence_of_element_located((By.ID, "normalLogin_username")))
    login_input.send_keys(login)
    password_input = wait.until(EC.presence_of_element_located((By.ID, "normalLogin_password")))
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)



def Add_new_student(surname: str, name: str, phone: int):
    wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Add student"))).click()
    surname_input = wait.until(EC.presence_of_element_located((By.ID, "create-student_name_surname")))
    surname_input.send_keys(surname)
    name_input = wait.until(EC.presence_of_element_located((By.ID, "create-student_name_name")))
    name_input.send_keys(name)
    phone_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[3]/div/form/div[1]/div/div[3]/div/div[2]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div[2]/input")))
    phone_input.clear()
    phone_input.click()
    phone_input.send_keys(phone)
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    add_student_button = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[3]/div/form/div[5]/div/div/div/div/div/div/button/span")))
    add_student_button.click()
    time.sleep(5)


def Close_driver():
    driver.quit()
    driver.close()

def Search_student(surname: str, name: str):
    wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/header/div[1]/div/div[1]/button/span[1]"))).click()
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "List of students"))).click()
    name_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[2]/div/span[2]/input")))
    name_input.clear()
    name_input.send_keys(surname)
    search_name = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[3]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/a")))
    search_target = (surname + " " + name)
    if search_name.text == search_target:
        print("Студент найден!")
    else:
        print("Студент не найден!")
