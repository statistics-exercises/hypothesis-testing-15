import numpy as np
import scipy.stats
  
def pvalue( data ) : 
  # Your code should go here.  You should calculate and return the p-value
  # given that the statistic takes the value data that is passed to the 
  # function
  
  

# You should not need to adjust anything from here onwards
sample = -2.3478
print("The null hypothesis is that the value of sample is a standard normal random variable")
print("The alternative hypothesis is that sample is set to a value that has been sampled from")
print("a distribution with an expectation that is less than 0.")
print("The p-value is", pvalue( sample ) )
