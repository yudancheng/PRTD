# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 11:29:28 2022

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



#定义数据和真值之间的距离函数
#计算数组的数据与平均值之间的标准差

#workbook = xlsxwriter.Workbook('data.xlsx') # 建立文件
#worksheet = workbook.add_worksheet('ITD') 




#A= [10,30,60,70,70,80,90,60,50,70]; #参与者的数据
wb = xw.Book('Sdata.xlsx')
sht = wb.sheets[0]
A = sht.range('D329:D378').value
print(A)


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

K=[];#存储迭代的次数
IPJ=[];#初始数组的平均值
FGT=[];#最终的真值
T=[];#程序运行的时间
Q=[];



num1=0;#循环的次数
while num1<1:
    PJ=[]
    k=1
    i_0=0
    W=[]
    #new_A=np.random.normal(20,4,70)#原始数组
    #new_A=Ex_data(A) #生成扩展数组
    #print ('扩展数组new_A=:\n',new_A)
    
    pj=np.mean(A)#求初始数组的平均值
    PJ.append(pj)
    IPJ.append(pj)
    print ('初始数组的平均值pj=:\n',round(pj,4))
    start=time.time()
    while k>0:
        #print ('第k次迭代k=:\n',k)
        while i_0<len(A):
            w=weight(pj, A[i_0])
            W.append(w);
            i_0+=1
        pj = truth_update(A, W);
        PJ.append(pj)
        np.set_printoptions(precision = 4)
        
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
        W=[]
        i=0
    print ('感知任务的最终真值pj=:\n',round(pj,4))
    k=0
    q=0
    q_1=0
    QK=[]
    R=[]
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
        R_0=1/(1+math.exp(-(QK[j]-1)))
        R.append(R_0)
        j+=1
    np.set_printoptions(precision = 4)
    print ('更新后的用户的声望值R=:\n',np.around(R,4))
    
    e=0
    E=[];#存储平均的误差值
    while e<len(A):
        er=abs((A[e]-pj)/pj)
        E.append(er)
        e+=1
    np.set_printoptions(precision = 4)
    print ('误差值E=:\n',np.around(E,4))
 
    num1+=1;
    


    






    

