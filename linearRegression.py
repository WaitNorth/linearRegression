import sys
import pandas as pd
import numpy as np
data = pd.read_csv('./train.csv',encoding='big5')
data = data.iloc[:, 3:]
data[data=='NR']=0
raw_data = data.to_numpy()

month_data = []

print(raw_data[0:18,:])
# month_data = {}
# for month in range(12):
#     sample = np.empty([18, 480])
#     for day in range(20):
#         sample[:, day * 24 : (day + 1) * 24] = raw_data[18 * (20 * month + day) : 18 * (20 * month + day + 1), :]
#     month_data[month] = sample
# print(month_data[1][1])
