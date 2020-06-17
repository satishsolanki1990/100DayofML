import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import time



# read the data
df=pd.read_csv('datasets_619455_1106121_Marketing_Data.csv')

# little summary of the data
# print(df.head)
# print(df.columns)

# histogram of the variables to check the assumption of "homoscedasticity"
# x=np.arange(0,len(df))
# plt.scatter(x,df['youtube'])
# plt.scatter(x,df['facebook'])
# plt.scatter(x,df['newspaper'])
# plt.show()

# # linear regression without normalization
# X=df.loc[:,df.columns!='sales']
# X=X.to_numpy()
# Y=df['sales']
# Y=Y.to_numpy()
# t=time.time()
# reg=LinearRegression().fit(X,Y)
# print(reg.score(X,Y)) #0.9004752358539351
# print(reg.coef_) #[0.04523544 0.18839783 0.00427949]
# print(reg.intercept_) #3.505870994465022
# print(time.time()-t) # 0.0026
#
# # with normalization mean/var
# X=df.loc[:,df.columns!='sales']
# X=X-X.mean()/X.var()
# X=X.to_numpy()
# Y=df['sales']
# Y=Y.to_numpy()
# t=time.time()
# reg=LinearRegression().fit(X,Y)
# print(reg.score(X,Y)) #0.9004752358539351
# print(reg.coef_)#[0.04523544 0.18839783 0.00427949]
# print(reg.intercept_)#3.523127447330099
# print(time.time()-t)#0.0019
#
# # with normalization max/min
# X=df.loc[:,df.columns!='sales']
# X=(X-X.min())/(X.max()-X.min())
# X=X.to_numpy()
# Y=df['sales']
# Y=Y.to_numpy()
# t=time.time()
# reg=LinearRegression().fit(X,Y)
# print(reg.score(X,Y)) #0.9004752358539351
# print(reg.coef_)#[16.0513451  11.21343857  0.51662026]
# print(reg.intercept_)#3.523127447330099
# print(time.time()-t)#0.0019




# dataframe slicing
#*****iloc[row,col] is integer based slicing*****
# print(df.iloc[2]['Age']) # 2nd row with info
# print(df.iloc[2,:].values) # 2nd row same as above but values in numpy array
# print(df.iloc[:,2]) # 2nd column
# print(df.iloc[0:2,2]) # 2nd column and 0:2 rows
# print(df.iloc[0:2,:]) # 0:2 row
# print(df.iloc[[1,3,5],[2,3]]) # list wise slicing

#*****loc[index(rows):name of columns] name based slicing*****
#*****iloc[row,col] is integer based slicing*****
# print(df.loc[[1,3,5],['Age','Salary']])
# print(df.loc[df['Age'].isin([27.0,27.5,38,35,40])])
# print(df.loc[df['Age']>=30])

# # Preprocessing:
# print('name of columns = ',df.columns)
# print('overall shape of dataframe ',df.shape)
# print('top 5 rows of dataset ',df.head(n=5))
#
# 1. Statical Analysis:  compute mean/variance
# print('mean = ',df.mean())
# print('standard deviation = ',df.std())
# print('variance = ', df.var())

# 2. Data visualization: Histogram : to see the data distribution
# plt.hist=df.hist(bins=3)
# plt.show()

# 3. missing data: there are two ways (1) delete that raw (2) use mean variance to assign value


# 4. Categorical data encoder


# 5. feature Scaling or  Normalization: there are many ways to normalize, every technique has
# its limitation and strength. Following techniques are usually followed
#   (1). Max-min normalization
#   (2). mean/variance normalization or mean/std normalization
#   (3). log normalization
#   (4).


# 6. feature selection : based on histogram or Heatmap

# 8. dataset split (test/train/val)
