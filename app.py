from flask import Flask, render_template, request
import requests
import random
import json
from faker import Faker

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/lotto')
def lotto() :
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
    res = requests.get(url).text
    lotto_dict = json.loads(res)

    # print(lotto_dict["drwNoDate"]) #"drwNoDate" 변수를 가져옴
    # week_num = []
    week_format_num = []
    # drwtNo = ["drwtNo1","drwtNo2","drwtNo3","drwtNo4","drwtNo5","drwtNo6"]
    # for num in drwtNo :
    #     number = lotto_dict[num]
    #     week_num.append(number)
    #     #append : 붙여넣기
    #     print(week_num)

    BnusNo = set([lotto_dict["bnusNo"]])

    num_list = range(1,46)
    pick = random.sample(num_list,6)
    sort_pick = sorted(pick) # set을 사용하면 sort을 안해도 됨

    for i in range(1,7) :
        num = lotto_dict["drwtNo{}".format(i)]
        week_format_num.append(num)
        sort_week_format_num = sorted(week_format_num)

    # print(type(res))
    # print(type(json.loads(res)))

        s1 = set(sort_week_format_num)
        s2 = set(sort_pick)

        s3 = s1&s2
        s5 = s1&BnusNo
        s6 = len(s5)
        s4 = len(s3)

        if s4 == 6 :
                s5 = "1등 입니다!! 축하축하"
        elif s4 == 5 and s6 == 1:
            s5 = "2등 입니다!!"
        elif s4 == 5  and s6 == 0:
            s5 = "3등 입니다"
        elif s4 == 4 :
            s5 = "4등 입니다"
        elif s4 == 3 :
            s5 = "5등 입니다"
        else :
            s5 = "꽝 ㅠㅠ"

    return render_template("lotto.html",sort_lotto=sort_pick, sort_week_format_num=sort_week_format_num,s5=s5, BnusNo=BnusNo)


@app.route('/ping') #/은 우리 사이트의 루트url
def ping():
    return render_template("ping.html")




@app.route('/pong')
def pong():
    return render_template("pong.html", html_name=saju, fake_job=fake_job)