#%%
import utility.URLConvert as url_convert
import numpy as np 
import matplotlib.pyplot as plt 
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
