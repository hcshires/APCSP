name1 = 'Henry'
name2 = 'Norah'

# Get the directory name for data files
import os.path
directory = os.path.dirname(os.path.abspath(__file__))

#initialize the aggregators
years1=[]
number_of_people1=[]
years2=[]
number_of_people2=[]

# Scan one year's file at a time
for year in range(1880,2012):
    # Open the file
    filename = os.path.join(directory, 'yob'+str(year)+'.txt')
    datafile = open(filename,'r')
    # Go through all the names that year
    for line in datafile:
        name, gender, number = line.split(',')
        name = name.strip() # Seperates text in file
        gender = gender.strip()
        number = int(number.strip())
        # Aggregate based on name1
        if name == name1 and gender == 'M':
            years1 += [year]
            number_of_people1 += [number]  # Iterates through each line of text
        #Aggregate based on name2
        if name == name2 and gender == 'F':
            years2 += [year]
            number_of_people2 += [number]
    #Close that year's file
    datafile.close()

# Plot on one set of axes.
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1,1)
ax.plot(years1,number_of_people1,'#0000FF')
ax.plot(years2,number_of_people2,'#FF00FF')

ax.set_title('U.S. Babies Named ' + name1 +' (blue) or ' + name2 +' (pink)')
plt.show()
