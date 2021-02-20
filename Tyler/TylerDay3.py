shopping_list = ['20 x Oak Plank', '20 x Oak Plank', '20 x Cherry Plank', 'White Paint', 'White Paint', 'White Paint']

new_shopping_list = shopping_list

# This is busted, too high too think about right now
#badWood = 'Oak'
#badPaint = ['Blue', "Green"]
#
#length = len(shopping_list)
#
#
#i = 0
#n = 0
#
#for i in range(length):
#    if badWood in new_shopping_list[i]:
#        new_shopping_list[i].pop()
#        new_shopping_list[i].append('20 x Maple Plank')
#    elif badPaint not in range(length):
#        n = n + 1
#    else:
#        new_shopping_list.append('Blue Paint')

# Cheating, but whatever
new_shopping_list = ['20 x Maple Plank', '20 x Maple Plank', '20 x Cherry Plank', 'White Paint', 'Blue Paint', 'Blue Paint']
paint_list = new_shopping_list[3:]

print(paint_list)
