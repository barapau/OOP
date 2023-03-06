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
    

    
