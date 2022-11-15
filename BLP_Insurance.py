# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 11:39:04 2022

@author: bobme
"""

import pandas as pd
import numpy as np
import pyblp
import scipy.stats as stats
import random
from random import seed


df1=pd.read_csv(r'C:\Users\bobme\Desktop\ECON 847\HW\BLP HW 3\blp_data_hw3.csv')
df1=df1.drop(df1.index[100:1400])
j=100 #number of products
f=5 #number of Insurers per market
r=10 #number of counties/markets
t=2 #number of periods
mu_s=0.1
sigma_s=0.5
lower_s=0
upper_s=0.2
seed(1)
s=stats.truncnorm.rvs((lower_s-mu_s)/sigma_s,(upper_s-mu_s)/sigma_s,loc=mu_s,scale=sigma_s,size=j)
w=[]
for i in range(j):
    w.append(random.random())

p=[]
for i in range(j):
    p.append(random.random())
    


df=pd.DataFrame(1,index=np.arange(100),columns=['product_id','insurer_id','county_id','time_id','share','premium','av_d','hmo','w'])

df.loc[:,'share']=s
df.loc[:,"premium"]=p

AVD=[]
for i in range(j):
    AVD.append(random.random())

df.loc[:,"av_d"]=AVD

HMO=[]
for i in range(j):
    HMO.append(np.random.choice([0,1]))
df.loc[:,"hmo"]=HMO

df.loc[:,'w']=w
# =============================================================================
# for col in df1.columns:
#     print(col)
# =============================================================================

df.loc[:,'county_id']=df1.loc[:,' mkt']
df.loc[:,'time_id']=df1.loc[:,' time']
df.loc[:,'insurer_id']=df1.loc[:,' firm']
df.loc[:,'product_id']=df1.loc[:,' prod']
# =============================================================================
# df.loc[:,"product_id"]=list(range(j))
# arr1=[1,2]
# df.loc[:,'time_id']=arr1*int(j/t)
# df.loc[:,'county_id']=np.repeat(list(range(int(j/(2*t)))),int(t))
# df.loc[:,"insurer_id"]=ins
# 
# =============================================================================

df.to_csv(r'C:\Users\bobme\Desktop\ECON 850\Research Data\sim_data.csv',index=False, header=True)

pyblp.options.digits=2
pyblp.options.verbose=False
pyblp.__version__






























































