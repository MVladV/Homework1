import sys
import os.path
import numpy as np

class STUDENT:

    def __init__(self, name, surname, num_book, grades):

        self.name = name
        self.surname = surname
        self.num_book = num_book
        self.grades = grades
        self.gpa = sum(self.__grades) / len(self.__grades)  
        
    @property
    def name(self):  
        return self.__name

    @name.setter
    def name(self, name):
        if not name:
            raise TypeError()        
        if not isinstance(name, str):
            raise TypeError()
        self.__name = name   

    @property
    def surname(self):  
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not surname:
            raise TypeError()
        if not isinstance(surname, str):
            raise TypeError()
        self.__surname = surname 

    @property
    def num_book(self):  
        return self.__num_book

    @num_book.setter
    def num_book(self, num_book):
        if not isinstance(num_book, int):
            raise TypeError()
        self.__num_book = num_book      

    @property
    def grades(self):  
        return self.__grades

    @grades.setter
    def grades(self, grades):
        if not isinstance(grades, list):
            raise TypeError()
        self.__grades = grades             

    def __str__(self):
        return f'Name = {self.__name}\nSurname = {self.__surname}\nNumber = {self.__num_book}\nGrades: {self.__grades}'                 

class GROUP:
    
    def __init__(self, *args):
        self.pupils = args

    @property
    def pupils(self):
        return self.__pupils        

    @pupils.setter
    def pupils(self, pupils):
        if any(not isinstance(pupil, STUDENT) for pupil in pupils):
            raise TypeError()
        if len(pupils) > 20:
            raise TypeError()    
        self.__pupils = list(pupils) 
        
    def best_st(self):
        sorted(self.pupils, key=lambda x: x.gpa)
        n = len(self.pupils)
        return self.pupils[n-5:]

class main:
    try:
        st1 = STUDENT("Vlad", "Mitl", 1, [8, 5, 6, 3])
    
        st2 = STUDENT("Vlad", "Mitl", 2, [7, 5, 6, 9])
      
        st3 = STUDENT("Alex", "Drain", 3, [5, 2, 7, 3])
   
        st4 = STUDENT("Rita", "Brawl", 4, [8, 9, 6, 3])
     
        st5 = STUDENT("Oleh", "Tiro", 5, [8, 9, 10, 10])
   
        st6 = STUDENT("Max", "Drue", 6, [7, 5, 10, 2])
   
        st7 = STUDENT("Mira", "Temp", 7, [5, 9, 6, 8])

        gr = GROUP(st1, st2, st3, st4, st5, st6, st7)
        best_five = gr.best_st()
        for i in range(5):
            print(str(best_five[i]))
    except Exception:
        print("Exeption!")
main()       
