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
import functools
import time
import os 

# %%
df = pd.read_csv("dataset/sina_cctv_processed_data/sina_cctv_list_cut_words.csv", usecols=['pub_time', 'weibo_content', 'forward', 'comment', 'like',
       'weibo_url', 'weibo_topic', 'timeStamp'])

# %%
df.describe()

#%%
def unifyTimeFormat(date):
       """
       Input: 1月31日 23:33
       Output: 1.31
       """
       try:
              date = date.split(" ")[0]
              date = datetime.strptime(date, '%m月%d日')
              month = date.month
              day = date.day
       except Exception as identifier:
              month = 2
              day = 29
       return str(month) + "." + str(day)

# %%
df["pub_time"] = df["pub_time"].apply(unifyTimeFormat)

# %%
df.groupby(by = "pub_time")

# %%
date_span = []
day_blog_amount = []
# 使用有序字典存储
date_blog = OrderedDict()

for name, group in df.groupby(by = "pub_time"):
       date_blog[name] = group.size 


#%%
def order_rule(date1, date2):
       try:
              date1 = datetime.strptime(date1, '%m.%d')
              month1 = date1.month
              day1 = date1.day
       except Exception as e:
              month1 = 2
              day1 = 29
              pass

       try:
              date2 = datetime.strptime(date2, '%m.%d')
              month2 = date2.month
              day2 = date2.day
       except Exception as e:
              month2 = 2
              day2 = 29


       if month1 > month2:
              return 1
       elif month1 == month2:
              if day1 > day2:
                     return 1
              elif day1 == day2:
                     return 0
              else:
                     return -1
       else:
              return -1

#%%
def sortedDateValues(date_blog):
    keys = date_blog.keys()
    keys = sorted(keys, key = functools.cmp_to_key(order_rule))
    return [(key, date_blog[key]) for key in keys]

#%%
date_blog = sortedDateValues(date_blog)
date_blog = np.array(date_blog)

#%%
date_blog

#%%
plt.plot(date_blog[18:30, 0], date_blog[18:30, 1])




# len(date_span), len(day_blog_amount)

#%%
date_span

# %%
plt.plot(date_span[10:40]), day_blog_amount[10:40])

# %%
print(max(day_blog_amount))

# %%
for i in range(10, 40):
       print(day_blog_amount[i])

# %%
day_blog_amount.index(928)

# %%
date_span[17]

# %%
plt.plot(date_span[10:40], day_blog_amount[10:40])

# %%
