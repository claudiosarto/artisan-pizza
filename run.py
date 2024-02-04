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
"""
for column in range(menu.col_count):
    #print(menu.col_values(column+1)[0]) #key value
    #print(menu.col_values(column+1)[1:]) #key list
    menu_dictionary[menu.col_values(column+1)[0].lower()] = menu.col_values(column+1)[1:]
"""
#pprint.pp(menu_dictionary)



def welcome():
    """
    Welcome function to gather Customer Name
    """
    print("Welcome to Artisan-Pizza - Where Artisan Craftsmanship Meets Your Cravings!")
    while True:
        customername = input("Please enter your name: \n")
        if customername.isalpha():
            break
        else:
            print("\nPlease check your name, only characters [A-Z] are accepted")
    return customername

def main():
    customer=welcome()

main()
