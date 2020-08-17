from datetime import datetime
import time 

def unifyTimeFormat(date, option = "day"):
       """
       Input: 1月31日 23:33

       option == 'day'
       Output: 1.31;

       option == 'month'
       Output: 1;

       option == 'week'
       Output: (month_day[month] + day - 1) // 7 + 1;
       """
       month_day = [0, 0, 31, 31 + 29, 31 + 29 + 31, 31 + 29 + 31 + 30]
       try:
              date = date.split(" ")[0]
              date = datetime.strptime(date, '%m月%d日')
              month = date.month
              day = date.day
       except Exception as identifier:
              month = 2
              day = 29

       if option == "day":
              return str(month) + "." + str(day)
       elif option == "month":
              return str(month)
       else:
              return str((month_day[month] + day - 1) // 7 + 1)


def unifyURLFormat(weibo_url):
    """
    Input: 'https://weibo.com/2656274875/IrKUN65dn?from=page_1002062656274875_profile&wvr=6&mod=weibotime'

    Output: 'https://weibo.com/2656274875/IrKUN65dn'
    """
    return weibo_url.split("?")[0]


def order_rule(date1, date2):
       """
       Cmp rule:
       return the correct order of the date, instead of sorting by the 'string' type
       1.1 < 1.10
       1.11 < 1.20
       1.21 < 1.30
       """
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
