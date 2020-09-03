'''
differenceBetweenProportions.py creates two proportions, MonteCarlo style,
from a known proportion in the population and from two sample sizes.
The two proportions are illustrated by two pie charts.
A third graphic shows the 95% confidence intervals for the proportions. 
A p-value is shown, highlighted green is p<0.05.
Alternate code allows the same visualization to be produced from real data.

Version 6/2/14. 
(c) 2014 Project Lead The Way, Inc
'''

import cse
import importlib
import matplotlib.pyplot as plt
importlib.reload(cse) # make import fresh in case you changed the code

####
# Get the data
###

# The two categories of each pie chart.
p_and_q = ['Text', 'Do Not Text'] # [p-label, q-label]
# The two groups of people (or whatever) being compared
treatments = ['Sophomores','Juniors'] 

simulate = True # Change to False if providing your own data
if simulate:  
    # Simulation parameters
    number_group1 = 30
    number_group2 = 30
    p1_hat, p2_hat = [0.72, 0.72] # Simulate sample from these two proportions
    # Based on Lenhart, A. (2011). Teens, Smartphones, and Technology. Retrieved from
    # http://pewinternet.org/Reports/2012/Teens-and-smartphones.aspx
    
    # Generate the samples by randomized simulation, elements is unused here    
    number_p1, number_q1, elements = \
        cse.montecarlo.two_categories(number_group1, p1_hat)
    number_p2, number_q2, elements = \
        cse.montecarlo.two_categories(number_group2, p2_hat)
else:
    # Or put real data here and change the simulate boolean to False
    number_p1 = 0 # number in group 1 who said "p"
    number_q1 = 0 # number in group 1 who said "q"
    number_p2 = 0 # number in group 2 who said "p"
    number_q2 = 0 # number in group 2 who said "q"

#####
# Create the visualizations
#####
data = [number_p1, number_q1, number_p2, number_q2] # use values from above
fig, ax = cse.viz.two_proportions(data, treatments, p_and_q)
plt.show()