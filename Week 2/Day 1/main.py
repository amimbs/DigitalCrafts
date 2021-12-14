shopping_lists = []

# class so we can item single items
class GroceryItem:
    def __init__(self, name):
        self.name = name

# class that holds the list the the above class can add it's onjects too
class GroceryStoreList:
    def __init__(self, store):
        self.store = store
        self.groceryitems = []

    def add_grocery_items(self, item):
        self.groceryitems.append(item)

    def display_grocery(self):
        for item in range(0, len(self.groceryitems)):
            print(f"{self.groceryitems[item].name}")
            

print("1. Add a shopping list")
print("2. add item to an existing shopping list")
print("3. display shopping lists")
print("Or type quit")

choice = input("Enter choice: ")

if choice == "1":
    grocery_store = GroceryStoreList(input("Input the name of the store: "))
    while True:
        user_input = input("list the item: ")
        if user_input == "quit":
            break
        else:
            item = GroceryItem(user_input)
            grocery_store.add_grocery_items(item)
    
    shopping_lists.append(grocery_store)
        
    # elif choice == "3":
    # print(f"{grocery_store.name} {grocery_store.groceritems}"
    

#print (f"{storename.store}:{storename.display_grocery()}")


    





# store = GroceryStoreList("walmart")

# store.add_grocery_items(GroceryItem("eggs"))
# store.add_grocery_items(GroceryItem("dog"))
# store.add_grocery_items(GroceryItem("cats"))


# store.display_grocery()
