import pprint
import os
import gspread
import shortuuid
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('artisan_pizza')


def read_menu():
    print("Please wait while we load our pizzas menu...")
    menu = SHEET.worksheet('menu')
    menu_dict = {}
    for column in range(menu.col_count):
        menu_dict[menu.col_values(column+1)[0]] = menu.col_values(column+1)[1:]
    return menu_dict


class pizza_obj:
    """
    Creates an instance of Pizza
    """
    def __init__(self, index, name, price, toppings, extratoppings=[],
                 size="standard", base="normal"):
        self.index = index
        self.name = name
        self.price = float(price)
        self.toppings = toppings
        self.extratoppings = extratoppings
        self.size = size
        self.base = base


class order_obj:
    """
    Creates an instance of Order
    """
    def __init__(self, id, pizzalist, totalprice):
        self.id = id
        self.pizzalist = pizzalist
        self.totalprice = float(totalprice)


def welcome():
    """
    Welcome function to gather Customer Name
    """
    print("Welcome to Artisan-Pizza")
    print("Where Artisan Craftsmanship Meets Your Cravings!")
    customerdata = ["name", "number"]
    while True:
        customerdata[0] = input("Please enter your name: \n")
        if customerdata[0].isalpha():
            break
        else:
            print("Please check the input, only [A-Z] characters are accepted")

    while True:
        customerdata[1] = input("Please enter your phone number: \n")
        if customerdata[1].isdigit():
            break
        else:
            print("Please check the input, only [0-9] characters are accepted")
    return customerdata


def show_menu(menu_dict):
    """
    Print the whole menu read previously from google sheet and give option
    to select pizza
    """
    os.system('clear')
    print("\nHere our pizza menu:")
    for i in menu_dict:
        """
        Print header from google sheet and first list element,
        containing the price
        """
        if menu_dict[i][0] != "Extra Toppings":
            print(f"\n{i}: {menu_dict[i][0]} - {menu_dict[i][1]}€ - ", end='')
            """
            Print all other list elements (ingredients/toppings)
            """
            print(*menu_dict[i][2:], sep=", ")


def select_pizza_base(pizza):
    """
    Function to select the pizza base
    """
    os.system('clear')
    while True:
        print("Please select the pizza base: ")
        print('Normal Dough')
        print('Glutenfree - +2.5€')
        print('Whole Wheat - +1.5€')
        pizza_base = input("[N/G/W]): \n").lower()
        match pizza_base:
            case "n":
                pizza.base = "Normal"
                break
            case "g":
                pizza.base = "Glutenfree"
                pizza.price += 2.5
                break
            case "w":
                pizza.base = "Whole Wheat"
                pizza.price += 1.5
                break
            case _:
                print("Invalid input, please try again\n")


def select_pizza_size(pizza):
    """
    Function to select the pizza size
    """
    os.system('clear')
    while True:
        print("Please select the pizza size: ")
        print('Standard - 10"')
        print('Large - 12": +1€')
        print('Extra Large - 14": +2€')
        pizza_size = input("[S/L/XL]): \n").lower()
        match pizza_size:
            case "s":
                pizza.size = "Standard"
                break
            case "l":
                pizza.size = "Large"
                pizza.price += 1
                break
            case "xl":
                pizza.size = "Extra Large"
                pizza.price += 2
                break
            case _:
                print("Invalid input, please try again\n")


def add_extra_toppings(pizza, extratoppings):
    """
    Function to add extra toppings to pizza.extratoppings attribute
    """
    os.system('clear')
    toppings_list = extratoppings[2:]
    """Removing existing toppings from the list"""
    toppings_list = [i for i in toppings_list if i not in pizza.toppings]
    while True:
        extra_toppings_choice = input(f"Do you want to add extra toppings "
                                      f"for {extratoppings[1]}€ each (Y/N)?\n")
        extra_toppings_choice.lower()
        match extra_toppings_choice:
            case "y":
                os.system('clear')
                print("Extra toppings available:")
                for (i, topping) in enumerate(toppings_list, start=1):
                    print(f"{i} - {topping}")
                while True:
                    topping_choice = int(input("\nSelect extra topping:\n"))-1
                    print("\n")
                    if (topping_choice < len(toppings_list)
                            and topping_choice >= 0):
                        break
                    else:
                        print("Invalid input, please try again\n")
                pizza.extratoppings.append(toppings_list[topping_choice])
                pizza.price = round(pizza.price + 1.2, 2)
                toppings_list.pop(topping_choice)
                """Check if extra topping list is empty """
                if toppings_list == []:
                    print("No more toppings available")
                    break
            case "n":
                break
            case _:
                print("Invalid input, please try again\n")


def build_pizza(menu_dict):
    """
    Function to select and build the pizza from Menu
    """
    while True:
        pizza_choice = input("\nPlease select the pizza to order: \n")
        print("\n")
        if pizza_choice in menu_dict and int(pizza_choice) != len(menu_dict):
            break
        else:
            print("Cannot find your pizza in the menu, please try again")
    pizza = pizza_obj(pizza_choice, menu_dict[pizza_choice][0],
                      menu_dict[pizza_choice][1],
                      menu_dict[pizza_choice][2:])
    select_pizza_base(pizza)
    select_pizza_size(pizza)
    """Creating list with Extra toppings.
    position is in the last colum of spreadsheet"""
    extra_toppings_list = menu_dict[str(len(menu_dict))]
    add_extra_toppings(pizza, extra_toppings_list)
    return pizza

def build_order():
    orderid = (str(shortuuid.ShortUUID().random(length=12)).upper())
    order = order_obj(orderid,[],0)
    menu_dict = read_menu()
    while True:
        show_menu(menu_dict)
        pizza = build_pizza(menu_dict)
        while True:
            pizza_qty = int(input("\nHow many of these pizza [1-5]?:\n"))
            if pizza_qty >=1 and pizza_qty <=5:
                break
            else:
                print("Invalid input, please try again\n")        
        for i in range(pizza_qty):
            order.pizzalist.append(pizza)
            order.totalprice += pizza.price
        while True:
            another_pizza = (input("\nDo you want to add another pizza? [Y/N]\n").lower())
            match another_pizza:
                case "y":
                    break
                case "n":
                    return order
                case _:
                    print("Invalid input, please try again\n")


def main():
    """
    Main function
    """
    os.system('clear')
    customer = welcome()
    customer_order = build_order()
    print("\n Main pprint order:")
    pprint.pprint(vars(customer_order))
    pprint.pprint(customer_order.pizzalist)


main()
