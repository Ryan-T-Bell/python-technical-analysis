"""
Moving Average Period
@author: Ryan Bell
"""

# Get path of parent directory to import Data Module
import sys
sys.path.insert(0, '..')

import Data

###################################################################################################
# Main Method for Moving Average TA
###################################################################################################


# closeList: List of all close values in sequential order
# period: Period to take moving average for e.g. 21 = 21 day MA
def movingAverage(closeList, period):
    
    # Variables
    i = 0
    
    movAvg = []                             # List of moving averages to return
    size = len(closeList)                   # Number of entries to calculate for
    sum = initialSum(closeList, period)     # 
    
    # Store Sum/Period for initial values
    while i < period:
        movAvg.append(sum/period)
        i += 1
    
    # Calculate remainder of ma values
    while i < size:
        sum += closeList[i]
        sum -= closeList[i-period]
        movAvg.append(sum/period)
        i += 1
    
    return movAvg

    
###################################################################################################
# Helper Methods to Calculate Moving Averages
###################################################################################################


# Calculate initial  sum for moving average calculation
def initialSum(closeList, period):
    
    i = 0    
    sum = 0
    
    while i < period:
        sum += closeList[i]
        i += 1
    
    return sum



###################################################################################################
# Testing Code
###################################################################################################
    

closeList = Data.getCloseList(Data.getData('IVV'))
print(movingAverage(closeList, 21)) 