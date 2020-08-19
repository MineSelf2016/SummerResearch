#%%
# 提取与COVID-19 相关的微博（未使用）
# 1. 使用weibo_content 字段构建语料库
# 2. 分词
# 3. 计算微博 tf-idf 权重
# 4. 提取相关微博
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from collections import OrderedDict
from datetime import datetime
from utility.TimeConvert import unifyTimeFormat, order_rule
import functools
import time
import os 

# %%
df = pd.read_csv("dataset/sina_cctv_processed_data/sina_cctv_list_cut_words.csv", usecols=['pub_time', 'weibo_content', 'forward', 'comment', 'like',
       'weibo_url', 'weibo_topic', 'timeStamp', "content_cut"])

# %%
df.info()

# %%
# 微博发布量统计图：
# 按日发布量、周发布量、月发布量绘制

# %%
# df["pub_time"]
# df["pub_time_m_d"] = None 
df["Month"] = None 
df["Week"] = None
df["Day"] = None


# %%
df["Month"] = df["pub_time"].apply(lambda x : unifyTimeFormat(x, "month"))

# %%
df["Week"] = df["pub_time"].apply(lambda x : unifyTimeFormat(x, "week"))

# %%
df["Day"] = df["pub_time"].apply(lambda x : unifyTimeFormat(x, "day"))


# %%
df["Month"].unique(), df["Week"].unique(), df["Day"].unique()


# %%
# 使用有序字典存储
date_blog = OrderedDict()

for name, group in df.groupby(by = "Day"):
       # date_blog[name] = group.shape[0] 
       date_blog[name] = {
              "forward": group["forward"].sum(),
              "comment": group["comment"].sum(),
              "like": group["like"].sum()
       }

#%%
def sortedDateValues(date_blog):
    keys = date_blog.keys()
    keys = sorted(keys, key = functools.cmp_to_key(order_rule))
    return [(key, int(date_blog[key]["forward"]), int(date_blog[key]["comment"]), int(date_blog[key]["like"])) for key in keys]

#%%
date_blog = sortedDateValues(date_blog)
date_blog_df = pd.DataFrame(date_blog)


#%%
date_blog_df = date_blog_df.rename(columns = {
       0: "date",
       1: "forward",
       2: "comment",
       3: "like"
})

# %%
plt.ylabel = "comment"
plt.plot(date_blog_df[30:60]["date"], date_blog_df[30:60]["comment"])
# plt.plot(date_blog_df[20:30]["date"], date_blog_df[20:30]["comment"])
# plt.plot(date_blog_df[20:30]["date"], date_blog_df[20:30]["like"])
# plt.plot(date_blog_df[1:10][0], date_blog_df[1:10][3])
plt.show()

# plt.plot(date_blog[20:30, 1])

# %%
