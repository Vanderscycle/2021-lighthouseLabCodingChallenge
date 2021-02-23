import pandas as pd # we must import our external python plugin

list_of_num = [1,2,3,4,5]

series = pd.Series(list_of_num) #converting our list_of_num to a pandas series variable
                                #we need to do this to use some of pandas' useful descriptive statistics functions

series.max()    #outputs maximum value in Pandas Series
series.min()    #outputs minimum value in Pandas Series
series.mean()   #outputs average value in Pandas Series
series.median() #outputs median value in Pandas Series
series.mode()   #outputs mode value in Pandas Series

import random 
random.seed(34)

hole_sizes = [random.randint(1, i) for i in range(1, 101)]
random.shuffle(hole_sizes)

# hole sizes in mm
print(hole_sizes[:5])

# Answer to Q1, the avg size of holes.
seriesHoleSize = pd.Series(hole_sizes)
print(seriesHoleSize.mean())

# Answer to Q2, the average cost to fix a hole.
cost_per_hole = list()

for i in range(len(hole_sizes)):
    size = hole_sizes[i]
    if size < 20:
        cost_per_hole.append(1.30)
    elif 20 <= size < 70:
        cost_per_hole.append(1.60)
    else:
        cost_per_hole.append(2.10)

seriesCostHole = pd.Series(cost_per_hole)
print(round(seriesCostHole.mean(), 3))

# Answer to Q3, the total cost to fix all holes.
print(round(sum(cost_per_hole), 2))

# Answer to Bonus Q1, the biggest hole.
# series = pd.Series(hole_sizes)
print(seriesHoleSize.max())

# Answer to Bonus Q1, the smallest hole.
# series = pd.Series(hole_sizes)
print(seriesHoleSize.min())