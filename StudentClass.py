from datetime import date


class Student:
    def __init__(self, sID, name, dob, classif):
        self.__stuID = sID
        self.__name = name
        self.__dob = dob
        self.__classification = classif
        self.__age = 0
        self.__register = ""

    def age_calc(self, dob):
        today = date.today()
        dob = self.__dob.split("/")
        dob_year = int(dob[2])
        age = today.year - dob_year
        self.__age = age

    def register(self):
        # bunch of if statements
        print()

    def get_age(self):
        return self.__age

    def return_registration(self):
        return self.__register
