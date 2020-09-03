'''
differenceBetweenMeans.py creates two samples, MonteCarlo style,
from a known mean and standard deviation in the population and from two sample sizes.
The two proportions are illustrated by histograms.
A third graphic shows the inferred heights and the p-value.
Alternate code allows the same visualization to be produced from real data

Version 6/2/14. 
(c) 2014 Project Lead The Way, Inc
'''

import cse
import importlib

importlib.reload(cse)
import numpy as np
import matplotlib.pyplot as plt
####
# Get the data
###

# The measurement being made 
measurement_variable = 'Height'
measurement_unit = 'In.'
# The two groups of people (or whatever) being compared
treatments = ['14 yo females','17 yo females'] 

simulate = True # Change to False if providing your own data
if simulate:  
    ###
    # Height  
    ###
    # Based on http://www.cdc.gov/nchs/data/series/sr_11/sr11_252.pdf
    mu1, sigma1 = [63.6, 2.9] # 14 yo girls
    mu2, sigma2 = [64.2, 3.3] # 17 yo girls
    n1 = 200 
    n2 = 200
    # Generate the samples by randomized simulation
    sample1 = mu1 + sigma1*np.random.randn(n1)
    sample2 = mu2 + sigma2*np.random.randn(n2) 
    
else:
    # Or put real data here and change the simulate boolean to False
    sample1 = [1, 2, 3, 10]
    sample2 = [4, 4, 4, 4.1]
    n1 = len(sample1)
    n2 = len(sample2)

fig, ax = cse.viz.two_means(sample1, sample2, 
                        measurement_variable, measurement_unit, treatments)
                        
plt.show()