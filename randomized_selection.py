# -*-coding:UTF8 -*
#------------------------------------------------------------------
# Randomized Median Algorithm
#------------------------------------------------------------------
"""
@author: W. Ider
"""

import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import random
import sys
from statistics import median
import warnings
warnings.filterwarnings("ignore")
from quickselect import Quickselect,random_partition_hoare


def randomized_median_algorithm(arr , NC = 0 ):#--------------------------
    """This function is an implementation of the Randomized Median
    Algorithm which returns the median of a list with a probability
    of success increasing with an increased value of n (size of the list)
    """#------------------------------------------------------------------
    n = len(arr)
    random.shuffle(arr)
    nb_samples = int(math.ceil(n ** (3.0 / 4.0)))
    R = random.sample(arr, nb_samples)
    NC+=Quicksort(R,0,len(R)-1,NC)
    di = int(math.floor(((n ** (3.0 / 4.0)) / 2.0) - math.sqrt(n)))
    d = R[di]
    ui = int(math.ceil(((n ** (3.0 / 4.0)) / 2.0) + math.sqrt(n)))
    u = R[ui]
    
    #----------------------------------------
    C = [x for x in arr if d <= x and x <= u]
    ld = len([x for x in arr if x < d])
    lu = len([x for x in arr if x > u])
    
    
    
    assert not (ld>(n/2) or lu > (n/2))
    assert len(C)<= 4.0 * (n**(3.0/4.0))

     
    #----------------------------------------
    
    
    NC+=Quicksort(C,0,len(C)-1,NC)
    NC+= 4+len(arr) + 3
    
    
    median = int(math.floor(n / 2) - ld + 1)
    return C[median],NC


def Quicksort(array, low, high,NC=0):#----------------
    """"Implementation of the Quicksort algorithm
    """
    #-------------------------------------------------
    if low < high:
        pivot = random_partition_hoare(array, low, high)[0]
        NC+=random_partition_hoare(array, low, high)[1] + 1 
        Quicksort(array, low, pivot - 1)
        Quicksort(array, pivot + 1, high)
    return NC



if __name__ == "__main__":
    for i in range(3):
        NC=0
        n=25000
        arr=[random.randint(1,n) for j in range(n)]
        print("_______________________________________________________________________________________________________________")
        print("The array's size is : " , len(arr))
        print("Its median is : ",randomized_median_algorithm(arr,NC)[0])
        print("The median given by statistics.median is : " , median(arr))
        print("___")
        print("The number of comparisons : " , randomized_median_algorithm(arr,NC)[1])
        print("_______________________________________________________________________________________________________________")
