import requests
import datetime
from bs4 import BeautifulSoup
from pymongo import MongoClient 
from flask import Flask, render_template, request

app = Flask(__name__)                        
client = MongoClient('localhost', 27017)  
db = client.test1                     

##금일 메뉴 dictionary 형태로 반환{'breakfirst' : menus_breakfirst_list,'lunch':menus_lunch_list, 'dinner' : menus_dinner_list}
def todayMenu(d_today_str):
    # url = 'https://www.kaist.ac.kr/kr/html/campus/053001.html?dvs_cd=icc&stt_dt=2021-11-06'
    url = 'https://www.kaist.ac.kr/kr/html/campus/053001.html?dvs_cd=icc&stt_dt='
    url_today = url + d_today_str

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_today,headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    times = ['breakfirst','lunch','dinner']

    for time in times:
        selector1 = '#tab_item_1 > table > tbody > tr > td:nth-child('
        selector2 = ')'
        if time == 'breakfirst':
            selector_time = '1'
            selector_final = selector1 + selector_time + selector2
            menus_breakfirst = soup.select_one(selector_final).text
            menus_breakfirst_list = menus_breakfirst.replace("*","").replace("\t","").replace("\n","").replace("\r","_").split("_")
            for menu_breakfirst in menus_breakfirst_list:
                if(menu_breakfirst == ""):
                    menus_breakfirst_list.remove("")
        elif time == 'lunch':
            selector_time = '2'
            selector_final = selector1 + selector_time + selector2
            menus_lunch = soup.select_one(selector_final).text
            menus_lunch_list = menus_lunch.replace("*","").replace("\t","").replace("\n","").replace("\r","_").split("_")
            for menu_lunch in menus_lunch_list:
                if(menu_lunch == ""):
                    menus_lunch_list.remove("")
        else:
            selector_time = '3'
            selector_final = selector1 + selector_time + selector2
            menus_dinner = soup.select_one(selector_final).text
            menus_dinner_list = menus_dinner.replace("*","").replace("\t","").replace("\n","").replace("\r","_").split("_")
            for menu_dinner in menus_dinner_list:
                if(menu_dinner == ""):
                    menus_dinner_list.remove("")
        
    menus = {'breakfirst' : menus_breakfirst_list,'lunch':menus_lunch_list, 'dinner' : menus_dinner_list}
    return menus

##금일 날짜 str형태로 반환
def strToday():
    d_today = datetime.date.today()
    d_today_str = d_today.strftime('%Y-%m-%d')
    return d_today_str

##DB에서(all_menus) menus_receive와 동일한 메뉴들의 평균 평점
def averageRating(all_menus,menus_receive):
    count = 0
    total_rating = 0
    total_count = 0

    for i in range(len(all_menus)):
        for menu_receive in menus_receive:
            if menu_receive in all_menus[i]['menus']:
                count += 1
            else:
                continue
        if count >= 3:
            total_rating += all_menus[i]['rating']
            total_count += 1
            count = 0
        else:
            count = 0
            continue
    
    return total_rating / total_count

#all_Info 에서 menus와 일치하는 정보를 리스트 형태로 반환 [{정보},{정보},,,]
def usersInfo(all_Info,menus):
    count = 0
    total_info =[]
    for i in range(len(all_Info)):
        for menu in menus:
            if menu in all_Info[i]['menus']:
                count += 1
            else:
                continue
        if count >= 3:
            show_info = {'userId': all_Info[i]['userId'],'postDate':all_Info[i]['postDate'],'rating':all_Info[i]['rating'],
            'comment' : all_Info[i]['comment']}
            total_info.append(show_info)
            count = 0
        else:
            count = 0
            continue    
    return total_info


@app.route('/main/post', methods=['POST'])
def post_memo():
		# 1. 클라이언트로부터 데이터를 받기
    userId_receive = request.form['userId_give']
    postDate_receive = request.form['postDate_give']
    time_receive = request.form['time_give']
    menus_receive = request.form['menus_give']
    rating_receive = request.form['rating_give']
    comment_receive = request.form['comment_give']
    
    # 2. mongoDB 에 입력
    doc = {'userId': userId_receive,'postDate': postDate_receive,'time': time_receive,
    'menus': menus_receive,'rating': rating_receive,'comment': comment_receive}
		
    db.postInfo.insert_one(doc)

    return render_template('/main.html')

@app.route('/main')
def show_main():
    all_Info = list(db.postInfo.find({},{'_id':False}))

    menus = todayMenu(strToday())
    
    menus_breakfirst = menus['breakfirst']
    menus_lunch = menus['lunch']
    menus_dinner = menus['dinner']
    
    rating_breakfirst = averageRating(all_Info,menus_breakfirst)
    rating_lunch = averageRating(all_Info,menus_lunch)
    rating_dinner = averageRating(all_Info,menus_dinner)

    usersInfo_breakfirst = usersInfo(all_Info,menus_breakfirst)
    usersInfo_lunch = usersInfo(all_Info,menus_lunch)
    usersInfo_dinner = usersInfo(all_Info,menus_dinner)

    return render_template('main.html', showToday = strToday(), menusBreakfirst = menus_breakfirst,
    menusLunch = menus_lunch, menusDinner = menus_dinner, ratingBreakfirst = rating_breakfirst, ratingLunch =rating_lunch,
    ratingDinner =rating_dinner, usersInfoBreakfirst = usersInfo_breakfirst, usersInfoLunch = usersInfo_lunch,
    usersInfoDinner = usersInfo_dinner)


