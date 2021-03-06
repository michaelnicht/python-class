# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import sys 
from IPython.display import display

#assignment 1:

shrubs=pd.read_csv('plants2017.csv')
df = pd.DataFrame(shrubs)
shr=df.loc[df['Plant']=='shrub']
df.reset_index(drop=True)
display(shr)

#ask: how does one give a whole list as input to a function, and have it also give a new list as its product?

GPSlat=pd.read_csv('plants2017.csv', index_col=1)
GPSlat1=np.deg2rad(GPSlat)
lat=(GPSlat1*40008000)/360
GPSlon=pd.read_csv('plants2017.csv', index_col=0)
GPSlon1=np.deg2rad(GPSlon)
lon=((GPSlon1*40075160)/360)*np.cos(GPSlat)

print(lon)
print(lat)
#def, keyword argument
def shrubs2017 (df, shr):
    data2=shr[df['height_m']>0.5]
    return data2
print(shrubs2017)

#assignment 2:
PH=pd.read_csv('PH2017.csv')
df2 = pd.DataFrame(PH)
#display(df2)

GPSlat=pd.read_csv('PH2017.csv', index_col=1)
GPSlat1=np.deg2rad(GPSlat)
lat=(GPSlat1*40_008_000)/360
GPSlon=pd.read_csv('PH2017.csv', index_col=2)
GPSlon1=np.deg2rad(GPSlon)
lon=((GPSlon1*40_075_160)/360)*np.cos(GPSlat)
#the coordinates for x and y in the origin were calculated under the assumption  that ymin and xmin are equal to zero. 

#basically same question as before
def scale(PAx,PAy):
    Px=((PAx−222_5)/(3222_5−222_5))*3000)//200
    Py=(((PAy−475)/(3475−475))*3000)//200
    return Py,Px
print scale(450,450)

df2.insert(loc=4, column='X', value=Px)
df2.insert(loc=5, column='Y', value=Py)

#how to create this array?
b=np.array((15,15), Px, Py)
        
#assignment 3:
import numpy as np
import pandas as pd
#PlantA=read_csv('plants2017.csv', index_col='height_m','leaf_length_cm','leaf_aspect_ratio','bud_length_cm')
PlantA=pd.read_csv('plants2017.csv')
plant=PlantA.iloc[index_col=3,4,5,6]       
categories=np.array([[1.2,3.5,2.0,	2.3],[1.8,	1.5,1.2,2.3],[0.7,2.1,10.2,1.5],[0.7,2.2,3.1,1.7]])
diff=categories-plant
dist = np.sqrt(np.sum(diff**2,axis=1))
nearest = np.argmin(dist)
print(nearest)

df2.insert(loc=6, column='species', value=nearest)



    
    
    
    
    
    
    
    
    
    
    