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



#定义数据和真值之间的距离函数
#计算数组的数据与平均值之间的标准差

#workbook = xlsxwriter.Workbook('data.xlsx') # 建立文件
#worksheet = workbook.add_worksheet('ITD') 




#A= [10,30,60,70,70,80,90,60,50,70]; #参与者的数据
wb = xw.Book('Sdata.xlsx')
sht = wb.sheets[0]
A = sht.range('D3:D406').value
#print(A)

'''
A=[18.1248, 26.4409, 16.4853, 15.2819, 24.2579, 12.4082, 15.4484, 19.8337,
   14.566,  23.2751,
   19.8675, 23.2984, 19.4375, 22.3232, 17.6393, 20.9642, 26.1289, 18.2914,
   17.1892, 17.2757,
   21.1238, 24.4709, 16.5897, 25.6081, 14.9187, 29.8125, 21.9326, 17.9684, 
   15.594,  20.4772,
   18.81,   23.3871, 14.4491, 18.2848, 16.8903, 18.3188, 26.4653, 25.5896,
   17.1845, 18.2053,
   20.4216, 20.1921, 20.9906] 
   19.2993, 18.0382, 30.2858, 26.0451, 20.4934,
   23.3135, 23.9104,
   19.2044, 22.1989, 19.1178, 22.1344, 24.6506, 23.5775, 19.7883, 22.1326, 
   21.5936, 22.8287,
   18.3558, 19.8709, 19.0104, 17.3194, 25.9816, 12.1257, 25.264,  18.6093, 
   19.1312, 17.917,
   22.6135, 22.1848, 16.5791, 15.6459, 22.1623, 22.8218, 23.9975, 15.2383,
   27.1622, 19.9423,
   19.5433] 
   27.1858, 25.2447, 17.7953, 23.0135, 16.1553, 17.9613, 15.4921,
   18.8945, 21.6442,
   13.8295, 18.2452, 17.6743, 20.2892, 20.6487, 24.0889,
   16.0664, 17.172,  17.9397, 18.9056]
'''

def dis(gt, a):#距离,,数据和真值之间的距离
    t = 0;
    i=0
    while i<len(A):
        t +=math.pow((A[i] - pj), 2);
        i+=1
    t =math.pow(t /len(A), 0.5);
    return pow((a - gt), 2) / t;

def weight(gt, a):
    t = 0;
    j=0
    while j<len(A):
        t +=dis(gt, A[j]);
        j+=1
    t /= dis(gt, a);
    t = math.log(t);
    return t;

def truth_update(A, W):
    t=0;
    w=0;
    k=0
    while k<len(A):
        t += W[k] * A[k];
        w += W[k]; 
        k+=1;
    return t / w;  
#生成声望倍数数组

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


num1=0;#循环的次数
while num1<1:
    W=[];#用户的权重
    D=[];#感知数据与真值之间的距离
    PJ=[];#数据的平均值
    k=0
    k_0=0
    i_0=0
    i_1=0
    j_0=0
    w_0=0
    d=0
    sd=0
    dw=0;#数据与权重乘积的和
    sw=0;#权重的和
    #new_A=np.random.normal(20,4,70)#原始数组
    #new_A=Ex_data(A) #生成扩展数组
    #print ('扩展数组new_A=:\n',new_A)
    
    pj=np.mean(A)#求初始数组的平均值
    PJ.append(pj)
    IPJ.append(pj)
    print ('初始数组的平均值pj=:\n',round(pj,4))
    start=time.time()
    while True:
        #print ('第k次迭代k=:\n',k)
        while i_0<len(A):
            w=weight(pj, A[i_0])
            W.append(w);
            i_0+=1
        pj = truth_update(A, W);
        PJ.append(pj)
        np.set_printoptions(precision = 4)
        print ('用户的权重W=:\n',np.around(W,4))
        #print ('感知任务的真值pj=:\n',round(pj,4))
        #print ('感知任务的真值pj=:\n',round(pj,4))
        if (abs(PJ[k]-PJ[k-1])<0.05):
            #print ('迭代次数k=',k)
            K.append(k)
            #worksheet.write(2,num1,k)
            k=0
            end=time.time();
            t=end-start;
            T.append(t);
            break
        else:
            k+=1 
        #print ('感知任务的真值pj=:\n',round(pj,4))
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
    #worksheet.write(3,num1,round(pj,4))
    k=0
    num1+=1;
 
'''  
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
    print (round(Mae,6))
    #worksheet.write(4,num1,round(Mae,4))

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
    print (round(Rmse,6))
    #worksheet.write(5,num1,round(Rmse,4))
    num1+=1;
 '''   
mT=np.mean(T)
print ('运行时间t=',round(mT,4))
#np.set_printoptions(precision = 4)   
#print ('迭代次数k=\n',np.round(K,4))
'''
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
print (round(mMAE,6))

#np.set_printoptions(precision = 4)
#print ('均方根误差为RMSE=\n',np.round(RMSE,4)) 
mRMSE=np.mean(RMSE)#求MAE的平均值
#print ('均方根误差的平均值为mRMSE=\n',round(mRMSE,4))  
print (round(mRMSE,6)) 
j_1=0
S_m=0 #存储绝对误差的和
#Mae=0
k_1=0
S_r=0
S_r1=0
#Rmse=0
pj=0
S=0
#workbook.close()
#np.set_printoptions(precision = 4)
#print ('平均绝对误差为Mae=\n',np.around(MAE,4))
#np.set_printoptions(precision = 4)
#print ('均方根误差为Rmse=\n',np.around(RMSE,4))
'''
    






    

