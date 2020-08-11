#%%
# 处理原始sina_cctv 数据集合
# 该数据集为 微博列表页 数据，从该数据集中提取出需要爬取的 微博详情页
# 下面开始数据清洗
import numpy as np
import pandas as pd 

#%%
def cleanNanValue(df):
    print("how many rows have Nan: ", df.isnull().sum())
    df = df.dropna(axis = "rows", how = "all")
    print("after clean Nan, the shape is: ", df.shape)
    return df


#%%
dataframeList = []
for i in range(11):
    csv_path = "dataset/sina_cctv_raw_data/sina_cctv_list_" + str(i + 1) + ".csv"
    print(csv_path)
    dataframeList.append(pd.read_csv(csv_path))

print(len(dataframeList))

#%%
dataframeList[0] = cleanNanValue(dataframeList[0])
dataframeList[0].shape 

#%%
for i in range(len(dataframeList)):
    dataframeList[i] = cleanNanValue(dataframeList[i])
    dataframeList[i].to_csv("dataset/sina_cctv_processed_data/sina_cctv_list_" + str(i + 1) + ".csv")

