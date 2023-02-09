from datetime import date


class Student:
    def __init__(self, sID, name, dob, classif):
        self.__stuID = sID
        self.name = name
        self.dateofbirth = dob
        self.classification = classif
        self.age = 0

    def age_calc(self, dob):
        today = date.today()
        self.age = today - dob

    def get_age(self):
        return self.age
