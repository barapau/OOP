import JoeClass as jc

name = 'John Doe'
address = '123 Main St. Waco TX 76706'
phone = 214-555-1112
make = 'Honda'
model = 'Accord LX'
year = 2016
parts = 1,210.50
labor = 765

customer = jc.Customer(name, address, phone)
car = jc.Car(make, model, year)
#service_quota = (parts, labor)

print('Customer:', customer.get.name(), '   ', 'Address:', customer.get.address(), '   ', 'Phone:', customer.get.phone())
print('Car Make:', car.get.make(), '   ', 'Car Model:', customer.get.model(), '   ', 'Car year:', car.get.year())
print('Service Quote')
print('Parts:')
print('Labor:')
print('Sales Tax:')
print('Total Charges:')