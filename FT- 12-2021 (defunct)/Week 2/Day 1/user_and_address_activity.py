# Activity 

# Create a class called User which consists of (first_name, last_name) properties. Create a class name Address which consists of (street, city, state, zip_code) properties.

#         Create a relationship between User and Address in a way a single user can have multiple addresses.
#         Add a new method/function to User class called add_address(self, address) which would take an address as an argument and add it to a list/array of addresses.
#         Add another method to the User class called display_addresses(self) which would display all the address of that user.


class Address:
    def __init__ (self, street, city, state, zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

class User:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
        self.addresses = []

    def add_address(self, address):
        self.addresses.append(address)
    
    def display_address(self):
        print(f"{user.f_name} {user.l_name}")
        for address in self.addresses:
            print(address.street)
            print(address.city)
            print(address.state)

user = User("Andy", "Mimbs")
user.add_address(Address("123 RD", "Atlanta", "Georgia", "30338"))
user.add_address(Address("456 Rd", "Atlanta", "GA", "30336"))

user.display_address()


