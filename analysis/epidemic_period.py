#%%
# 获取COVID-19 相关的微博元数据与评论数据
# 爬取1月20日至1月31日的数据
# 1. API 爬取
# 2. 自动化框架爬取
# 获取微博url_list
import numpy as np 
import pandas as pd 
import os 
import matplotlib.pyplot as plt 
from utility.TimeConvert import unifyTimeFormat
from utility.TimeConvert import unifyURLFormat

# %%
dataFrame = pd.read_csv("dataset/sina_cctv_processed_data/sina_cctv_list_cut_words.csv")

#%%
dataFrame["pub_time_m_d"] = dataFrame["pub_time"].apply(unifyTimeFormat)
dataFrame["weibo_url"] = dataFrame["weibo_url"].apply(unifyURLFormat)

# %%
for name, group in dataFrame.groupby(by = "pub_time_m_d"):
    period_url_list = []
    print(name)
    print(group.shape[0])
    period_url_list.extend(group["weibo_url"])
    try:
        os.mkdir("dataset/comment/" + name)
        with open("dataset/comment/" + name + "/" + name + ".txt", mode = "w") as f:
            for item in period_url_list:
                f.write(item + "\n")
    except Exception as e:
        pirnt(e)
        pass
    
print(len(period_url_list))

# %%
period_url_list[:2]

# %%
with open("analysis/preprocess/2.txt", mode = "w") as f:
    for item in period_url_list:
        f.write(item + "\n")

# %%
