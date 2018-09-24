# import quandl
# quandl.ApiConfig.api_key = ''
# Data=quandl.get('NSE/INFIBEAM')

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd


DF=pd.read_csv('infibeam.csv')

x=DF.loc[:,'High':'Turnover (Lacs)']
y=DF.loc[:,'Open']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)
LR=LinearRegression()
LR.fit(x_train,y_train)
Test=[[239.65,230.35,235.15,234.9,3357625.0,7898.64]]
prediction=LR.predict(Test)
score=LR.score(x_test,y_test)
print(prediction)
print(score)
