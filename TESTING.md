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
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|---|---|---|---|---|
| Name input | Customer Name is validated | Check Name is not blank | User gets a "Name cannot be blank, please try again" error | Pass |
| Name input | Customer Name is validated | Check Name doesn't contain numbers | User gets a "Please check the input, only [A-Z] characters are accepted" error | Pass |
| Name input | Customer Name is validated | Name contain a space character | User name is accepted  | Pass |
| Phone input | Phone number validated correctly | Check Phone is digit only and 10 digits long | User gets a "Phone number should be 10 numeric digits" error | Pass |

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
| Expected Outcome                                                   | Testing Performed                                                                | Result                                                                           | Pass/Fail |
|--------------------------------------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|-----------|
| Customer can select only extra toppings displayed using digits     | Check alpha characters are not accepted                                          | User gets a "Invalid input, please try again" error message                      | Pass      |
| Customer can select only extra toppings displayed using digits     | Check numbers out of range are not accepted                                      | User gets a "Invalid input, please try again" error message                      | Pass      |
| Price within the object pizza is updated                           | Print the updated pizza price                                                    | Price is updated based on base selected                                          | Pass      |
| Customer gets the add extra toppings choice question               | After selecting the extra topping validate the user can add other extra toppings | User is asked for extra toppings again                                           | Pass      |
| Extra toppings menu list is updated                                | After selecting the extra topping, it gets removed from available options        | New list of extra toppings is displayed without the latest topping selected      | Pass      |

###  Select Pizza Quantity Feature
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|---|---|---|---|---|

###  Adding Another Pizza Feature
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|---|---|---|---|---|

###  Order confirmation Feature
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|---|---|---|---|---|
 