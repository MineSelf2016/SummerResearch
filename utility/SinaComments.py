#%%
import numpy as np 
import matplotlib.pyplot as plt 
import requests
import json

# %%

url = "https://api.weibo.com/2/comments/show.json?id=4533799314792533&access_token=2.00t5fpdHh28sPC6124e7664b0zN_ne&count=5&page=1"

payload = {}
headers= {}

#%%
response = requests.request("GET", url, headers=headers, data = payload)

#%%
r = json.loads(response.text)

#%%
r.keys()

#%%
len(r["comments"])

# %%
r["comments"][1]["text"]

#%%[markdown]
### head2
# 123 </br>
# json 转 dataframe 再转 xlsx
# 检测 page 值与 count 值数据是否有重合，无重合，使用pageitr 做翻页

# %%
