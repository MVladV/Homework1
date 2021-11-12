import pandas as pd
import datetime


class Pizza:

    def __init__(self):
        self.products = [
            "Бекон",
            "Сир",
            "Кукурудза",
            "Ананас",
            "Перець",
            "Оливи",
            "Печериці",
            "Помідор"]
        self.pizzas = [
            "Папероні",
            "Сицілійська",
            "Чотири сири",
            "М'ясна",
            "Мексикано",
            "Баварська",
            "Шеф-піца"]
        self.total_bill = 0.0

    def start(self):

        df = pd.DataFrame(self.pizzas, columns=["Pizzas"])
        df.loc[:4, "Prices"] = 12.50  # First 4 items.
        df.loc[4:, "Prices"] = 20.30  # All the rest.
        df.index += 1  # So that it's not zero-indexed.

        print("Welcome to Pizza Planet!\n")  # So unoriginal, I know.
        print("Today we want to offer you a delicious pizza of the day!\n")
        day = datetime.datetime.today().weekday()
        print(self.pizzas[int(day)])
        answer = input("If you agree, input yes. Else input no.\n")
        if answer == 'yes':
            price = df.loc[int(day), "Prices"]
            self.total_bill += price
            print("Great, do you want to complement your pizza?")
            answer = input("If you agree, input yes. Else input no.\n")
            if answer == 'yes':
                self.add()
        elif answer == 'no':
            print("Goodbye...")

    def add(self):

        df = pd.DataFrame(self.products, columns=["Products"])
        df.loc[:4, "Prices"] = 1.50  # First 4 items.
        df.loc[4:, "Prices"] = 2.50  # All the rest.
        df.index += 1  # So that it's not zero-indexed.
        print("Here's our menu!\n")
        print(df.to_string(justify='left',
                           header=False,
                           formatters={
                               'Products': '{{:<{}s}}'.format(
                                   df['Products'].str.len().max()
                               ).format,
                               'Prices': '     ${:.2f}'.format}))

        print("Input a number and press enter to select an item.")
        print("Input 'done' to finish your order and tabulate your bill.")
        print("Input 'exit' to cancel your orders.")

        while True:

            order = input(">>>  ")

            if order == 'exit':
                break
            elif order == 'done':
                print("Your total bill is ${:.2f}.".format(self.total_bill))
                input("Press any key to exit.")
                break
            elif int(order) in df.index:
                item = df.loc[int(order), "Products"]  # Get the respective items
                price = df.loc[int(order), "Prices"]  # by indexing order input.
                print("You've selected {}! That would be ${:.2f}.".format(item, price))
                self.total_bill += price
                continue
            else:
                print("Error!")
                input("Press any key to exit.")
                break


def main():
    try:
        my_rect = Pizza()
        my_rect.start()
    except Exception:
        print("Exeption!")


main()
