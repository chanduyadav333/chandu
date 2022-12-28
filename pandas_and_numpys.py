import numpy as np
import string
import pandas as pd
df=pd.read_csv("pokemon_data.csv")
dff=df.copy()
print(df)
df['sum']=df['Attack']+df['Defense']+df['Speed'][1:800:2]
print(df['sum'])
print("==========================================================")
df['temp']=df['Type 1']
df['Type 1']=df['Type 2']
df['Type 2']=df['temp']
print(df[['Type 1','Type 2']])
print("===============================================================")
df.loc[df['Name'].str[0]=='V',['new']]=df['Name']
print(df['new'])
new_dta_frm=pd.DataFrame(df['new'])
print(new_dta_frm)
print("=============================================================")
dates=pd.date_range("20010101",periods=800)
df['dates']=dates
df.set_index(df['dates'],inplace=True)
print(df)
