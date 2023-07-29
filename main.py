from function import Add_new_student, Autorization, Close_driver, Search_student
from pydantic import BaseModel

login_prod = "*******"
password_prod = "********"


class Student(BaseModel):
    surname: str
    name: str
    phoneNumber: int


Student.name = "Оля"
Student.surname = "Иванова"
Student.phoneNumber = 9132238732

try:
    Autorization(login_prod, password_prod)
    Add_new_student(Student.surname, Student.name, Student.phoneNumber)
    Search_student(Student.surname, Student.name)

except Exception as ex:
    print(ex)

finally:
    Close_driver()
