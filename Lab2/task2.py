import sys
import os.path

class line:

    def __init__(self, file):
        if not isinstance(file, str):
            raise TypeError()     
        else:
            self.__file = file
        self.__lines = 0
        self.__letters = 0
        self.__words = 0

    def get_info(self):
        for line in open(self.__file):
            self.__lines += 1
            self.__letters += len(line)

        pos = 'out'
        for letter in line:
            if letter != ' ' and pos == 'out':
                self.__words += 1
                pos = 'in'
            elif letter == ' ':
                pos = 'out'

    def __str__(self):
        return f'Lines = {self.__lines}\nWords = {self.__words}\nLetters = {self.__letters}'                 

class main:
    try:
        check_file = os.path.exists('text.txt')
        if check_file:
            FileNotFoundError()
        fname = sys.argv[1]
        work = line(fname)
        work.get_info()
        print(work)
    except Exception:
        print("Exeption!")
main()       