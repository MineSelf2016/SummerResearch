#%%
# 提取与COVID-19 相关的微博
# 构建语料库
# 1. 分词 tokening
import pandas as pd 
import jieba 
import os 
from sklearn.feature_extraction.text import CountVectorizer

# %%
df = pd.read_csv("dataset/sina_cctv_processed_data/uniqueValue/sina_cctv_list.csv", usecols=['pub_time', 'weibo_content'])

# %%
df.describe()

#%%
def get_stop_words_list(path):
    #从文件导入停用词表
    stpwrd_dic = open(stpwrdpath, 'r')
    stpwrd_content = stpwrd_dic.read()
    #将停用词表转换为list  
    stpwrdlst = stpwrd_content.splitlines()
    stpwrd_dic.close()
    return stpwrdlst

stpwrdpath = "utility/stop_words.txt"
stop_words_list = get_stop_words_list(stpwrdpath)
stop_words_list.append("展开")
stop_words_list.append("全文")

len(stop_words_list)


#%%
df["content_cut"] = None 

#%%
df["content_cut"] = df["weibo_content"].apply(lambda x : " ".join(jieba.cut(x)).split(" "))

#%%
# 将weibo_content 内容完成分词，并去除非汉字字符与停用词
def get_content_cut(content):
    result = ""
    for word in content:
        if (word not in stop_words_list):
            # 单个长度字符可能是非汉字符号，需判断
            if (len(word) == 1):
                if '\u4e00' <= word <= '\u9fa5':
                    result = result + " " + word
            # 两个及以上长度词不需要判断
            else:
                result = result + " " + word

    return result

print(get_content_cut(result))

#%%
df["content_cut"] = df["content_cut"].apply(get_content_cut)

#%%
df2 = pd.read_csv("dataset/sina_cctv_processed_data/uniqueValue/sina_cctv_list.csv", usecols=["pub_time", "weibo_content", "forward", "comment", "like", "weibo_url", "weibo_topic", "timeStamp"])

#%%
df2["content_cut"] = df["content_cut"]

#%%
df2.to_csv("dataset/sina_cctv_processed_data/sina_cctv_list_cut_words.csv", index = False)
