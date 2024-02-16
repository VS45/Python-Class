import pandas as pd
import numpy as np 
# creating an array
data=np.array([[1,4],[2,5],[3,6]])
#print(data)

# creating data frames with pandas
df=pd.DataFrame(data,columns=["col1","col2"],index=['row1','row2','row3'])
print(df)