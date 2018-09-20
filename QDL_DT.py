import quandl
from sklearn import  tree
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.preprocessing import minmax_scale

quandl.ApiConfig.api_key = ''
Data=quandl.get('NSE/INFIBEAM')

# DF=pd.read_csv('infibeam.csv')
# x=DF.loc[:,'High':'Turnover (Lacs)']
# y=DF.loc[:,'Open']

Boston = load_boston()
x = Boston.data
y = Boston.target
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)
DT=tree.DecisionTreeRegressor(random_state=42)
DT.fit(x_train,y_train)
print(DT.score(x_test,y_test))
# Test=[[467.0,440.25,445.55,445.75,7342816.0,33161.98]]
# Prediction=DT.predict(Test)
# print(Prediction)


