class Item: #This is the Item object
    def __init__(self, name, quantity): #Initialization of Item name and quantity
        self.name = name
        self.quantity = quantity

    def add_quantity(self, amount): #Adding the quantity of the Item
        self.quantity = amount + self.quantity

    def update_quantity(self, amount): #Updating the quantity of the Item
        self.quantity = amount
    
    def display_details(self): #Displaying the details of the Item
        print("Name:", self.name)
        print("Quantity:", self.quantity)
    
class Inventory: #This is the Inventory object
    def __init__(self): #Initialization of Inventory list
        self.itemList = []
        pass

    def add_item(self, name, quantity): #Adding item to the inventory
        self.itemList.append(Item(name,quantity))

    def find_item(self, name): #Finding item in the inventory
        for item in self.itemList:
            if(len(self.itemList) == 0):
                print("Inventory Empty!")
            else:
                if(item.name == name):
                    print("Name:", item.name)
                    print("Quantity:", item.quantity)
                else:
                    print("Item not found!")

    def update_item(self, name, quantity): #Updating item from the inventory
        if(len(self.itemList) == 0):
                print("Inventory Empty!")
        else:
            counter = 0
            for item in self.itemList:
                counter = counter + 1
                if(item.name == name):
                    item.quantity = quantity
                    print("Item quantity updated!")
                elif(counter == len(self.itemList)):
                    print("Item not found!")
    
    def generate_report(self): #Generating reports such as the number of items in the inventory, their name and quantity.
        counter = 1
        for item in self.itemList:
            print("Item", counter)
            print("Name:", item.name)
            print("Quantity:", item.quantity)
            counter = counter + 1

    def load_data(self, filename): #Loading the saved data
        counter = 1
        try:
            with open(filename, 'r') as file:
                data = file.readlines()
                for line in data:
                    print("Item", counter, ":", line.rstrip())
                    counter = counter + 1
        except IOError:
            print("Error: could not read file", filename)

    def save_data(self, filename): #Saving the data from the inventory
        try:
            with open(filename, 'w+') as file:
                for line in self.itemList:
                    name = line.name
                    quantity = str(line.quantity)
                    file.write("%s\n" % (name + "," + quantity))
            print("Inventory saved.")
        except IOError:
            print("Error: could not save file", filename)
        
inv = Inventory() 

choice = 0

while(choice != 5): #Loop for the Menu
    print("1 - Add an item")
    print("2 - Update an item")
    print("3 - Generate a report")
    print("4 - Save the data")
    print("5 - Exit")
    choice = int(input('Enter Choice: '))

    if(choice == 1):
        print("Add an item")
        name = input("Enter item name: ")
        quantity = int(input("Enter item quantity: "))
        inv.add_item(name,quantity)
        print("Item added!")
    
    elif(choice == 2):
        print("Update an item")
        name = input("Enter item name: ")
        quantity = int(input("Enter item quantity: "))
        inv.update_item(name,quantity)

    elif(choice == 3):
        print("Generate a report")
        inv.generate_report()

    elif(choice == 4):
        inv.save_data("inventory.txt")
        inv.load_data("inventory.txt")
    
    elif(choice < 5):
        print("Input invalid!")