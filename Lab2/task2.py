import sys
import os.path
import re

class line:

    def __init__(self, file):
        
        self.file = file
        self.__letters = 0
        self.__words = 0
        self.__sent = 0 

    @property
    def file(self):  
        return self.__file

    @file.setter
    def file(self, file):
        check_file = os.path.exists('text.txt')
        if check_file:
            FileNotFoundError() 
        self.__file = file 

    def get_info(self): 
        data = self.file.read() 
        self.__words = len({x for x in re.findall(r'[A-z\']+', data)}) 
        self.__letters = len(data)
        new_text = re.sub(r'[.!?]\s', r'|', data)
        self.__sent = len(new_text.split('|'))
 
            
    def __str__(self):
        return f'Words = {self.__words}\nLetters = {self.__letters} \nSentences = {self.__sent}'                 

class main:
    try:
        file = open("text.txt", "rt")
        work = line(file)
        work.get_info()
        print(work)
    except Exception:
        print("Exeption!")
main()       
