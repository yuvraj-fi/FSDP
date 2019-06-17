"""
Code Challenge ( Line Plot )

We have to find sea level rise in past 100 years
Read the file sealevel.csv which has data for 135 years

It has two parts in the data, year and the sea level rise in inches

Read the csv file using the csv reader and create two list
    1) Which stores the years from 1880 to 2014
    2) Which stores the sealevel increase in inches
    
Now plot the data using Line Plot
The plot should have the valid title,labels, ticks ( x and y ), legend

Is the  sea level increasing almost every year.

"""

import csv
from matplotlib import pyplot as plt
x=[]
y=[]
with open("sealevel.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
        x.append(int(row['Year']))
        y.append(float(row['inches']))
plt.plot(x, y, color='blue',)
plt.grid(True)
plt.xlabel("Years")
plt.ylabel("Inches")
plt.title("sea level")
