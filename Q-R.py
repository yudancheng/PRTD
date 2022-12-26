# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 16:49:11 2022

@author: E490
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time
import random
import numpy as np
import matplotlib.pyplot as plt
import math
import xlsxwriter
import xlwings as xw
from scipy.stats import truncnorm

def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)



#定义数据和真值之间的距离函数
#计算数组的数据与平均值之间的标准差

workbook = xlsxwriter.Workbook('data.xlsx') # 建立文件
worksheet = workbook.add_worksheet('ITD') 




#A= [10,30,60,70,70,80,90,60,50,70]; #参与者的数据
wb = xw.Book('Sdata.xlsx')
sht = wb.sheets[0]
A = sht.range('D329:D378').value
print(A)

'''
R=[0.63, 0.57, 0.39, 0.8,  0.78, 0.24, 0.74, 0.89, 0.8,  0.99,
   0.44, 0.89, 0.65, 0.51, 0.39, 0.98, 0.62, 0.71, 0.55, 0.49, 
   0.88, 0.52, 0.48, 0.51, 0.58, 0.91, 0.74, 0.74, 0.91, 0.83,
   0.91, 0.35, 0.86, 0.73, 0.67, 0.52, 0.39, 0.66, 0.45, 0.64, 
   0.64, 0.32, 0.55, 0.41, 0.85, 0.95, 0.56, 0.72, 0.4,  0.71,
   0.81, 0.75, 0.74, 0.92, 0.66, 0.34, 0.58, 0.28, 0.61, 0.62,
   0.81, 0.77, 0.98, 0.73, 0.93, 0.25, 0.57, 0.46, 0.28, 0.49, 
   0.03, 0.31, 0.48, 0.41, 0.21, 0.46, 0.74, 0.59, 0.46, 0.43, 
   0.54, 0.28, 0.54, 0.92, 0.71, 0.53, 1.,   0.23, 0.86, 0.8,  
   0.93, 0.63, 0.77, 0.77, 0.25, 0.5,  0.45, 0.29, 0.69, 0.47]
   0.41, 0.59, 0.58, 0.74, 0.38, 0.53, 0.61, 0.37, 0.3,  0.89, 
   0.34, 0.79, 0.87, 0.4,  0.4,  0.99, 0.83, 0.79, 0.67, 0.5,
   0.57, 0.77, 0.53, 0.34, 0.56, 0.22, 0.41, 0.78, 0.67, 0.88, 
   0.22, 0.62, 0.02, 0.97, 0.61, 0.72, 0.69, 0.64, 0.57, 0.22, 
   0.4,  0.71, 0.31, 0.38, 0.63, 0.17, 0.1,  0.3,  0.76, 0.62,
   0.58, 0.51, 0.5,  0.13, 0.25, 0.35, 0.21, 0.22, 0.16, 0.36, 
   0.39, 0.41, 0.35, 0.45, 0.01, 0.39, 0.47, 0.33, 0.1,  0.18, 
   0.59, 0.36, 0.22, 0.59, 0.19, 0.89, 0.87, 0.15, 0.6,  0.06,
   0.28, 0.11, 0.22, 0.06, 0.22, 0.18, 0.26, 0.14, 0.1,  0.18, 
   0.37, 0.25, 0.21, 0.75, 0.97, 0.72, 0.47, 0.27, 0.32, 0.12] 
'''
new_R=[1.45,0.7,0.4,2.2,1.65,0,1.45,1.85,1.85,2.6,
       0.85,2.1,1.6,0.85,0.15,2.95,1.15,1.4,1.1,0.6,1.8,      
       1.05,0.85,1,0.95,2.3,1.8,2.1,2.3,2.75,2.85,
       0.2,2.15,1.6,1.45,0.95,0.4,1.25,0.4,1.15,1.55,
       0.2,1.1,0.9,2.3,2.55,1.15,2.3,0.65,1.7]

  #参与者的声望值
 #生成声望倍数数组
'''
def R_mul(R):
     i=0
     t=0.2
     while i<len(R):
         a=int(R[i]/t)
         new_R.append(a)
         i+=1   
     return new_R
'''
'''
def R_mul(R):
     i=0
     t=0.2
     while i<len(R):
         if(R[i]>=t):
            a=int((R[i]-t)/0.1)
            new_R.append(a)
         else:
            new_R.append(0)
         i+=1   
     return new_R
'''
 #生成扩展数组
'''
def Ex_data(A):#X表示原始数组
     j=0
     new_A=[]
     while j<len(A):
         b=A[j]
         num=new_R[j]
         k=0
         while k<num:
             new_A.append(b)
             k+=1
         j+=1
     return new_A #扩展之后的数组 
'''
def Ex_data(A):#X表示原始数组
     j=0
     new_A=[]
     while j<len(A):
         b=A[j]
         num=round(new_R[j])
         k=0
         while k<num:
             new_A.append(b)
             k+=1
         j+=1
     return new_A #扩展之后的数组 
  

#X=get_truncated_normal(mean=0.75, sd=0.5, low=0, upp=1)
#R=X.rvs(100)

#np.set_printoptions(precision = 2)
#print ('感知数据与真值之间的标准差R=:\n',np.around(R,2)) #感知数据与真值的标准差数组

def dis(gt, a):#距离,,数据和真值之间的距离
    t = 0;
    i=0
    while i<len(new_A):
        t +=math.pow((new_A[i] - pj), 2);
        i+=1
    t =math.pow(t /len(new_A), 0.5);
    return pow((a - gt), 2) / t;

def weight(gt, a):
    t = 0;
    j=0
    while j<len(new_A):
        t +=dis(gt, new_A[j]);
        j+=1
    t /= dis(gt, a);
    t = math.log(t);
    return t;

def truth_update(new_A, W):
    t=0;
    w=0;
    k=0
    while k<len(new_A):
        t += W[k] * new_A[k];
        w += W[k]; 
        k+=1;
    return t / w;  
#生成声望倍数数组
#new_R=[]
#new_R=R_mul(R)
#print ('声望倍数数组new_R=：\n',new_R)
K=[];#存储迭代的次数
IPJ=[];#初始数组的平均值
FGT=[];#最终的真值
T=[];#程序运行的时间
Q=[];#数据的质量
R=[]


num1=0;#循环的次数
while num1<1:
    #new_R=[]
    #new_R=R_mul(R)
    new_A=[];#扩展的数据
    W=[];#用户的权重
    D=[];#感知数据与真值之间的距离
    PJ=[];#数据的平均值
    k=1
    i_0=0
    #A=np.random.normal(20,4,100)#原始数组
    new_A=Ex_data(A) #生成扩展数组
    #print ('扩展数组new_A=:\n',new_A)
    
    pj=np.mean(new_A)#求初始数组的平均值
    PJ.append(pj)
    IPJ.append(pj)
    print ('初始数组的平均值pj=:\n',round(pj,4))
    #print (round(pj,4))
    #worksheet.write(1,num1,round(pj,4))
    start=time.time()
    while k>0:
        #print ('第k次迭代k=:\n',k)
        while i_0<len(new_A):
            w=weight(pj, new_A[i_0])
            W.append(w);
            i_0+=1
        pj = truth_update(new_A, W);
        PJ.append(pj)

        if (abs(PJ[k]-PJ[k-1])<0.05):
            #print ('迭代次数k=',k)
            K.append(k)
            #worksheet.write(2,num1,k)
            k=0
            end=time.time();
            t=end-start;
            T.append(t);
        else:
            k+=1 
        #print ('感知任务的真值pj=:\n',round(pj,4))
        i_0=0
        D=[]
        W=[]
    print ('感知任务的最终真值pj=:\n',round(pj,4))
    k=0
    q=0
    q_1=0
    QK=[]
    while q<len(A):
        Q.append(1/(dis(pj,A[q])+0.01))
        q+=1
    Sq=sum(Q);
    while q_1<len(A):
        QK.append(Q[q_1]/Sq)
        q_1+=1
    np.set_printoptions(precision = 4)
    print ('用户的数据质量Q=:\n',np.around(QK,4))  
    j=0
    while j<len(QK):
        #if (new_R[j]!=0):
        R_0=1/(1+math.exp(-(new_R[j]*QK[j]-1)))
        R.append(R_0)
        #else:
            #R[j]=0.1
        j+=1
    np.set_printoptions(precision = 4)
    print ('更新后的用户的声望值R=:\n',np.around(R,4))
    
    #e=0
    #E=[];#存储平均的误差值
    #while e<len(A):
    #    er=abs((A[e]-pj)/pj)
    #    E.append(er)
     #   e+=1
    #np.set_printoptions(precision = 4)
    #print ('误差值E=:\n',np.around(E,4))
    #真值和感知数据之间的差距
    d=0;
    D=[];#存储平均距离
    while d<len(A):
        dr=dis(pj, A[d])
        D.append(dr)
        d+=1
    np.set_printoptions(precision = 4)
    print ('误差值E=:\n',np.around(D,4))       
    num1+=1;
    

    






    

