# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 09:07:54 2022

@author: E490
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 09:58:36 2022

@author: E490
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import numpy as np
import matplotlib.pyplot as plt
import math
import xlsxwriter
import xlwings as xw
import time

#wb = xw.Book('Sdata.xlsx')
#sht = wb.sheets[0]
#A = sht.range('G3:G31').value
#print(A)
#R=np.random.rand(2)
#print(R)

#R=[0.67, 0.77, 0.97, 0.87, 0.77, 0.7,  0.22, 0.24, 0.36, 0.36, 0.26, 0.97,
 #  0.09, 0.08,0.06, 0.54, 0.4,  0.57, 0.76, 0.83, 0.66, 0.79, 0.56, 0.17,
#   0.24, 0.95, 0.52, 0.63,0.24];

#workbook = xlsxwriter.Workbook('data.xlsx') # 建立文件
#worksheet = workbook.add_worksheet('ITD') 
#A= [10,30,60,70,70,80,90,60,50,70];
#print(A)
wb = xw.Book('Sdata.xlsx')
sht = wb.sheets[0]
A = sht.range('D1163:D1206').value
print(A)

R=[0.63, 0.57, 0.39, 0.8,  0.78, 0.24, 0.74, 0.89, 0.8,  0.99,
   0.44, 0.89, 0.65, 0.51, 0.39, 0.98, 0.62, 0.71, 0.55, 0.49, 
   0.88, 0.52, 0.48, 0.51, 0.58, 0.91, 0.74, 0.74, 0.91, 0.83,
   0.91, 0.35, 0.86, 0.73, 0.67, 0.52, 0.39, 0.66, 0.45, 0.64, 
   0.64, 0.32, 0.55]
'''
   0.41, 0.85, 0.95, 0.56, 0.72, 0.4,  0.71,
   0.81, 0.75, 0.74, 0.92, 0.66, 0.34, 0.58, 0.28, 0.61, 0.62,
   0.81, 0.77, 0.98, 0.73, 0.93, 0.25, 0.57, 0.46, 0.28, 0.49, 
   0.03, 0.31, 0.48, 0.41, 0.21, 0.46, 0.74, 0.59, 0.46, 0.43, 
   0.54, 0.28, 0.54, 0.92, 0.71, 0.53, 1.,   0.23, 0.86, 0.8,  
   0.93, 0.63, 0.77, 0.77, 0.25, 0.5,  0.45, 0.29, 0.69, 0.47,
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


MAE=[];#存储Mae的值
RMSE=[];#存储RMSE的值
K=[];#存储迭代的次数
IPJ=[];#初始数组的平均值
FGT=[];#最终的真值
T=[];#程序运行的时间
mK=0;#迭代次数的平均值
mIPJ=0;#初始数组的均值的均值
mFGT=0;#最终真值的均值
mMAE=0;
mRMSE=0;
mT=0;#程序运行的平均时间

num=0;#循环的次数
while num<1:
    #A=np.random.normal(20,4,80)
    #R=np.random.rand(80)
    #print (R)


    i=0
    S=0;#数组的和
    k=1;#迭代的次数
    i_0=0
    d=0
    j_0=0
    D=[];#感知数据与真值之间的距离
    k_0=0
    sd=0
    w_0=0
    W=[];#用户的权重
    i_1=0
    dw=0
    sw=0
    PJ=[];#初始数组的平均值
    

 #计算数组A中的数据的平均值
    pj=np.mean(A)
    PJ.append(pj)
    IPJ.append(pj)
    print ('初始数组的平均值pj=:\n',round(pj,3))
    #worksheet.write(1,num,round(pj,3))
    
    start=time.time()
    while k>0:
    #print ('第k次迭代k=:\n',k)
    #通过声望值计算用户的权重
        while i_0<len(R):
            d+=R[i_0]
            i_0+=1
        #print(d) 
        while j_0<len(R):
            sd=R[j_0]/d
            W.append(sd)
            j_0+=1
        #print(W)
        #np.set_printoptions(precision = 4)
        #print ('用户的权重W=:\n',np.around(W,4))
#计算真值
        while i_1<len(W):
            dw+=A[i_1]*W[i_1]
            sw+=W[i_1]
            i_1+=1
        pj=dw/sw
        PJ.append(pj)
    #print ('感知任务的真值pj=:\n',round(pj,4))
        if (abs(PJ[k]-PJ[k-1])<0.05):
            #print ('迭代次数k=',k)
            K.append(k)
            #print (k)
            #worksheet.write(2,num,k)
            k=0
            end=time.time();
            t=end-start;
            T.append(t);
        else:
            k+=1 
        i_0=0
        j_0=0
        k_0=0
        w_0=0
        i_1=0
        D=[]
        W=[]
        i=0
    #print ('感知任务的最终真值pj=:\n',round(pj,4))
    FGT.append(pj)
    print (round(pj,4))
   # worksheet.write(3,num,round(pj,3))
    k=0
    
#计算MAE（平均绝对误差）
    j_1=0
    S_m=0 #存储绝对误差的和
    Mae=0
    while j_1<len(A):
        S_m+=abs(A[j_1]-pj)
        j_1+=1
    Mae=S_m/len(A)
    MAE.append(Mae);
    #print ('平均绝对误差为Mae=\n',round(Mae,4))
    print (round(Mae,3))

#计算RMSE（均方根误差）
    k_1=0
    S_r=0
    S_r1=0
    Rmse=0
    while k_1<len(A):
        S_r1+=math.pow((A[k_1]-pj), 2)
        k_1+=1
    S_r=S_r1/len(A)
    Rmse=math.pow(S_r, 0.5)
    RMSE.append(Rmse)
    #print ('均方根误差为Rmse=\n',round(Rmse,4))
    print (round(Rmse,3))
    
    num+=1;
mT=np.mean(T)
print ('运行时间t=',round(mT,6))
#np.set_printoptions(precision = 4)   
#print ('迭代次数k=\n',np.round(K,4))
mK=np.mean(K)
#print ('平均迭代次数为mK=\n',round(mK,4))
print (round(mK,4))

e=0
E=[];#存储平均的误差值
mE=0;#平均的误差值
while e<100:
    er=abs(IPJ[e]-FGT[e])/FGT[e]
    E.append(er)
    e+=1
mE=np.mean(E)
print (round(mE,6))    
#np.set_printoptions(precision = 4)   
#print ('初始数据的平均值IPJ=\n',np.round(IPJ,4))
#mIPJ=np.mean(IPJ)
#print ('平均的初始数据的平均值为mIPJ=\n',round(mIPJ,4))
#print (round(mIPJ,4))

#np.set_printoptions(precision = 4)   
#print ('数据的真值FGT=\n',np.round(FGT,4))
#mFGT=np.mean(FGT)
#print ('平均的数据的真值为mFGT=\n',round(mFGT,4))
#print (round(mFGT,4))

#np.set_printoptions(precision = 4)   
#print ('平均绝对误差为MAE=\n',np.round(MAE,4))
mMAE=np.mean(MAE)#求MAE的平均值
#print ('绝对误差的平均值为mMAE=\n',round(mMAE,4))
print (round(mMAE,4))

#np.set_printoptions(precision = 4)
#print ('均方根误差为RMSE=\n',np.round(RMSE,4)) 
mRMSE=np.mean(RMSE)#求MAE的平均值
#print ('均方根误差的平均值为mRMSE=\n',round(mRMSE,4))  
print (round(mRMSE,4)) 
j_1=0
S_m=0 #存储绝对误差的和
Mae=0
k_1=0
S_r=0
S_r1=0
Rmse=0
pj=0
S=0
#workbook.close()
#np.set_printoptions(precision = 4)
#print ('平均绝对误差为Mae=\n',np.around(MAE,4))
#np.set_printoptions(precision = 4)
#print ('均方根误差为Rmse=\n',np.around(RMSE,4))