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

menu = SHEET.worksheet('menu')

# Define empty menu dictionary
menu_dict = {}

# Add Header as key and remaining items as list of values
for column in range(menu.col_count):
    """print(column)
    print(menu.col_values(column+1)[0]) #key value
    print(menu.col_values(column+1)[1:]) #key list"""
    menu_dict[menu.col_values(column+1)[0]] = menu.col_values(column+1)[1:]

"""pprint.pp(menu_dict)"""


class pizza_obj:
    """
    Creates an instance of Pizza
    """
    def __init__(self, name, price, toppings, extratoppings=[],
                 size="standard", base="normal"):
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


def show_menu():
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
        print(f"\n{i}: {menu_dict[i][0]}€ - ", end='')
        """
        Print all other list elements (ingredients/toppings)
        """
        print(*menu_dict[i][1:], sep=", ")


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


def select_pizza_size():
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
                return "Standard"
                break
            case "l":
                return "Large"
                break
            case "xl":
                return "Extra Large"
                break
            case _:
                print("Invalid input, please try again\n")


def build_pizza():
    """
    Function to select and build the pizza from Menu
    """
    while True:
        selected_pizza = input("\nPlease select the pizza to order: \n")
        print("\n")
        if selected_pizza in menu_dict or selected_pizza == "Extra Toppings":
            break
        else:
            print("\nCannot find your pizza in the menu, please try again\n")

    pizza = pizza_obj(selected_pizza, menu_dict[selected_pizza][0],
                      menu_dict[selected_pizza][1:])
    pizza.base = select_pizza_base(pizza)
    pizza.size = select_pizza_size()
    print("Selected pizza:")
    pprint.pprint(vars(pizza))
    return pizza


def main():
    """
    Main function
    """
    os.system('clear')
    customer = welcome()
    show_menu()
    pizza = build_pizza()


main()
