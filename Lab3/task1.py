# Write a program for selling tickets to IT-events. Each ticket has a unique number and a price. There are four type_ts
# of tickets: standard ticket, advance ticket (purchased 60 or more days before the event), late ticket (purchased
# fewer than 10 days before the event) and student ticket. Additional information: -advance ticket - discount 40% of
# the standard ticket price; -student ticket - discount 50% of the standard ticket price; -late ticket - additional 10%
# to the reguler ticket price. All tickets must have the following properties: -the ability to construct a ticket by
# number; -the ability to ask for a ticket’s price; -the ability to print a ticket as a String.

import json


class Events:
    events_tickets = []
    advance_tickets = 0
    late_tickets = 0
    student_tickets = 0

    def __init__(self, name_of_file, name, standard, advance, late, student, price):
        self.price_student = round(price * 0.5)  # студентський
        self.advance_price = round(price * 0.6)  # завчасно куплений
        self.late_price = round(price * 1.1)  # куплено запізно
        self.name_of_file = name_of_file
        self.name = name
        self.standard = standard
        self.advance = advance
        self.late = late
        self.student = student
        self.price = price
        self.quantity = standard + advance + late + student
        Events.add_event(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError()
        if not name:
            raise ValueError()
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, int):
            raise TypeError()
        if price <= 0:
            raise ValueError()
        self.__price = price

    @property
    def standard(self):
        return self.__standard

    @standard.setter
    def standard(self, standard):
        if not isinstance(standard, int):
            raise TypeError()
        if standard <= 0:
            raise ValueError()
        self.__standard = standard

    @property
    def advance(self):
        return self.__advance

    @advance.setter
    def advance(self, advance):
        if not isinstance(advance, int):
            raise TypeError()
        if advance <= 0:
            raise ValueError()
        self.__advance = advance

    @property
    def late(self):
        return self.__late

    @late.setter
    def late(self, late):
        if not isinstance(late, int):
            raise TypeError()
        if late <= 0:
            raise ValueError()
        self.__late = late

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, student):
        if not isinstance(student, int):
            raise TypeError()
        if student <= 0:
            raise ValueError()
        self.__student = student

    def add_event(self):  # add to .json file

        event = {
            "Name of file": self.name_of_file,
            "Name": self.name,
            "Standard quantity": self.standard,
            "Price": self.price,
            "Advance quantity": self.advance,
            "Advance price": self.advance_price,
            "Late quantity": self.late,
            "Late price": self.late_price,
            "Student quantity": self.student,
            "Student price": self.price_student
        }
        with open(self.name_of_file, "w") as write_file:
            json.dump(event, write_file)
        write_file.close()

    def __str__(self):
        return f"Event: \n" \
               f"{self.__standard} standard tickets, price - {self.__price}, " \
               f"{self.__advance} advance tickets, price - {self.advance_price}, " \
               f"{self.__late} late tickets, price - {self.late_price}, " \
               f"{self.__student} student tickets, price - {self.price_student} \n"


class Tickets:

    file_tickets = []

    def __init__(self, event, number, days, price, type_t="Standard ticket"):
        self.event = event
        self.number = number
        self.days = days
        self.price = price
        self.type_t = type_t
        Tickets.add_ticket(self)
        if len(self.event.events_tickets) > event.quantity:
            raise ValueError("No more tickets.")

    @property
    def event(self):
        return self.__event

    @event.setter
    def event(self, event):
        if not isinstance(event, Events):
            raise TypeError()
        self.__event = event

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if not isinstance(number, int):
            raise TypeError()
        if number <= 0:
            raise ValueError()
        for ticket in self.event.events_tickets:
            if number in ticket.values():
                raise ValueError()
        self.__number = number

    @property
    def days(self):
        return self.__days

    @days.setter
    def days(self, days):
        if not isinstance(days, int):
            raise TypeError()
        if days <= 0:
            raise ValueError()
        self.__days = days

    def add_ticket(self):  # add to .json file
        ticket = {
            "Event": self.event.name,
            "Number": self.number,
            "Type": self.type_t,
            "Days": self.days,
            "Price": self.price
        }
        self.file_tickets.append(ticket)
        with open("info.json", "w") as write_file:
            json.dump(self.file_tickets, write_file)
        write_file.close()

    def __str__(self):
        return f"{self.type_t} ticket #{self.number} for the {self.event.name} event:" \
               f" price - {self.price}, bought {self.days} days before the event"

    @staticmethod
    def get_num(event, number):

        with open("info.json", "r") as read_file:
            info = json.load(read_file)
        for ticket in info:
            if ticket.get("Event") == event.name and ticket.get("Number") == number:
                return ticket

    @staticmethod
    def get_price(event, number):
        with open("info.json", "r") as read_file:
            info = json.load(read_file)
        for ticket in info:
            if ticket.get("Event") == event.name and ticket.get("Number") == number:
                return ticket.get("Price")

    @staticmethod
    def standard_price(name_of_file):
        with open(name_of_file, "r") as read_file:
            info = json.load(read_file)
        return info.get("Price")


class Student(Tickets):

    def __init__(self, event, number, days):
        with open(event.name_of_file, "r") as read_file:
            info = json.load(read_file)
        super().__init__(event, number, days, info.get("Student price"), "Student ticket")
        event.student_tickets += 1
        if event.student_tickets > event.student:
            raise ValueError()


class Advance(Tickets):

    def __init__(self, event, number, days):
        if days < 60:
            raise ValueError()
        with open(event.name_of_file, "r") as read_file:
            info = json.load(read_file)
        super().__init__(event, number, days, info.get("Advance price"), "Advance ticket")
        event.advance_tickets += 1
        if event.advance_tickets > event.advance:
            raise ValueError()


class Late(Tickets):

    def __init__(self, event, number, days):
        if days > 10:
            raise ValueError()
        with open(event.name_of_file, "r") as read_file:
            info = json.load(read_file)
        super().__init__(event, number, days, info.get("Late price"), "Late ticket")
        event.late_tickets += 1
        if event.late_tickets > event.late:
            raise ValueError()


def main():
    try:
        event_1 = Events("event1.json", "Business Analyst course", 1, 2, 1, 3, 700)
        print(event_1)

        ticket_1 = Tickets(event_1, 1, 15, Tickets.standard_price(event_1.name_of_file))
        ticket_2 = Tickets(event_1, 2, 16, Tickets.standard_price(event_1.name_of_file))
        print("Received a ticket by number:")
        print(Tickets.get_num(event_1, 2))
        print()
        ticket_3 = Late(event_1, 3, 2)
        ticket_4 = Advance(event_1, 4, 70)
        ticket_5 = Student(event_1, 5, 10)
        ticket_6 = Advance(event_1, 6, 67)
        ticket_7 = Student(event_1, 7, 14)

        print("All tickets:")
        print(ticket_1)
        print(ticket_2)
        print(ticket_3)
        print(ticket_4)
        print(ticket_5)
        print(ticket_6)
        print(ticket_7)

    except Exception:
        print("Exeption!")


main()
