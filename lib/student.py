# lib/student.py
from user import User  # <-- Change from lib.user to user

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []

    def learn(self, info):
        self.knowledge.append(info)
