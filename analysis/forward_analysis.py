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
              "like": group["like"].sum(),
              "pub_num": group.shape[0]
       }

#%%
def sortedDateValues(date_blog):
    keys = date_blog.keys()
    keys = sorted(keys, key = functools.cmp_to_key(order_rule))
    return [(key, int(date_blog[key]["forward"]), int(date_blog[key]["comment"]), int(date_blog[key]["like"]), int(date_blog[key]["pub_num"])) for key in keys]

#%%
date_blog = sortedDateValues(date_blog)
date_blog_df = pd.DataFrame(date_blog)


#%%
date_blog_df = date_blog_df.rename(columns = {
       0: "date",
       1: "forward",
       2: "comment",
       3: "like",
       4: "pub_num"
})

# %%
# 微博发布量统计图：
# 按日发布量、周发布量、月发布量绘制
# 微博日发布量：
# 分为3个阶段：0 ～ 20，20 ～ 150-40，150-40 ～ 150
plt.ylabel = "pub_num"
plt.plot(date_blog_df[:]["date"], date_blog_df[:]["pub_num"])
plt.xticks([])
plt.title("the number of everyday forward".title(), fontdict = {"size": "14"})
plt.ylabel = "number"
plt.text(35, 100, "mean: 51.875", fontdict = {"size": "12"})
plt.text(35, 93, "time span: 1.1 ~ 5.31", fontdict = {"size": "12"})
print(plt.ylabel)
plt.savefig("images/forward/day_forward.png", dpi = 300)
plt.show()

#%%
date_blog_df[:]["pub_num"].mean()

#%%
# 分为3个阶段：0 ～ 20，20 ～ 150-40，150-40 ～ 150
plt.ylabel = "pub_num"
plt.plot(date_blog_df[0:20]["date"], date_blog_df[0:20]["pub_num"])
plt.text(0, 45, "mean: 31.75", fontdict = {"size": "12"})
plt.text(0, 43, "time span: 1.1 ~ 1.19", fontdict = {"size": "12"})
plt.title("the number of forward of early stage".title(), fontdict = {"size": "14"})
plt.savefig("images/forward/early_stage_forward.png", dpi = 300)
plt.show()

#%%
date_blog_df[0:20]["pub_num"].mean()

# %%
plt.ylabel = "pub_num"
plt.plot(date_blog_df[20:-40]["date"], date_blog_df[20:-40]["pub_num"])
plt.text(10, 110, "mean: 61.5", fontdict = {"size": "12"})
plt.text(10, 105, "time span: 1.20 ~ 4.20", fontdict = {"size": "12"})
plt.xticks([])
plt.title("the number of forward of middle stage".title(), fontdict = {"size": "14"})
plt.savefig("images/forward/middle_stage_forward.png", dpi = 300)
plt.show()

#%%
date_blog_df[20:-40]["pub_num"].mean()

#%%
plt.ylabel = "pub_num"
plt.plot(date_blog_df[-40:]["date"], date_blog_df[-40:]["pub_num"])
plt.text(0, 56, "mean: 39.8", fontdict = {"size": "12"})
plt.text(0, 54, "time span: 4.20 ~ 5.31", fontdict = {"size": "12"})
plt.xticks([])
plt.title("the number of forward of later stage".title(), fontdict = {"size": "14"})
plt.savefig("images/forward/later_stage_forward.png", dpi = 300)
plt.show()

#%%
date_blog_df[-40:]["pub_num"].mean()

# %%
