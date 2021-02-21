item_list = ['Oak Wood', 'Blue Paint', 'White Paint', 'Paint Finish']

amount_list = [600,150,15,165]

wholesale_price_list = [7000, 1000, 1000, 800]

retail_price = [12.99, 8.99, 9.99, 3.99]

total_retail_price = [0, 0, 0, 0]
purchase_wholesale = [False, False, False, False]

# This actually worked out great with minimal issues.
for i in range(len(item_list)):
    total_retail_price[i] = retail_price[i] * amount_list[i]
    total = total_retail_price[i]
    wholesale = wholesale_price_list[i]
    if total > wholesale:
        purchase_wholesale[i] = True
    else:
        purchase_wholesale[i] = False

print(total_retail_price)
print(purchase_wholesale)