#%%
# 由于爬取的数据并没有标注，故只能选择文本聚类的方式来提取主题；
# 1. 使用LDA 方式，猜测主题数 K ；
# 2. 使用word2vec 计算与肺炎相关信息的相似度，根据相似度区间来提取肺炎相关微博；
# 主题：春晚、肺炎、武汉、国际、Floyd 黑人抗议活动、医生、民法典、开学
# 主题随时间的变化

#%%
import numpy as np 
import pandas as pd 
from collections import Counter 

# %%
df = pd.read_csv("dataset/sina_cctv_processed_data/sina_cctv_list_cut_words.csv")

# %%
df["content_cut"]

# %%
# corpus = " ".join(df["content_cut"])
stopWords = None
with open("analysis/stopWords.txt") as f:
    stopWords = f.read()
    stopWords = stopWords.splitlines()
len(stopWords)

#%%
corpus = []
for sentence in df["content_cut"]:
    for item in sentence.split(" "):
        if item not in stopWords:
            corpus.append(item)
# corpus.append(item for item in (sentence.split(" ") for sentence in df["content_cut"]))

# %%
len(corpus)

# %%
cc = Counter(corpus)

# %%
cc.most_common(200)

# %%
