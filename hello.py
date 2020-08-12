#%%
import utility.URLConvert as url_convert
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import requests
import json

# %%

url = "https://api.weibo.com/2/comments/show.json?id=4534110062382062&access_token=2.00t5fpdHh28sPC6124e7664b0zN_ne&count=20&page=1"

payload = {}
headers= {}

#%%
response = requests.request("GET", url, headers=headers, data = payload)

#%%
r = json.loads(response.text)

# %%
len(r["comments"])

# %%
r["comments"][0]

# %%
case = r["comments"][0]

# %%
case.keys()

# %%
case["created_at"]

# %%
del case["user"] 

#%%    
del case["status"]

# %%
comment = {
    "comment_id" : case["id"],
    "created_at" : case["created_at"],
    "comment_text" : case["text"],
    "comment_text_len" : len(case["text"]),
    "floor_number" : case["floor_number"],
    "user_id" : case["user"]["id"],
    "likes" : 10
}

comment

#%%
import pandas as pd 

#%%
pd.DataFrame([comment])

# %%
dataFrameList = []
for i in range(11):
    # 1.csv
    dataFrameList.append(pd.read_csv("dataset/sina_cctv_processed_data/unityTime/sina_cctv_list_" + str(i + 1) + ".csv"))

#%%
ss = 0
for i in range(11):
    ss += dataFrameList[i].shape[0]
    print(dataFrameList[i].shape)

# %%
ss 

