#%%
# 整理已爬取的数据，将数据做成一张表
# 1. dataframe 连接
# 2. 数据去重
# 3. 数据排序
# 4. 时间序列分析
import numpy as np 
import pandas as pd 
import request 
import os
import time, datetime 

#%%
dataFileList = os.listdir("dataset/sina_cctv_processed_data/unityTime")
dataFrame = pd.DataFrame(columns = ["pub_time", "weibo_content", "forward", "comment", "like", "weibo_url", "weibo_topic"])
dataFrame

#%%
for i in range(len(dataFileList)):
    dataFrame = dataFrame.append(pd.read_csv("dataset/sina_cctv_processed_data/unityTime" + "/" + dataFileList[i], usecols = ["pub_time", "weibo_content", "forward", "comment", "like", "weibo_url", "weibo_topic"]))

dataFrame.shape 

# %%
sum(dataFrame.duplicated())

# %%
dataFrame[dataFrame.duplicated()]

# %%
dataFrame = dataFrame.drop_duplicates(["pub_time"])

# %%
dataFrame.shape

# %%
dataFrame.index

# %%
ss = dataFrame["pub_time"]

#%%
for i in range(len(ss)):
    if ss[i].find("已编辑") != -1:
        # print(i, " xxxx ", ss[i])
        print(ss[i].split("已编辑")[0].strip())

# %%
for i in range(len(dataFrame["pub_time"])):
    if dataFrame["pub_time"][i].find("已编辑") != -1:
        # print(i, " xxxx ", ss[i])
        dataFrame["pub_time"][i] = dataFrame["pub_time"][i].split("已编辑")[0].strip()
        # print(ss[i].split("已编辑")[0].strip())


# %%
dataFrame.shape

#%%
# def sort_weibo(df):
dataFrame["timeStamp"] = None
dataFrame["timeStamp"] = dataFrame["pub_time"].apply(lambda x : int(time.mktime(time.strptime("2020年" + x, "%Y年%m月%d日 %H:%M"))))


# %%
dataFrame.sort_values(by = ["timeStamp"], ascending = False, inplace = True)


# %%
dataFrame.reindex(range(dataFrame.shape[0]))

# %%
dataFrame = dataFrame.reset_index(drop = True)

# %%
dataFrame.to_csv("dataset/sina_cctv_processed_data/uniqueValue/sina_cctv_list.csv", sep=",")
