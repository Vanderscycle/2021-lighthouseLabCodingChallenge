#new_shopping_list will replace oak with maple
shopping_list = ['20 x Oak plank', '20 x Oak Plank', '20 x Cherry Plank', 'White Paint', 'White Paint', 'White Paint']
x='20 x Maple Plank'
y= 'Blue Paint'
shopping_list.pop(0)
shopping_list.pop(0) 
shopping_list.insert(0,x)
shopping_list.insert(0,x)
shopping_list.pop(3)
shopping_list.pop(3)
shopping_list.insert(3,y)
shopping_list.insert(3,y)
new_shopping_list=shopping_list
print(new_shopping_list)
