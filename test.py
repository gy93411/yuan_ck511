import pandas as pd
import numpy as np
list_1={'math':[98,99],'language':[88,89]}
df=pd.DataFrame(list_1,index=('xiaozhang','xiaowang'))
print(df)
df.columns=['math1','language1']
print(df)
df.rename(columns=({'math1':'math2','language1':'language2'}),inplace=True)
print(df)
df.rename({'xiaozhang':'xz'},inplace=True)
print(df)
df.iloc[0]=[11,12]
print(df)
df.drop('xz',axis=0,inplace=True)
print(df)
df.drop('math2',axis=1,inplace=True)
print(df)
df=pd.DataFrame(list_1,index=('xiaozhang','xiaowang'))
print(df)

# print(df.loc[df['math']<99].index)
# df.drop(df[df['math']<99].index,axis=0,inplace=True)
# print(df)
df.loc['xiaozhang','math']=np.nan
# x=df[df['math'].notnull()]
# print(x)
#df.dropna(inplace=True)
print(df)