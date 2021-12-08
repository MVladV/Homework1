from datetime import date
from re import match


class Person:
    def __init__(self, surname, name, phone, birthday):
        self.surname = surname
        self.name = name
        self.phone = phone
        self.birthday = birthday

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not surname:
            raise TypeError
        if not isinstance(surname, str):
            raise TypeError
        self.__surname = surname

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not name:
            raise TypeError
        if not isinstance(name, str):
            raise TypeError
        self.__name = name

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday):
        if not birthday:
            raise TypeError
        if not isinstance(birthday, date):
            raise TypeError
        self.__birthday = birthday

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        if not phone:
            raise TypeError
        if not isinstance(phone, str):
            raise TypeError
        self.__phone = phone

    def __str__(self):
        return f"Name: {self.name}\nSurname: {self.surname}\nPhone: {self.phone}\nBirthday: {self.birthday}"


class Notebook:
    def __init__(self, *persons):
        self.persons = list(persons)

    @property
    def persons(self):
        return self.__persons

    @persons.setter
    def persons(self, persons):
        if not all(isinstance(person, Person) for person in persons):
            raise TypeError
        self.__persons = persons

    def __str__(self):
        return '\n\n'.join(list(map(str, self.persons)))

    def __add__(self, person):
        if not isinstance(person, Person):
            raise TypeError
        self.persons.append(person)

    def __sub__(self, person):
        if not isinstance(person, Person):
            raise TypeError
        self.persons.remove(person)

    def __mul__(self, arg):
        res = []
        if not isinstance(arg, dict):
            raise TypeError
        # print(self.person.get(f'{user.id}'))
