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
menu_dictionary = {}

# Add Header as key and remaining items as list of values
for column in range(menu.col_count):
    #print(column)
    #print(menu.col_values(column+1)[0]) #key value
    #print(menu.col_values(column+1)[1:]) #key list
    menu_dictionary[menu.col_values(column+1)[0]] = menu.col_values(column+1)[1:]

#pprint.pp(menu_dictionary)

class pizza_obj:
    """
    Creates an instance of Pizza
    """
    def __init__(self, name, price, toppings, size="standard", base="normal"):
        self.name  = name
        self.price = price
        self.toppings = toppings
        self.size = size
        self.base = base

class order:
    pass

def welcome():
    """
    Welcome function to gather Customer Name
    """
    print("Welcome to Artisan-Pizza - Where Artisan Craftsmanship Meets Your Cravings!")
    customerdata=["name","number"]
    while True:
        customerdata[0] = input("Please enter your name: \n")
        if customerdata[0].isalpha():
            break
        else:
            print("\nPlease check your name, only [A-Z] characters are accepted")

    while True:
        customerdata[1] = input("Please enter your phone number: \n")
        if customerdata[1].isdigit():
            break
        else:
            print("\nPlease check your phone number, only [0-9] characters are accepted")    
    
    return customerdata

def show_menu():
    """
    Print the whole menu read previously from google sheet and give option to select pizza
    """
    os.system('clear')
    print("\nHere our pizza menu:")
    for i in menu_dictionary:
        # Print header from google sheet and first list element, containing the price
        print(f"\n{i}: {menu_dictionary[i][0]}€")
        # Print all other list elements (ingredients/toppings)
        print(*menu_dictionary[i][1:], sep=", ")     


def select_pizza_size():
    """
    Function to select the pizza size
    """
    while True:
        pizza_base = input("Please select the pizza you'd like to order: \n")
        if selected_pizza in menu_dictionary or selected_pizza == "Extra Toppings":
            break
        else:
            print("\nInvalid input, please try again\n")

    return pizza_base


def build_pizza():
    """
    Function to select the pizza from Menu
    """
    while True:
        selected_pizza = input("Please select the pizza you'd like to order: \n")
        if selected_pizza in menu_dictionary or selected_pizza == "Extra Toppings":
            break
        else:
            print("\nCannot find the pizza you typed, please try again\n")

    pizza = pizza_obj(selected_pizza,menu_dictionary[selected_pizza][0],menu_dictionary[selected_pizza][1:])
    print("Selected pizza:")
    print(pizza)
    print(pizza.name)
    print(pizza.price)
    print(pizza.toppings)
    print(pizza.base)
    print(pizza.size)
    return pizza


def main():
    """
    Main function
    """
    customer = welcome()
    show_menu()
    pizza = build_pizza()


main()
