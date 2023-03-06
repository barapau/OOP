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

#service quote class
class ServiceQuote:
    def __init__(self,part_charges, labor_charges):
        self.part_charges = part_charges
        self.labor_charges= labor_charges
    
    def get_parts_charges(self):
        return self.part_charges

    def get_labor_charges(self):
        return self.labor_charges
    
    def get_tax(self):
        total = self.part_charges + self.labor_charges
        tax = total * 0.825
        return tax
    
    def get_total(self):
        total = self.part_charges + self.labor_charges
        tax = total * 0.825
        total1 = self.part_charges + self.labor_charges + tax
        return total1
    
    def get_tax(self):
        return self.tax
    
    def get_charges(self):
        return self.get_charges
    
    def get_sales_tax(self):
        return self.parts * .0825


    
    def set_year(self):
        return self.__year
        

    
