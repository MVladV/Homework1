# Write a program for selling tickets to IT-events. Each ticket has a unique number and a price. There are four type_ts
# of tickets: standard ticket, advance ticket (purchased 60 or more days before the event), late ticket (purchased
# fewer than 10 days before the event) and student ticket. Additional information: -advance ticket - discount 40% of
# the standard ticket price; -student ticket - discount 50% of the standard ticket price; -late ticket - additional 10%
# to the reguler ticket price. All tickets must have the following properties: -the ability to construct a ticket by
# number; -the ability to ask for a ticket’s price; -the ability to print a ticket as a String.

# Write a program for selling tickets to IT-events. Each ticket has a unique number and a price. There are four type_ts
# of tickets: standard ticket, advance ticket (purchased 60 or more days before the event), late ticket (purchased
# fewer than 10 days before the event) and student ticket. Additional information: -advance ticket - discount 40% of
# the standard ticket price; -student ticket - discount 50% of the standard ticket price; -late ticket - additional 10%
# to the regular ticket price. All tickets must have the following properties: -the ability to construct a ticket by
# number; -the ability to ask for a ticket’s price; -the ability to print a ticket as a String.

import json  # типи білетів мають бути окремо від класу Event


class Events:

    def __init__(self, name_of_file, name, tickets, price):
        # self.price_student = round(price * 0.5)  # студентський (ОКРЕМО)
        # self.advance_price = round(price * 0.6)  # завчасно куплений
        # self.late_price = round(price * 1.1)  # куплено запізно
        self.name_of_file = name_of_file
        self.name = name
        self.tickets = tickets
        self.price = price
        self.current = tickets
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
    def tickets(self):
        return self.__tickets

    @tickets.setter
    def tickets(self, tickets):
        if not isinstance(tickets, int):
            raise TypeError()
        if tickets <= 0:
            raise ValueError()
        self.__tickets = tickets

    def add_event(self):  # add to .json file

        event = {
            "Name of file": self.name_of_file,
            "Name": self.name,
            "Tickets": self.tickets,
            "Price": self.price,
            }
        with open(self.name_of_file, "w") as write_file:
            json.dump(event, write_file)
        write_file.close()

    def __str__(self):
        return f"Event: \n" \
               f"{self.__tickets} tickets, price - {self.__price}"

    num_standard = 0
    num_st = 0
    num_advance = 0
    num_late = 0


class Tickets:

    file_tickets = []

    def __init__(self, event, number, days, price, type_t="Standard ticket"):
        self.event = event
        self.number = number
        self.days = days
        self.price = price
        self.type_t = type_t
        event.num_standard += 1
        event.current -= 1
        if not event.current:
            raise ValueError("No more tickets.")
        Tickets.add_ticket(self)



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

    @staticmethod
    def standard_price(name_of_file):
        with open(name_of_file, "r") as read_file:
            info = json.load(read_file)
        return info.get("Price")

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
               f" price - {int(self.price)}, bought {self.days} days before the event"

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


class Student(Tickets):

    def __init__(self, event, number, days, price):
        with open(event.name_of_file, "r") as read_file:
            info = json.load(read_file)
        super().__init__(event, number, days,  price * 0.5, "Student ticket")
        event.num_st += 1


class Advance(Tickets):

    def __init__(self, event, number, days, price):
        if days < 60:
            raise ValueError()
        with open(event.name_of_file, "r") as read_file:
            info = json.load(read_file)
        super().__init__(event, number, days, price * 0.6, "Advance ticket")
        event.num_advance += 1


class Late(Tickets):

    def __init__(self, event, number, days, price):
        if days > 10:
            raise ValueError()
        with open(event.name_of_file, "r") as read_file:
            info = json.load(read_file)
        super().__init__(event, number, days, price * 1.1, "Late ticket")
        event.num_late += 1


def main():
    try:
        event_1 = Events("event1.json", "Business Analyst course", 10, 700)
        print(event_1)

        first_price = Tickets.standard_price(event_1.name_of_file)
        ticket_1 = Tickets(event_1, 1, 15, first_price)
        ticket_2 = Tickets(event_1, 2, 16, first_price)
        print("Received a ticket by number:")
        print(Tickets.get_num(event_1, 2))
        print()
        ticket_3 = Late(event_1, 3, 2, first_price)
        ticket_4 = Advance(event_1, 4, 70, first_price)
        ticket_5 = Student(event_1, 5, 10, first_price)
        ticket_6 = Advance(event_1, 6, 67, first_price)
        ticket_7 = Student(event_1, 7, 14, first_price)

        print("All tickets:")
        print(ticket_1)
        print(ticket_2)
        print(ticket_3)
        print(ticket_4)
        print(ticket_5)
        print(ticket_6)
        print(ticket_7)

        print("\nGet price by number:")
        print(Tickets.get_price(event_1, 5))

    except Exception:
        print("Exeption!")


main()
