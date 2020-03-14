import pandas as pd
import numpy as np
def sum_matrix(a,b):
    return a.append(b)
df1=pd.DataFrame([[1,2],[3,4]],columns=['A','B'])
df2=pd.DataFrame([[6,5],[7,9]],columns=['A','B'])
print(sum_matrix(df1,df2))