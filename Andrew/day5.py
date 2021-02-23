# Cleaning Supplies List (19 items)
cleaningsupplies_list = ['Broom', 'Mop', 'Dustpan', 'Garbage Bags', 'Glass Cleaner', 'Vinegar',
                        'Soap', 'Bleach', 'Duster', 'Floor Cleaner', 'Sponges', 'Dish Soap',
                        'Drain Cleaner', 'Paper Towels', 'Cleaning Rags', 'Toilet Cleaner', 
                        'Rubber Gloves', 'Alcohol Wipes', 'Squeegee']

# City Price
city_price = [6.49, 4.99, 3.39, 4.29, 3.99, 1.99, 
              1.50, 3.99, 4.99, 5.99, 2.99, 2.99, 
              5.99, 2.99, 3.49, 6.99, 2.99, 1.98, 11.99]

# Country Price
country_price = [5.49, 4.69, 4.42, 5.99, 5.99, 2.50,
                1.25, 2.49, 4.50, 6.75, 2.49, 1.99, 
                6.25, 3.99, 3.59, 4.99, 1.69, 1.87, 10.99]
for i in range(len(city_price)):
    if (country_price[i] / city_price[i]) > 1.10:
        print (cleaningsupplies_list[i], " is over 10%")

#you can also do it in a single line using list comprehensions
results = [cleaningsupplies_list[i] for i in range(len(city_price)) if (country_price[i] / city_price[i]) > 1.10]
print(results)