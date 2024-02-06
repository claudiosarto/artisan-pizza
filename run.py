import pprint
import os
import gspread
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


class order:
    pass


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
                pizza.price +=2.5
                break
            case "w":
                pizza.base = "Whole Wheat"
                pizza.price +=1.5
                break
            case _:
                print("Invalid input, please try again\n")


def select_pizza_size(pizza):
    """
    Function to select the pizza size
    """
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
                pizza.price +=1
                break
            case "xl":
                pizza.size = "Extra Large"
                pizza.price +=2                   
                break
            case _:
                print("Invalid input, please try again\n")


def add_extra_toppings(pizza,extratoppings):

    pass


def build_pizza(menu_dict):
    """
    Function to select and build the pizza from Menu
    """
    while True:
        selected_pizza = input("\nPlease select the pizza to order: \n")
        print("\n")
        if selected_pizza in menu_dict and int(selected_pizza) != 7:
            break
        else:
            print("\nCannot find your pizza in the menu, please try again\n")
    pizza = pizza_obj(selected_pizza, menu_dict[selected_pizza][0],menu_dict[selected_pizza][1],menu_dict[selected_pizza][2:])
    """ 
    print("Build pizza pizza:")
    pprint.pprint(vars(pizza))
    """
    select_pizza_base(pizza)
    select_pizza_size(pizza)
    return pizza

def main():
    """
    Main function
    """
    os.system('clear')
    customer = welcome()
    menu_dict = read_menu()
    show_menu(menu_dict)
    pizza = build_pizza(menu_dict)
    print("\n Main pprint pizza:")
    pprint.pprint(vars(pizza))


main()
"""
menu_test = read_menu()
pprint.pprint(menu_test)
"""