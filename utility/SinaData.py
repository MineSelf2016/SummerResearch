#%%
import requests
import json
import utility.URLConvert as cvt
import numpy as np 
import pandas as pd 
import time

#%%
def get_weibo_info(url):
    ids = cvt.url_to_mid(url)
    request_url = "https://api.weibo.com/2/statuses/count.json"
    payload = {
        "access_token" : "2.00nekpaGoKmofCff2b09c93aGXcCTC",
        "ids" : ids
    }
    headers= {}
    response = requests.request("GET", request_url, headers = headers, params = payload)
    print("response : ", response.text)
    r = json.loads(response.text)[0]
    return r

#%%
def get_comment_list(url, total_num = 100, count = 100):
    ids = cvt.url_to_mid(url)
    request_url = "https://api.weibo.com/2/comments/show.json"
    
    result = []
    for i in range(1, total_num // count + 1):
        payload = {
            "access_token" : "2.00nekpaGoKmofCff2b09c93aGXcCTC",
            "id" : ids,
            "count" : count,
            "page" : i
        }
        headers= {}

        response = requests.request("GET", request_url, headers=headers, params = payload)
        
        try:
            comments_itr = json.loads(response.text)["comments"]
        except Exception as e:
            print(e)
            return result

        for k in range(len(comments_itr)):
            case = comments_itr[k]
            comment = {
                "comment_id" : case["id"],
                "created_at" : case["created_at"],
                "comment_text" : case["text"],
                "comment_text_len" : len(case["text"]),
                "floor_number" : case["floor_number"],
                "user_id" : case["user"]["id"],
                "likes" : 10
            }
            result.extend([comment])
        
        print("The " + str(i * count) + " have finished!\n")
        # 每次请求后休息 3 秒
        time.sleep(3)
    
    return result

# %%
url = "IweWzd6WQ"
r = get_weibo_info(url)
r 

#%%
# 获取评论的数量 total_num 
total_num = r["comments"]
r = get_comment_list(url, 1000)

# %%
df = pd.DataFrame(r)

# %%
df 

#%%
df.to_csv("dataset/temp1.csv")

# %%
# https://weibo.com/cctvxinwen?is_search=1&visible=0&is_ori=1&is_pic=1&is_video=1&is_music=1&is_article=1&is_forward=1&is_text=1&key_word=%E8%82%BA%E7%82%8E&start_time=2020-01-01&end_time=2020-02-29&is_tag=0&profile_ftype=1&page=2#feedtop


