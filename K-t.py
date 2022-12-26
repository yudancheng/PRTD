# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 10:48:29 2022

@author: E490
"""

import random
import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib.mlab as malb
#import math
#import xlsxwriter
#import xlwings as xw
from scipy.stats import truncnorm

def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

new_R=[]

#生成声望倍数数组
'''
def R_mul(R):
    i=0
    t=0.5
    while i<len(R):
        a=int(R[i]/t)
        new_R.append(a)
        i+=1   
    return new_R
'''
def R_mul(R):
     i=0
     t=0.4
     while i<len(R):
         a=(R[i]-t)/0.1
         if (a>0):
            new_R.append(a)
         else:
            new_R.append(0)
         i+=1   
     return new_R

#求出new_R=[]中所有元素的和
def r_sum(R,n):
    return(sum(R))

j=0
n=0
count=0
s=0
k=0
#sampleNo = 100;
#mu = 0.05
# = 0.01
while j<10000:
    #随机生成声望值
    X=get_truncated_normal(mean=0.75, sd=0.5, low=0, upp=1)
    R=X.rvs(60)
    np.set_printoptions(precision = 2)
    #print ('声望值R1=:\n',np.around(R,2)) #感知数据与真值的标准差数组
    #随机生成扰动数据
    #X1=get_truncated_normal(mean=0.5, sd=0.5, low=0, upp=1)
    #R1=X1.rvs(20)
    #R=np.random.normal(0.75,0.5,100)
    #np.random.seed(0)
    R1 = np.random.normal(0.05, 0.01, 60)
    np.set_printoptions(precision = 2)
    #print ('声望值R1=:\n',np.around(R1,2)) #感知数据与真值的标准差数组

#生成声望倍数数组
    new_R=[]
    new_R1=[]
    new_R=R_mul(R)
    print ('扰动前的声望倍数数组new_R=：\n',np.around(new_R,2))
    while k<len(new_R):
        b=new_R[k]
        if (b>0):
           new_R1.append(new_R[k]+R1[k])
        else:
           new_R1.append(0)
        k+=1
    np.set_printoptions(precision = 2)
    print ('扰动后的声望倍数数组new_R1=：\n',np.around(new_R1,2))
    n=len(new_R1)
    count=r_sum(new_R1, n)
    print(count)
    s+=count
    j+=1
    k=0
#print(s/j)
np.set_printoptions(precision = 2)
print ('扰动后的平均声望倍数数组=：\n',np.around(s/j,2))