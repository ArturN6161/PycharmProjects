import datetime


class Person:
    name = "Artur"
    country = "Russia"
    birthyear = 1999

    def age(self):
        year_now = int(datetime.datetime.now().strftime("%Y"))
        number_of_year = year_now - self.birthyear
        
        return number_of_year


artur = Person()
print(artur.age())
