# Artisan Pizza

Artisan pizza is a place where Pizza Chef prepare your favorite original Italian pizza, using the most delicious ingredients. 

This ordering system app will help the users selecting from a pizza menu or customize a pizza. 
The goal for the owner is to have access to the menu via Google Sheet as well as see all the orders placed there on a simple and intuitive GUI.

![Initial Page](/docs/artisan-pizza-homepage.png)

[Visit the live website link](https://artisanpizza-e12e243b6fd4.herokuapp.com/)

# UX

There are a lot of ways to approach an ordering system for a Pizza restaurant below you can find the considerations I put together.

## User stories

As pizza restaurant customer:
- Provide Name and Phone number 
- View the menu
- Choose the pizza without much typing
- Choose the pizza base/dough and size
- Add extra toppings if I'd like to customize my pizza
- Add the pizza to my order
- Being able to add multiple pizza in a single order
- View the whole order once I completed
- Get an order reference ID

As pizza restaurant ower: 
- Provide an easy way for customers to order pizza
- Being able to modify Menu in an easy way via a GUI like Google Sheet
- Being able to see all the placed orders

## App Workflow

I used [Diagrams.net](https://app.diagrams.net/) to create the application worlfow to have a guideline in terms of which functions I had to implement. Almost every block correspond to a defined function.

![Workflow](/docs/artisan-pizza-workflow-diagram.png)

# Data Structure - Google Sheet

I decided to integrate the application with Google sheet to have a place to load the menu and to save the orders.

## Menu Worksheet

Each column correspond to a Pizza, and last column is used for the Extra toppings.
A menu fuction has been implemented to load each column in a list using gspread related methods.

Here how the menu is structured:
- Row-1 - This heading is as index/pizza ID [or extra toppings]
- Row-2 - This represent the Pizza name
- Row-3 - This is the price set for each pizza
- Row-4 - From this row on each column we've all the included toppings, and for last column all the extra toppings

![GS-Menu](/docs/artisan-pizza-googlesheet-menu.png)

## Orders Worksheet

As the name says, this worksheet is used to store the data related to the orders, so the owner can see what to prepare, with an order ID, time and all the data related to pizza and related customization in terms of base, size and extra toppings with the total price for each pizza and related quantity. 
An order is identified by an ID and can have multiple rows corresponding to a specific pizza.

![GS-Orders](/docs/artisan-pizza-googlesheet-orders.png)

