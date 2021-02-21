item_list = ['Oak Wood', 'Blue Paint', 'White Paint', 'Paint Finish']

amount_list = [600,150,15,165]

wholesale_price_list = [7000, 1000, 1000, 800]

retail_price = [12.99, 8.99, 9.99, 3.99]
#use a lst = [1,2,3,4,5]
#for i in range(len(lst)): 
#    '''insert code''' Use a loop to determine the price Dot would pay for purchasing supplies at the retail price.
#  Based on that calculation, which itmes should Dot buy at retail vs. wholesale?
#In your for loop, you may want to use the .append() function to append the total 
# price of buying each needed item of supply at retail price to a new list.
#for (i = 1; i <= 10; i++)
#    <loop body>
#a = ['foo', 'bar', 'baz']
#for x in a:
 #   print(x)
total_retail_price = []
compare_list = [False, False, False, False]

for i in range(len(item_list)):
    total_retail_price.append(retail_price[i] * amount_list[i])
    total = total_retail_price[i]
    wholesale = wholesale_price_list[i]
    if total > wholesale:
        compare_list[i] = True
    else:
        compare_list[i] = False

print(total_retail_price)
print(compare_list)

