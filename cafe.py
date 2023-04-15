# This program is calculating the worth of the stock in a cafe
menu = ["Mocha" , "Cappucino" , "Latte" , "Tea"] # Listing the items in my menu

stock = {"Mocha": 300 , "Cappucino": 400 , "Latte": 200 , "Tea": 600} # Defining my stock and price dictionaries
price = {"Mocha": 3 , "Cappucino": 4 , "Latte": 4 , "Tea": 2}

total_worth = 0 # Calculting the total worth of the stock
for item in menu :
    if item in stock and item in price :
        total_worth += stock[item] * price[item]
print(f"The total worth of my stock is : £ {int(total_worth)}")
