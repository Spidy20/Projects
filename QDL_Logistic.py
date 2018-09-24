import pandas as pd
from sklearn.linear_model import  LogisticRegression
from sklearn.model_selection import train_test_split

Data=pd.read_csv('infibeam.csv')

x=Data.loc[:,'High':'Turnover (Lacs)']
y=Data.loc[:,'Open']

x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2,random_state=42)
Log_reg=LogisticRegression()
Log_reg.fit(x,y)

Test=[[239.65,230.35,235.15,234.9,3357625.0,7898.64]]
prediction=Log_reg.predict(Test)
Score=Log_reg.score(x_test,y_test)
print(Score)
print(prediction)