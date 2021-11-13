import requests
# import datetime
from bs4 import BeautifulSoup
from pymongo import MongoClient 
# from flask import Flask, render_template, jsonify, request

# app = Flask(__name__)                        
# client = MongoClient('localhost', 27017)
# db = client.test1                       

# docs = [{'menus': ['1','2','31','41','51'],'rating': 1},
# {'menus': ['1','2','7','8','10'],'rating': 2},
# {'menus': ['1','2','4','7','0'],'rating': 3},
# {'menus': ['1','41','51','7','8'],'rating': 4},
# {'menus': ['1','4','6','2','3'],'rating': 5},
# {'menus': ['1','3','41','6','7'],'rating': 1}]

# for doc in docs:
#     db.postInfo.insert_one(doc)

# all_menus = list(db.postInfo.find({},{'_id' : False}))
# #all_menus = [{'menus':[],'rating':1},{'menus':[],'rating':1},{}...]
# menus_receive = ['1','2','3','4','5']
# count = 0
# total_rating = 0
# total_count = 0

# for i in range(len(all_menus)):
#     for menu_receive in menus_receive:
#         if menu_receive in all_menus[i]['menus']:
#             count += 1
#             # print(count)
#         else:
#             continue
#     if count >= 3:
#         total_rating += all_menus[i]['rating']
#         total_count += 1
#         # print(total_rating)
#         # print(total_count)
#         count = 0
#     else:
#         count = 0
#         continue

# average_rating = total_rating / total_count

# print(average_rating)
# print(total_rating)
# print(total_count)
# print(count)

# d_today = datetime.date.today()
# d_today_str = d_today.strftime('%Y-%m-%d')

# # url = 'https://www.kaist.ac.kr/kr/html/campus/053001.html?dvs_cd=icc&stt_dt=2021-11-06'
url = 'https://www.kaist.ac.kr/kr/html/campus/053001.html?dvs_cd=icc&stt_dt=2021-10-29'
# url_today = url + d_today_str

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

breakfirst = soup.select_one('#tab_item_1 > table > tbody > tr > td:nth-child(3)').text
breakfirsts = breakfirst.replace("*","").replace("\t","").replace("\n","").replace("\r","_").split("_")
# # breakfirsts_list = breakfirsts.split(" ")[0].split("\r")
# # print(breakfirsts.rstrip())
for breakfirst in breakfirsts:
    if(breakfirst == ""):
        breakfirsts.remove("")
# doc ={'menu':breakfirsts[2],'star':star_recieve}
# db.menu.insert_one(doc)
print(breakfirsts)