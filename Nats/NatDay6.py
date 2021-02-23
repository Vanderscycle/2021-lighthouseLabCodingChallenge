import random 
random.seed(34)

hole_sizes = [random.randint(1, i) for i in range(1, 101)]
random.shuffle(hole_sizes)

# hole sizes in mm


print(hole_sizes)


import pandas as pd # we must import our external python plugin

series = pd.Series(hole_sizes) #converting our hole_sizes to a pandas series variable
                                #we need to do this to use some of pandas' useful descriptive statistics functions

series.max()    #outputs maximum value in Pandas Series
series.min()    #outputs minimum value in Pandas Series
series.mean()   #outputs average value in Pandas Series
series.median() #outputs median value in Pandas Series
series.mode()   #outputs mode value in Pandas Series

print(series.mean())#question 1 what is average size of the holes

small = 20
small_hole = 1.3
medium_hole= 1.6
large = 70
large_hole=2.1


#What is the average cost to fix a hole?

#Small (less than 20 mm)	$1.30
#Medium (above or equal to 20 mm AND less than 70mm)	$1.60
#Large (above or equal to 70 mm)	$2.10

hole=list()
for i in range(len(hole_sizes)):
    if series[i] < small:
        hole.append(small_hole)
    elif small <= series[i] < large:
        hole.append(medium_hole)
    else:
        hole.append(large_hole)

series2 = pd.Series(hole)

print(series2.mean())
       
print(sum(hole))

