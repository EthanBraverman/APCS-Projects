# Database of users and their respective passwords and names.
users = ["admin", "user1", "user2"]
names = ["Administrator", "User #1", "User #2"
passwords = ["123", "456", "789"]

# Introduction to the program and asks the user to log in.
access_granted = False

print("CURRENCY CONVERTER")
print("")
print("Please log in.")
print("--------------")

# Asks the user for their username and password and checks them against the database. Access is granted if the username and password match.
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

# Currency conversion rates relative to USD as of November, 2024
usd = 1  # US DOLLAR
gbp = 0.77  # POUND STERLING
eur = 0.91  # EURO
jpy = 151.59  # JAPANESE YEN
cad = 1.38  # CANADIAN DOLLAR

# Asks the user what currency they are starting with and provides options
print("What currency are you starting with?")
print("1. US Dollar")
print("2. British Pound Sterling")
print("3. Euro")
print("4. Japanese Yen")
print("5. Canadian Dollar")
print("")

# Function to determine the currency name, value, and symbol based on user input
def currency_type():
    # Loop re-runs the option selector if the option selected is not valid
    valid_option = False
    while valid_option == False:
        currency = input("Please select an option: ")

        if currency == "1" or currency == "US Dollar" or currency == "USD":
            currency_name = "US Dollar"  # Sets initial currency name (readable text)
            currency_value = usd  # Sets initial currency value to the ones defined above
            currency_symbol = "$"  # Sets the initial currency symbol to be used in output text
            valid_option = True  # Exits the loop
        elif currency == "2" or currency == "British Pound Sterling" or currency == "Pound Sterling" or currency == "Pound" or currency == "GBP":
            currency_name = "British Pound Sterling"
            currency_value = gbp
            currency_symbol = "£"
            valid_option = True
        elif currency == "3" or currency == "Euro" or currency == "EUR":
            currency_name = "Euro"
            currency_value = eur
            currency_symbol = "€"
            valid_option = True
        elif currency == "4" or currency == "Japanese Yen" or currency == "Yen" or currency == "JPY":
            currency_name = "Japanese Yen"
            currency_value = jpy
            currency_symbol = "¥"
            valid_option = True
        elif currency == "5" or currency == "Canadian Dollar" or currency == "CAD":
            currency_name = "Canadian Dollar"
            currency_value = cad
            currency_symbol = "CA$"
            valid_option = True
        else:
            # Re-runs the loop if the input is invalid (based on "if" option)
            print("")
            print("That is not a valid option.")
            valid_option = False

    return currency_name, currency_value, currency_symbol # Returns the currency name, value, and symbol for further use


initial_currency_name, initial_currency_value, initial_currency_symbol = currency_type() # Gets the initial currency values based on user input in the function above

print("")
# Asks how many of the initial currency the user has
amount = float(input("How many " + initial_currency_name + "s do you have?: "))

# Rounds any given float number to 2 decimals to be used in currency
def round_to_2_decimals(number_to_round):
    rounded_number = round(number_to_round, 2)
    return rounded_number

# Finds the input currency in USD (USD is used as a conversion factor), then uses a defined function to round it to 2 decimals
amount_in_usd_unrounded = amount / initial_currency_value
amount_in_usd = round_to_2_decimals(amount_in_usd_unrounded)

# Asks the user which currency they would like to convert to
print("")
print("Which currency would you like to convert to?")
print("1. US Dollar")
print("2. British Pound Sterling")
print("3. Euro")
print("4. Japanese Yen")
print("5. Canadian Dollar")
print("")

converting_currency_name, converting_currency_value, converting_currency_symbol = currency_type() # Gets the converting currency values based on user input in the function above

# Finds the new amount based on the previously converted to USD amount and the value of the "converted to" currency, then rounds using the defined function
new_amount_unrounded = amount_in_usd * converting_currency_value
new_amount = round_to_2_decimals(new_amount_unrounded)

# Prints final conversion
print("")
print(initial_currency_symbol + str(
    amount) + " (" + initial_currency_name + "s) in " + converting_currency_name + " is " + converting_currency_symbol + str(
    new_amount) + ".")
