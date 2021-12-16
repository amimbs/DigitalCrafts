
class Address:
    def __init__ (self, street, city, state):
        self.street = street
        self.city = city
        self.state = state


class User:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
        # self.address = Address()
        # we can also set a class as an array
        self.addresses = []

    def add_address(self, address):
        self.addresses.append(address) # here we're adding address objects to the addresses array

user = User("John", "Doe")
# use dot notation to access a class within a class
# user.address.street = "1200 Richmond"
# user.address.city = "Houston"
# user.address.state = "Texas"
user.add_address(Address("1200 Richmond", "Houston", "TX")) # here we pass in objects using the class constructor for the argument variable of address (line 18)
user.add_address(Address("456 Road", "Austin", "Texas"))

print(user.f_name)
print(user.l_name)
# How should we print our adresses
print(user.addresses)

for address in user.addresses: # address is an object because addresses is an array
    print(address.street)
    print(address.city)
    print(address.state)

class Post:
    def __init__(self, title, description, author):
        self.title = title
        self.description = description
        self.author = author
        self.comments = [] # one post can have many comments
