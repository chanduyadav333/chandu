import numpy as np
import pandas as pd
'''a=[1,2,3]
b=pd.Series(a)
print(b)
c=pd.Series(a,index=[10,20,30])
print(c)'''
'''d=pd.read_csv('dummydata.txt')
print(d.head(2))'''
'''df={'bikes':['a','b','c'],'speed':[1,2,3]}
dff=pd.DataFrame(df)
print(dff.loc[[0,1,2]])'''

'''s=pd.Series([1,2,3,np.nan])
print(s)
dates=pd.date_range("20010511",periods=6)
print(dates)
n=np.ones((6,5),dtype=int)
print(n)
df= pd.DataFrame(np.random.randn(6,4),index=dates,columns=list("ABCD"))
print(df)
df1= pd.DataFrame(n,index=dates,columns=list("ABCDE"))
print(df1)'''

'''
df=pd.DataFrame(
    {
        "A":pd.Timestamp("20010511"),
        "B":pd.Series(1,index=list(range(4)),dtype=float),
        "C":np.array([3]*4,dtype=int),
        "E":pd.Categorical(["dcdd","dde","iudgeywg","uywfd"]),
        "F":"asd"
    }
)
'''
''''
dates=pd.date_range("20010511",periods=6)
df= pd.DataFrame(np.random.randn(6,4),index=dates,columns=list("ABCD"))
print(df)
print(df.sort_values(by="A",ascending=False))
print("=============================")
print(df.iloc[3:5,0:2])
print(df[df>0])'''


df=pd.read_csv("pokemon_data.csv")
for i,j in df.iterrows():
    print(i,j["Name"],j["Type 1"])
print(df.iloc[2,1])
print(df.sort_values(['Type 1','Speed'],ascending=[1,0]))
df.loc[df['Type 2']=='Poison',['Type 2']]='1'
print("===================")
print(df['Type 2'])
#df.to_csv('E:\\d2.csv',index=False)
df['string_concat']=df['Name']+df['Type 1']+df['Type 2']
df['sum']=df['HP']+df['Attack']+df['Defense']+df['Sp. Atk']+df['Speed'][0:799:2]
print("============================")
print(df['sum'])
