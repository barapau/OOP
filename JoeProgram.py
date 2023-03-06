import JoeClass as jc

name = 'John Doe'
address = '123 Main St. Waco TX 76706'
phone = '214-555-1112'
make = 'Honda'
model = 'Accord LX'
year = 2016


customer = jc.Customer(name, address, phone)
car = jc.Car(make, model, year)
service_quote = jc.ServiceQuote(1210.50, 765.00)

print('Customer:', customer.get_name(), '  ', 'Address:', customer.get_address(), '  ', 'Phone:', customer.get_phone())
print()
print('Car Make:', car.get_make(), '  ', 'Car Model:', car.get_model(), '  ', 'Car year:', car.get_year())
print()
print('Service Quote')
print()
print('Parts: $', format(service_quote.get_parts(), ',.2f'), sep ='')
print()
print('Labor: $', format(service_quote.get_labor(), ',.2f'), sep ='')
print()
print('Sales Tax: $',format(service_quote.get_tax(), ',.2f'), sep ='')
print()
print('Total Charges: $', format(service_quote.get_total(), ',.2f'), sep ='')