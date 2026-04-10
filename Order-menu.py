# Veg Menu
veg_menu = {
    "idli": 30,
    "dosa": 50,
    "veg biryani": 120
}

# Non-Veg Menu
nonveg_menu = {
    "chicken biryani": 180,
    "egg rice": 100,
    "chicken curry": 200
}

# Cold Drinks Menu
drinks_menu = {
    "coke": 40,
    "sprite": 40,
    "water": 20
}

# Function to show menu
def show_menu():
    print("\n------ VEG MENU ------")
    for item,price in veg_menu.items():#item is used to store both key and pair value
      print(item, ":", price)#item=key,price=value

    print("\n------ NON-VEG MENU ------")
    for item, price in nonveg_menu.items():
        print(item, ":", price)

    print("\n------ DRINKS MENU ------")
    for item, price in drinks_menu.items():
        print(item, ":", price)


# Function to take order
def take_order():
    total = 0

    while True:#run loop infinite times
        item = input("\nEnter item name : ").lower()#lower to avoid confiusion

        if item == "exit":
            break

        # Check item in all menus
        if item in veg_menu:
            total += veg_menu[item]
            print("Added", item)

        elif item in nonveg_menu:
            total += nonveg_menu[item]
            print("Added", item)

        elif item in drinks_menu:
            total += drinks_menu[item]
            print("Added", item)

        else:
            print("Item not found!")

    print("\nTotal bill:", total)


# Main program
print("Welcome to Food Ordering System 🍴")
show_menu()
take_order()