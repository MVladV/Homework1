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

    def __mul__(self, name):
        for person in self.persons:
            if person.name == name:
                return person


class main:
    try:
        user1 = Person("Мітлицький", "Влад", "+380964068502", date(2003, 4, 2))
        # print(user1)
        # print()
        user2 = Person("Мельник", "Олег", "+380954058502", date(2000, 7, 25))
        user3 = Person("Загорецький", "Іван", "+380984028135", date(2010, 9, 13))
        user4 = Person("Калуш", "Віталій", "+380999999502", date(2001, 1, 3))

        book = Notebook(user1, user2, user3)
        print(book)
        print()

        book + user4
        print(f'Add User #4:\n{book}\n')

        book - user3
        print(f'Delete User #3:\n{book}\n')

        print(book * "Влад")

        input('press enter to continue')
    except Exception:
        print("Exeption!")
