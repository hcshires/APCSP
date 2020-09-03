'''
plot_age_income.py 
reads data from the age_income_feb14.csv
and creates a scatter plot.
The data are from U.S. Census Bureau's February 2014 
Current Population Survey. 

(c) 2014 Project Lead The Way
'''
import matplotlib.pyplot as plt

# Get the income/age data from CSV
datafile = open('age_income_feb14.csv','r')
data = datafile.readlines()

####
# Transform the data from strings to signed integers
####
ages=[]
incomes=[]
for line in data[3:]: # Omit header lines
    age, income = line.split(',')
    ages.append(int(age))
    
    if '-' in income:
        incomes.append(-1*int(income[3:-1])) # omit space, -, $, \n
    else:
        incomes.append(int(income[2:-1])) # omit space, $, \n         
        
fig, ax  = plt.subplots(1, 1)
ax.plot(ages, incomes, 'ro')
ax.set_title('Household Income vs. Householder Age\n(2/2014 U.S. Sample)')
ax.set_xlabel('Age (yrs)')
ax.set_ylabel('Household income ($/yr)')

plt.show()