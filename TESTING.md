# Artisan Pizza Testing

## Automated Tests

### Python Validation
Python code syntax has been validated using Code Insitute PEP8 Linter.  
No syntax errors found:  
![PEP8 Linter](/docs/artisan-pizza-pep8-linter.png)

## Manual Tests
Testing performed exclusively on a desktop

- Browsers tested:
    - Google Chrome
    - Firefox

Manual tests have been performed extenstively during the development using the both print or pprint functions to verify the correct variable contents.

### Welcome Feature 
| Feature                        | Expected Outcome                                               | Testing Performed                                                                | Result                                                                         | Pass/Fail |
|--------------------------------|----------------------------------------------------------------|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------|-----------|
| Name input                     | Customer Name is validated                                     | Check Name is not blank                                                          | User gets a "Name cannot be blank, please try again" error                     | Pass      |
| Name input                     | Customer Name is validated                                     | Name contain a single or multiple space characters only                          | User gets a "Name cannot be blank, please try again" error                     | Pass      |
| Name input                     | Customer Name is validated                                     | Check Name doesn't contain numbers                                               | User gets a "Please check the input, only [A-Z] characters are accepted" error | Pass      |
| Name input                     | Customer Name is validated                                     | Name contain a space character                                                   | User name is accepted                                                          | Pass      |
| Phone input                    | Phone number validated correctly                               | Check Phone is digit only and 10 digits long                                     | User gets a "Phone number should be 10 numeric digits" error                   | Pass      |


### Menu Feature
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|---|---|---|---|---|
| Menu | The Menu is loaded correctly | Verify the menu is loaded from Google Sheet using Google API | The menu is displayed on the user screen | Pass |
| Menu | Customer can select only pizza displayed using digits 1-6 | Check alpha characters are not accepted | User gets a "Cannot find your pizza in the menu, please try again" error message| Pass |
| Menu | Customer can select only pizza displayed using digits 1-6 | Check numbers out of range 1-6 are not accepted | User gets a "Cannot find your pizza in the menu, please try again" error message| Pass |

### Pizza Base Feature
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|---|---|---|---|---|
| Select Base  | Customer can select pizza base only using the displayed characters | Try to use numbers and characters different from the 3 allowed (N, G, W) | User gets a "Invalid input, please try again" error message                      | Pass      |
| Select Base  | Customer can use both capital or lowercase allowed characters      | Try the 3 allowed options (N, G, W) both in uppercase or lowercase       | Selected base is accepted                                                        | Pass      |
| Update pizza price | Price within the object pizza is updated                           | Print the updated pizza price                                          | Price is updated based on base selected                                          | Pass      |

### Pizza Size Feature
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|---|---|---|---|---|
| Select Size  | Customer can select pizza size only using the displayed characters | Try to use numbers and characters different from the 3 allowed (S, L, XL) | User gets a "Invalid input, please try again" error message                      | Pass      |
| Select Size  | Customer can use both capital or lowercase allowed characters      | Try the 3 allowed options (S, L, XL) both in uppercase or lowercase       | Selected size is accepted                                                        | Pass      |
| Update pizza price | Price within the object pizza is updated                           | Print the updated pizza price                                          | Price is updated based on size selected                                          | Pass      |

###  Pizza Extra Toppings Choice Feature
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|---|---|---|---|---|
| Extra Toppings Choice | Customer input is validated                                        | Try to use numbers and characters different from Y/N                   | User gets a "Invalid input, please try again" error message                      | Pass      |
| Extra Toppings Choice | Customer can use both capital or lowercase Y/N                     | Try the 2 allowed options (Y, N) both in uppercase or lowercase        | Input is valid and Extra toppings menu is displayed                              | Pass      |

###  Pizza Extra Toppings Menu Feature
| Feature                        | Expected Outcome                                               | Testing Performed                                                                | Result                                                                      | Pass/Fail |
|---|---|---|---|---|
| Select Extra Topping           | Customer can select only extra toppings displayed using digits | Check alpha characters are not accepted                                          | User gets a "Invalid input, please try again" error message                 | Pass      |
| Select Extra Topping           | Customer can select only extra toppings displayed using digits | Check numbers out of range are not accepted                                      | User gets a "Invalid input, please try again" error message                 | Pass      |
| Update pizza price             | Price within the object pizza is updated                       | Print the updated pizza price                                                    | Price is updated based on number of toppings added                          | Pass      |
| Customer Extra Topping choice  | Customer gets the add extra toppings choice question           | After selecting the extra topping validate the user can add other extra toppings | User is asked for extra toppings again                                      | Pass      |
| Update extra topping menu list | Extra toppings menu list is updated                            | After selecting the extra topping, it gets removed from available options        | New list of extra toppings is displayed without the latest topping selected | Pass      |

###  Select Pizza Quantity Feature
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|---|---|---|---|---|
| Select pizza quantity          | Customer can select only pizza displayed using digits 1-10     | Check alpha characters are not accepted                                          | User gets a "Invalid input, please try again" error message                 | Pass      |
| Select pizza quantity          | Customer can select only pizza displayed using digits 1-10     | Check numbers out of range 1-10 are not accepted                                 | User gets a "Invalid input, please try again" error message                 | Pass      |
| Update pizza price             | Price within the object pizza is updated                       | Print the updated pizza price                                                    | Price is updated based on extra toppings added                              | Pass      |
| Update order price             | Total Price within the object order is updated                 | Print the updated order total price                                              | Price is updated based on selected pizza quantity                           | Pass      |

###  Adding Another Pizza Feature
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|---|---|---|---|---|
| Choose to build another pizza  | The pizza menu is displayed                                    | Select Y/y to start building a new pizza                                         | Customer gets the pizza menu an can start building an additional pizza      | Pass      |
| Choose to build another pizza  | The complete order is displayed                                | Select N/n to get the order details                                              | Customer gets the order details                                             | Pass      |

###  Order confirmation Feature
| Feature                        | Expected Outcome                                                                       | Testing Performed                                                                                                  | Result                                                                      | Pass/Fail |
|--------------------------------|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|-----------|
| Display Order                  | All the order details gets displayed correctly                                         | Check customer Name, Number, Order ID, Date and all pizza are displayed correctly and Order total price is correct | Order details are displayed correctly                                       | Pass      |
| Confirm Order                  | Customer input is validated                                                            | Try to use numbers and characters different from Y/N                                                               | User gets a "Invalid input, please try again" error message                 | Pass      |
| Confirm Order                  | Customer can use both capital or lowercase Y/N                                         | Try the 2 allowed options (Y, N) both in uppercase or lowercase                                                    | Input is valid and order is transmitted to Google Sheet                     | Pass      |
| Confirm Order                  | Customer order is correctly displayed in Google sheet                                  | Check on google drive new lines with reference order ID are appended                                               | Worksheet "orders" is updated                                               | Pass      |
| Confirm Order                  | When customer decide not to confirm the order the application start from the beginning | Digit N/n when asked to confirm order                                                                              | The Welcome page appers                                                     | Pass      |
