# %%
# 处理评论数据，按照微博发表时间进行聚合
# 1.20 日
# 1. 读取1.20 日微博列表信息；
# 2. 根据微博列表信息聚合出微博评论信息
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

# %%
dataset_comments_1_20 = pd.read_csv("test/dataset_comment/1.20_comments.csv")

dataset_comments_1_20.info()
# %%
len(dataset_comments_1_20["pub_time"])

# %%
len(dataset_comments_1_20["pub_time"].unique())

# %%
