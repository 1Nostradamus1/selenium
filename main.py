from function import Add_new_student, Autorization, driver


login_prod = "admin"
password_prod = "UdngeL7ldEu"
surname_student = "Иванов"
name_student = "Иван"
phoneNumber_student = 9132238732


try:
    Autorization(login_prod, password_prod)
    Add_new_student(surname_student, name_student, phoneNumber_student)

except Exception as ex:
    print(ex)

finally:
    driver.quit()
    driver.close()





