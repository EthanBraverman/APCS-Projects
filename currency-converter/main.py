# Database of users and their respective passwords and names.
users = ["user1", "user2"]
names = ["name1", "name2"]
passwords = ["pass1", "pass2"]

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
eur = 0.92 #EURO
jpy = 150.06 #JAPANESE YEN
cad = 1.38 #CANADIAN DOLLAR

print("What currency are you starting with?")
print("1. US Dollar")
print("2. British Pound Sterling")
print("3. Euro")
print("4. Japanese Yen")
print("5. Canadian Dollar")
print("")

valid_option = False

while valid_option == False:
    initial_currency = input("Please select an option: ")
    
    if initial_currency == "1" or initial_currency == "US Dollar" or initial_currency == "USD":
        initial_currency_type = "US Dollar"
        initial_currency_value = usd
        initial_currency_symbol = "$"
        valid_option = True
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
        initial_currency_type = "Canadian Dolar"
        initial_currency_value = cad
        initial_currency_symbol = "CA$"
        valid_option = True
    else:
        print("")
        print("That is not a valid option.")
        valid_option = False

print("")
initial_amount = float(input("How many " + initial_currency_type + "s do you have?: "))

amount_in_usd = round(initial_amount / initial_currency_value, 2)

print("")
print("Which currency would you like to convert to?")

print("1. US Dollar")
print("2. British Pound Sterling")
print("3. Euro")
print("4. Japanese Yen")
print("5. Canadian Dollar")
print("")

valid_option = False

while valid_option == False:
    converting_currency = input("Please select an option: ")
    
    if converting_currency == "1" or converting_currency == "US Dollar" or converting_currency == "USD":
        converting_currency_type = "US Dollars"
        converting_currency_value = usd
        converting_currency_symbol = "$"
        valid_option = True
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
        print("")
        print("That is not a valid option.")
        valid_option = False
    
new_amount = round(amount_in_usd * converting_currency_value, 2)

print("")
print(initial_currency_symbol + str(initial_amount) + " (" + initial_currency_type + "s) in " + converting_currency_type + " is " + converting_currency_symbol + str(new_amount) + ".")
