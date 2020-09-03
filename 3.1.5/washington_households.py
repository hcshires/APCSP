'''
washington_households.py
reads data from the household_size_feb14.csv
and creates a histogram for the number of people per household
The data are from U.S. Census Bureau's February 2014
Current Population Survey.
'''

import matplotlib.pyplot as plt
import os.path

###
# Get the income/age data from CSV
###
# Get the directory name for data files
directory = os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'household_size_feb14.csv')
datafile = open(filename,'r')
data = datafile.readlines() # Reads all lines, each line is an entry in a list

people = [] # List for amount of people per house

# Line is a walker - stores an item from the list
for line in data:
    if line[:2] == 'WA': # Find specific state WA
        # Transforming the age data from str to int
        person = line[4]
        people.append(int(person))

# Find average number of people per house
average = sum(people) / len(people)
print("Average:", average)

# Median
people.sort() # Built-in python sorting, uses list with int
i = int(len(people) / 2)

median = people[i]
print("Median:", median)

# Histogram
fig_age, ax  = plt.subplots(1, 1)
a = ax.hist(people, color='#4286f4', bins=range(1, 10))
ax.set_title('People per Household in the state of Washington Feb 2014 U.S. Sample')
ax.set_xlabel('Frequency (# people)')
ax.set_ylabel('House')
plt.show()
