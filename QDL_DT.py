
from sklearn import  tree
from sklearn.model_selection import train_test_split
import pandas as pd
# import quandl
#
# quandl.ApiConfig.api_key = 'cEwafLSxcxfDwzNREWup'
# D=quandl.get('NSE/INFIBEAM', start_date='2018-10-03', end_date='2018-10-03')
# Data=pd.DataFrame(D)
# print(Data)


DF=pd.read_csv('infibeam.csv')
x=DF.loc[:,'High':'Turnover (Lacs)']
y=DF.loc[:,'Open']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)
DT=tree.DecisionTreeRegressor(random_state=42)
DT.fit(x_train,y_train)
print(DT.score(x_test,y_test))
Test=[[239.65,230.35,235.15,234.9,3357625.0,7898.64]]
Prediction=DT.predict(Test)
print(Prediction)