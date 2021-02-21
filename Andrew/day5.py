for i in range(len(city_price)):
    if (country_price[i] / city_price[i]) > 1.10:
        print (cleaningsupplies_list[i], " is over 10%")
