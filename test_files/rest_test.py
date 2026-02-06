class Student:
   

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_profile(self, year):
      
        if year < 0:
            raise ValueError("Year cannot be negative")
        return f"{self.name} - {year}"


def countdown(n):
    while n > 0:
        yield n
        n -= 1
