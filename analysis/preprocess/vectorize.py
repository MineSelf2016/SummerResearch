#%%
# 提取与COVID-19 相关的微博
# 构建语料库
# 2. 向量化 vectorizing
import numpy as np 
import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

#%%
df = pd.read_csv("dataset/sina_cctv_processed_data/sina_cctv_list_cut_words.csv", usecols = ["pub_time", "content_cut"])

#%%
vectorizer = CountVectorizer()

#%%
content_cut = df["content_cut"]

#%%
# corpus=["I come to China to travel", 
#     "This is a car polupar in China",          
#     "I love tea and Apple ",   
#     "The work is to write some papers in science"]
     
# vectorizer.fit_transform(corpus)

# %%
count_vector = vectorizer.fit_transform(content_cut)
tf_idf_Transformer = TfidfTransformer()
tf_idf = tf_idf_Transformer.fit_transform(count_vector)

#%%
tf_idf

