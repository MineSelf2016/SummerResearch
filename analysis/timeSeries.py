#%%
# 提取与COVID-19 相关的微博（未使用）
# 1. 使用weibo_content 字段构建语料库
# 2. 分词
# 3. 计算微博 tf-idf 权重
# 4. 提取相关微博

import pandas as pd 
import os 

# %%
df = pd.read_csv("dataset/sina_cctv_processed_data/uniqueValue/sina_cctv_list.csv", usecols=['pub_time', 'weibo_content', 'forward', 'comment', 'like',
       'weibo_url', 'weibo_topic', 'timeStamp'])

# %%
df.describe()

# %%
