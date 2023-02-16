import InsectClass as I

#this is creating an instance of the insect class
mosquito = I.Insect('mosquito',2,4) #the init method parameters need to be there
housefly = I.Insect('housefly',2,4) #if classfile has 3, thy need to be 3

mosquito.flight_lenght()
housefly.flight_lenght()

print(f"The {mosquito.get_name()} can fly up to {mosquito.get_miles()} miles")
print(f"The {housefly.get_name()} can fly up to {mosquito.get_miles()} miles")