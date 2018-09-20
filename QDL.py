import quandl
import pandas as pd

quandl.ApiConfig.api_key = 'cEwafLSxcxfDwzNREWup'
Data=quandl.get('NSE/INFIBEAM',column_index='[0:8]')
print(Data)