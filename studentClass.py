
from datetime import date

class Student:

    def __init__(self,id,name,bod,classification):
        self.studentid = id
        self.__name = name
        self.__dob = dob
        self.__classification = classification
        self.__age = 0
        self.__register = ''

    def calc_age(self):
        today = date.today()
        today_year = today.year
        dob = self.__dob.split('/') #creates a list of 3 elements
        dob_year = int(dob[2]) #grabs the year
        self.__age = today.year - dob_year
    
    def calc_register(self):
         if self.__classification == 'senior':
            self.__register = '4/1 thru 4/3'
         elif self.__classification == 'junior':
            self.__register = '4/14 thru 4/6'
         elif self.__classification == 'sophomore':
            self.__register = '4/7 thru 4/9'
         elif self.__classification == 'freshmen':
            self.__register = '4/10 thru 4/12'
         else:
            self.__register = 'Classification not found'
            
    def get_age(self):
        return self.__age
    
    def get_register(self):
        return self.__register 



