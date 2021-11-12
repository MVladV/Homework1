# task1

# pass the list of arguments from the console
import sys 
# calculation of mathematical expression
try:
    print(eval(' '.join(sys.argv[1]+sys.argv[2]+sys.argv[3]))) 
except Exception:
    print("Exeption!")

#grgrgr
class student:
    def __init__(self, name, surname, **kwargs):
        self.name = name
        self.surname = surname
        for key in kwargs.keys():
            self.__dict__[key] = kwargs[key]

    def __str__(self):
        return ', '.join(list(map(str, list(self.__dict__.items())))) + '.'


class main():
    person1 = student("Tom", "Kuper", weight=24)
    print(person1.weight)
    print(person1)
main()

class rectangle:
    def __init__(self, a, b,):
        self.a = a
        self.b = b

    def setter:


