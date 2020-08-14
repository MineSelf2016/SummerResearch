from datetime import datetime
import time 

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


def unifyURLFormat(weibo_url):
    """
    Input: 'https://weibo.com/2656274875/IrKUN65dn?from=page_1002062656274875_profile&wvr=6&mod=weibotime'

    Output: 'https://weibo.com/2656274875/IrKUN65dn'
    """
    return weibo_url.split("?")[0]