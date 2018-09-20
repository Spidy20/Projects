import quandl
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np


quandl.ApiConfig.api_key = ''
Data=quandl.get('NSE/INFIBEAM')

DF=pd.read_csv('infibeam.csv')

x=DF.loc[:,'High':'Turnover (Lacs)']
y=DF.loc[:,'Open']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)
LR=LinearRegression()
LR.fit(x,y)
Test=[[467.0,440.25,445.55,445.75,7342816.0,33161.98]]
prediction=LR.predict(Test)
score=LR.score(x_test,y_test)
print(prediction)
print(score)
