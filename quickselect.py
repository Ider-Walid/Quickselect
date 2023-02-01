# -*-coding:UTF8 -*
#------------------------------------------------------------------
# Quicksort using Hoare's Partitioning function
#------------------------------------------------------------------
"""
@author: W. Ider
"""

from math import ceil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from math import *
import warnings
warnings.filterwarnings("ignore")
from typing import Any, Optional, List



def random_partition_hoare(arr, p, q , NC = 0): # -----------------------------------
    """ This function partitions a segment of a list using Hoare's pivot
        algorithm and returns the new index of p after partitioning, where all
        elements before are <= pivot and all elements after are >= pivot.
    """ # ---------------------------------------------------------------------------
    a=random.randint(p,q)
    arr[p] , arr[a] = arr[a] , arr[p]
    r = arr[p] 

    arr.append(r)

    i, j = p , (q+1)
    while True:
        i += 1
        while (arr[i] < r):
            NC += 1
            i += 1  
        j -= 1

        while (arr[j] > r): 
            NC += 1
            j -= 1  

        arr[i], arr[j] = arr[j], arr[i]


        if (i >= j):
            NC+=1

            arr[i], arr[j] = arr[j], arr[i] 

            break
    arr.pop()  
    arr[p], arr[j] = arr[j], arr[p]
    return j , NC 

def Quickselect( arr , k , NC = 0): # -------------
    """This function is an implementation of the quickselect algorithm,
        using Hoare's partitioning, to select the k-th smallest element in a list
        """# -----------------------------------------------------------------
    bool_pivot= False 
    p= 0
    q= len(arr) - 1
    pivot=-1
    while not bool_pivot : 
        NC_Aux=0
        pivot , NC_Aux = random_partition_hoare(arr, p, q , NC_Aux) 
        NC += NC_Aux
        if (pivot < (k-1)):

            p = (pivot+1)
            NC+=1

        elif (pivot > (k-1)):

            q = (pivot-1)
            NC+=1

        else:

            bool_pivot = True

    return arr[pivot] , NC



if __name__ == "__main__":
    XX=[]
    YY=[]
    ZZ=[]
    for j in [100 * k for k in range(1,240)] : 
        N=25000
        alpha = j / N 
        XX.append(alpha)
        arr2=[random.randint(1,10000) for i in range(N)]
        listOfValues = [] 
        for i in range(100) :
            listOfValues.append(Quickselect(arr2 , j  )[1] / N )
        df=pd.DataFrame(listOfValues)
        YY.append(df.describe().loc['mean'].values[0])
        ZZ.append(2-2*(alpha*log(alpha) +  (1-alpha)*log(1-alpha) ))
        plt.figure(figsize=(10,10))
    plt.xscale("log")
    plt.xlabel("Value of Alpha")
    plt.plot(XX,YY,label='Approxmation Value')
    plt.plot(XX,ZZ, label = 'Real Value',linestyle=  '--')
    plt.legend()

