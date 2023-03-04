#customer class
class Customer:
    def __init__(self,name,address,phone):
        self.__name = name
        self.__address= address
        self.__phone = phone

    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address 
    
    def get_phone(self):
        return self.__phone 

    def set_name(self):
        return self.__name
    
    def set_address(self):
        return self.__address
    
    def set_phone(self):
        return self.__phone


#car class
class Car:
    def __init__(self,make,model,year):
        self.__make = make
        self.__model= model
        self.__year = year
    
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model 
    
    def get_year(self):
        return self.__year

    def set_make(self):
        return self.__make
    
    def set_model(self):
        return self.__model
    
    def set_year(self):
        return self.__year

#service quote class
class ServiceQuote:
    def __init__(self,part_charges, labor_charges):
        self.__part_charges = part_charges
        self.__labor_charges= labor_charges
    
    def set_parts_charges(self):
        return self.__year

    def set_make(self):
        return self.__make
    
    def set_model(self):
        return self.__model
    
    def set_year(self):
        return self.__year
        

    
