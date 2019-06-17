"""
Code Challenge ( Scatter Plot )

Suppose the result was announced for a class. 
In this class both guys and girls appeared in the exam. 
The goal is to find out who performed better and how to get rid of shortcomings.
We are going to make a scatter plot for that.
Boys are in green while girls in red. 

girls_grades = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
boys_grades = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
grades_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

Are their any outliers

Hint: 
    Use the Scatter method to scatter the data on the plot

"""

from matplotlib import pyplot as plt

girls_grades = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
boys_grades = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
grades_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.scatter(grades_range,girls_grades, color='red',label="girls"); 
plt.scatter(grades_range,boys_grades, color='green',label="boys"); 
plt.legend()
plt.xlabel("grade_range")
plt.ylabel("grade_obtained")