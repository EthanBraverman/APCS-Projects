# Database of users and their respective passwords and names.
users = ["admin", "user1", "user2"]
names = ["Administrator", "User #1", "User #2"]
passwords = ["123", "456", "789"]

# Introduction to the program and asks the user to log in.
access_granted = False

print("CURRENCY CONVERTER")
print("")
print("Please log in.")
print("--------------")

#Asks the user for their username and password and checks them against the database. Access is granted if the username and password match.
while access_granted == False:
    username = input("Username: ")
    password = input("Password: ")
    print("")
    if username in users:
        if password == passwords[users.index(username)]:
            name = names[users.index(username)]
            print("Login successful. Welcome, " + name + "!")
            access_granted = True
        else:
            print("Incorrect password. Please try again.")
            print("-------------------------------------")
    else:
        print("User not found. Please try again.")
        print("---------------------------------")

print("")

#Currency conversion rates relative to USD
usd = 1 #US DOLLAR
gbp = 0.77 #POUND STERLING
eur = 0.91 #EURO
jpy = 151.59 #JAPANESE YEN
cad = 1.38 #CANADIAN DOLLAR

print("What currency are you starting with?")
print("1. US Dollar")
print("2. British Pound Sterling")
print("3. Euro")
print("4. Japanese Yen")
print("5. Canadian Dollar")
print("")

#Loop re-runs the option selector if the option selected is not valid
valid_option = False

while valid_option == False:
    initial_currency = input("Please select an option: ")
    
    if initial_currency == "1" or initial_currency == "US Dollar" or initial_currency == "USD":
        initial_currency_type = "US Dollar" #Sets initial currency type (readable text)
        initial_currency_value = usd #Sets initial currency value to the ones defined above
        initial_currency_symbol = "$" #Sets the initial currency symbol to be used in output text
        valid_option = True #Exits the loop
    elif initial_currency == "2" or initial_currency == "British Pound Sterling" or initial_currency == "Pound Sterling" or initial_currency == "Pound" or initial_currency == "GBP":
        initial_currency_type = "British Pound Sterling"
        initial_currency_value = gbp
        initial_currency_symbol = "£"
        valid_option = True
    elif initial_currency == "3" or initial_currency == "Euro" or initial_currency == "EUR":
        initial_currency_type = "Euro"
        initial_currency_value = eur
        initial_currency_symbol = "€"
        valid_option = True
    elif initial_currency == "4" or initial_currency == "Japanese Yen" or initial_currency == "Yen" or initial_currency == "JPY":
        initial_currency_type = "Japanese Yen"
        initial_currency_value = jpy
        initial_currency_symbol = "¥"
        valid_option = True
    elif initial_currency == "5" or initial_currency == "Canadian Dollar" or initial_currency == "CAD":
        initial_currency_type = "Canadian Dollar"
        initial_currency_value = cad
        initial_currency_symbol = "CA$"
        valid_option = True
    else:
        #Re-runs the loop if the input is invalid (based on "if" option)
        print("")
        print("That is not a valid option.")
        valid_option = False

print("")
#Asks how many of the initial currency the user has
initial_amount = float(input("How many " + initial_currency_type + "s do you have?: "))

#Rounds any given float number to 2 decimals to be used in currency
def round_to_2_decimals(number_to_round):
    rounded_number = round(number_to_round, 2)
    return rounded_number

#Finds the input currency in USD (USD is used as a conversion factor), then uses a defined function to round it to 2 decimals
amount_in_usd_unrounded = initial_amount / initial_currency_value
amount_in_usd = round_to_2_decimals(amount_in_usd_unrounded)

print("")
print("Which currency would you like to convert to?")

print("1. US Dollar")
print("2. British Pound Sterling")
print("3. Euro")
print("4. Japanese Yen")
print("5. Canadian Dollar")
print("")

#Loop for choosing a second (converting) currency so that it can run again if an invalid input is entered
valid_option = False

while valid_option == False:
    #Selection of the second (converting) currency
    converting_currency = input("Please select an option: ")
    
    #Based on the selected second (converting) currency, the converting currency type, value (determined by previously defined variables that are called,) and symbol are defined to be used later.
    if converting_currency == "1" or converting_currency == "US Dollar" or converting_currency == "USD":
        converting_currency_type = "US Dollars" #Sets the converting currency type (readable text)
        converting_currency_value = usd #Sets the converting currency value  to the ones defined above
        converting_currency_symbol = "$" #Sets the converting currency symbol to be used in output text
        valid_option = True #Exits the loop
    elif converting_currency == "2" or converting_currency == "British Pound Sterling" or converting_currency == "Pound Sterling" or converting_currency == "Pound" or converting_currency == "GBP":
        converting_currency_type = "British Pound Sterlings"
        converting_currency_value = gbp
        converting_currency_symbol = "£"
        valid_option = True
    elif converting_currency == "3" or converting_currency == "Euro" or converting_currency == "EUR":
        converting_currency_type = "Euros"
        converting_currency_value = eur
        converting_currency_symbol = "€"
        valid_option = True
    elif converting_currency == "4" or converting_currency == "Japanese Yen" or converting_currency == "Yen" or converting_currency == "JPY":
        converting_currency_type = "Japanese Yen"
        converting_currency_value = jpy
        converting_currency_symbol = "¥"
        valid_option = True
    elif converting_currency == "5" or converting_currency == "Canadian Dollar" or converting_currency == "CAD":
        converting_currency_type = "Canadian Dollars"
        converting_currency_value = cad
        converting_currency_symbol = "CA$"
        valid_option = True
    else:
        #Re-runs the loop if the input is invalid
        print("")
        print("That is not a valid option.")
        valid_option = False

#Finds the new amount based on the previously converted to USD amount and the value of the "converted to" currency, then rounds using the defined function
new_amount_unrounded = amount_in_usd * converting_currency_value
new_amount = round_to_2_decimals(new_amount_unrounded)

#Prints final conversion
print("")
print(initial_currency_symbol + str(initial_amount) + " (" + initial_currency_type + "s) in " + converting_currency_type + " is " + converting_currency_symbol + str(new_amount) + ".")
