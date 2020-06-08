import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# read the data
df=pd.read_csv('Data_day1.csv')
# # Preprocessing:
# print('name of columns = ',df.columns)
# print('overall shape of dataframe ',df.shape)
# print('top 5 rows of dataset ',df.head(n=5))
#
# # 1. Statical Analysis:  compute mean/variance
# print('mean = ',df.mean())
# print('standard deviation = ',df.std())
# print('variance = ', df.var())

# 2. Data visualization: Histogram : to see the data distribution
plt.hist=df.hist(bins=3)
plt.show()

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
