
#customer class
class Customer:
    def __init__(self,name,address,phone):
        self.name = name
        self.address= address
        self.phone = phone

    def get_name(self):
        return self.name
    
    def get_address(self):
        return self.address 
    
    def get_phone(self):
        return self.phone 


#car class
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model= model
        self.year = year
    
    def get_make(self):
        return self.make
    
    def get_model(self):
        return self.model 
    
    def get_year(self):
        return self.year

#service quote class
class ServiceQuote:
    def __init__(self,parts,labor):
        self.parts = parts
        self.labor = labor 
   
    def get_parts(self):
        return self.parts
    
    def get_labor(self):
        return self.labor
    
    def get_tax(self):
        sub_total = self.parts + self.labor
        tax = sub_total * .0825
        return tax
    
    def get_total(self):
        sub_total = self.parts + self.labor
        tax = sub_total * .0825
        total = self.parts + self.labor + tax
        return total
