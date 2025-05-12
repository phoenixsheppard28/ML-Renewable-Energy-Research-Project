import pandas as pd

num_arr=[]

dfn=pd.read_csv('wind.csv')
df=dfn.drop_duplicates(subset=["wind","temp","pressure","humidity","clouds","precipitation","sunshine_hours"],keep='first',inplace=False)
print(len(dfn))
print(len(df))
df.to_csv("wind_fixed")