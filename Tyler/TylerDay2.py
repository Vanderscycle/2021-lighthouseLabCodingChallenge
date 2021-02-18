# pip install rich
# https://github.com/willmcgugan/rich
from rich.console import Console
from rich.table import Table

# creating a simple table
table = Table(show_header=True, header_style="bold magenta")
table.add_column("Item", style="dim", width=12)
table.add_column("City Price")
table.add_column("Country Price", justify="right")
console = Console()

# Grocery List (19 items)
grocery_list = ['Bananas', 'Clementines', 'Baguette', 'Oat Milk', 'Olive Oil', 'Coffee Beans',
                'Chocolate Bar', 'Brocolli', 'Eggplant', 'Chickpeas', 'Lentils', 'Tomatoes',
                'Pasta', 'Rice', 'Yogurt', 'Blueberries', 'Onions', 'Garlic', 'Truffles']

# City Price
city_price = [6.49, 4.99, 4.39, 4.29, 11.99, 17.99,          
              3.49, 3.99, 1.10, 1.99, 2.99, 4.68,            
              1.59, 8.99, 3.49, 6.99, 2.99, 1.98, 14.99]

# Country Price
country_price = [4.49, 4.12, 3.42, 6.99, 7.99, 14.99,              
                2.99, 2.49, 0.99, 1.49, 2.49, 1.99,              
                1.59, 6.99, 3.89, 4.99, 1.69, 1.87, 11.49]

# Percent Difference = (y - x)/x
city_sum = sum(city_price)
country_sum = sum(country_price)
percent_difference = (city_sum - country_sum) / country_sum
display_percent = abs(round(percent_difference * 100, 2))
print(display_percent)

print()

# Prints the data and adds headers, but doesn't align columns as it uses raw tabs and doesn't know the length of data in the list
for i in range(len(grocery_list)):
    if i == 0: print("Grocery List\tCity Price\tCountry Price")
    print(grocery_list[i], "\t\t", city_price[i], "\t\t", country_price[i])
    # using the for loop to add rows
    table.add_row(str(grocery_list[i]), str(city_price[i]), str(country_price[i]))


print()

# Another option that looks nicer, but still doesn't react to data size
for i in range(len(grocery_list)):
    if i == 0: print("Grocery List\t\tCity Price\tCountry Price")
    print("%-23s %-15s %s" %(grocery_list[i], city_price[i], country_price[i]))

print("Pecent Difference = %", display_percent)

if city_sum > country_sum:
    difference_statement = f'The city is %{display_percent} more expensive.'
elif city_sum == country_sum:
    difference_statement = f'Food in the country costs the same as the city.'
else:
    difference_statement = f'The city is %{display_percent} less expensive.'
print(difference_statement)

console.print(table)