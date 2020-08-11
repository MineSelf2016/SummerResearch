#%%
# 统一将发布时间字段命名为 Time
# 统一列名顺序为 发布时间，微博内容，微博话题，转发量，评论量，点赞量，微博url
# ["pub_time", "weibo_content", "weibo_topic", "forward", "comment", "like", "weibo_url"]
# 从weibo_content 中提取weibo_topic, 从weibo_from 中提取pub_time

import numpy as np 
import pandas as pd 

#%%
def unifyColumns(df):
    # print("how many rows have Nan: ", df.isnull().sum())
    # df = df.dropna(axis = "rows", how = "all")
    df = df.drop(columns = ["S_txt2", "WB_video", "W_img_face"])
    # df = df.drop(columns = ["Time"])
    df = df.drop(columns = ["Unnamed: 0", "头像", "缩略图"])
    return df

#%%
dataframeList = []
for i in range(11):
    csv_path = "dataset/sina_cctv_processed_data/cleanNanValue/sina_cctv_list_" + str(i + 1) + ".csv"
    print(csv_path)
    dataframeList.append(pd.read_csv(csv_path))

#%%
for i in range(2):
    dataframeList[i] = unifyColumns(dataframeList[i])

#%%
for i in range(11):
    print(dataframeList[i].columns, "\n")

#%%
for i in range(10):
    print(dataframeList[i].columns == dataframeList[i + 1].columns)

#%%
for i in range(0, 11):
    dataframeList[i]["WB_from"] = dataframeList[i]["WB_from"].apply(lambda x : x.split(" 来自 ")[0])

#%%
for i in range(len(dataframeList)):
    dataframeList[i].rename(columns = {"WB_from": "pub_time", "WB_text": "weibo_content"}, inplace = True)


# %%
tt = dataframeList[0]
tt.head()

#%%
for i in range(len(dataframeList)):
    dataframeList[i].to_csv("dataset/sina_cctv_processed_data/unityTime/sina_cctv_list_" + str(i + 1) + ".csv")

#%%
# for i in range(0, 11):
#     dataframeList[i]["weibo_topic"] = dataframeList[i]["weibo_content"].apply(lambda x : x.split("】")[0].split("【")[1])


# %%
for i in range(0, 11):
    dataframeList[i]["weibo_topic"] = None
    for idx in range(len(dataframeList[i]["weibo_content"])):
        try:
            dataframeList[i]["weibo_topic"][idx] = dataframeList[i]["weibo_content"][idx].split("】")[0].split("【")[1]
            # print("Index ", i, ": ", dataframeList[2]["weibo_content"][i].split("】")[0].split("【")[1])
        except Exception as e:
            dataframeList[i]["weibo_topic"][idx] = None
            print("Dataframe", i, "Index", idx, e, dataframeList[i]["weibo_content"][idx])
            pass
        

# %%
print(dataframeList[2]["weibo_content"][44])
print(dataframeList[2]["weibo_content"][45])
print(dataframeList[2]["weibo_content"][46])

# %%
