import JoeClass as jc

name = 'John Doe'
address = '123 Main St. Waco TX 76706'
phone = 214-555-1112
make = 'Honda'
model = 'Accord LX'
year = 2016
parts = 1,210.50
labor = 765

car = jc.Car(make, model, year)
customer = jc.Customer(name, address, phone)
service_quota = (parts, labor)
