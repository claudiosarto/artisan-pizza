import pprint
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


class pizza:
    pass    

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
    print("\nHere our pizza list and related included toppings:")
    for i in menu_dictionary:
        print(f"\n{i}: ")
        print(*menu_dictionary[i], sep=", ")

def main():
    customer=welcome()
    show_menu()

main()
