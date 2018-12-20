import random
phonebook = {
    "치킨집" : "02:000-0000",
    "피자집" : "062-123-4567"
}
# print(phonebook["치킨집"])

izone = {"장원영" : 15 , "미야와키 사쿠라" : 21, "조유리" : 18,
"최예나" : 20, "안유진" : 16, "야부키 나코":18, "권은비":24,
"강혜원":20, "혼다 히토미":18, "김채원":19, "김민주":18, "이채연":19
}

bts = {
    "RM":20,
    "슈가":21,
    "진":22,
    "제이홉":23
}


idol ={
    "izone":izone,
    "bts":bts
}

# print(idol)
# print(idol["izone"]["장원영"])

score = {
    "수학":50,
    "국어":70,
    "영어":100
}
for key, value in score.items():
    pass
    # print(key)
    # print(value)

for key in score.keys():
    pass
    # print(key)

score_sum = 0
for value in score.values():
    score_sum = score_sum + value

# print(score_sum/len(score))



ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scrapying": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "gj1":  {
            "lecturer": "ChangE",
            "manager": "pro1",
            "class president": "서희수",
            "groups": {
                "두드림": ["구종민", "김녹형", "윤은솔", "이준원", "이창훈"],
                "런치타임": ["문영국", "박나원","박희승", "서희수", "황인식"],
                "Friday": ["강민지", "박현진", "서상준", "안현상", "최진호"],
                "TMM": ["김훈", "송건희", "이지선", "정태준", "조호근"],
                "살핌": ["문동식", "이중봉", "이지희", "차상권", "최보균"]
            }
        },
        "gj2": {
            "lecturer": "teacher2",
            "manager": "pro2"
        },
        "gj3": {
            "lecturer": "teacher3",
            "manager": "pro3"
        }
    }
}

print(len(ssafy["location"]))
# 1. ssafy를 진행하는 지역(location)은 몇개 인가요?

if ssafy["language"]["python"]["python standard library"] == "requests" :
    print("T")
else :
    print("F")
# 2. python standard library 'requests'가 있나요??

print(ssafy["classes"]["gj1"]["class president"])
# 3. gj1반의 반장의 이름을 출력하세요

for key in ssafy["language"].keys():
    print(key)
# 4. ssafy에서 배우는 언어들을 출력하세요 : dictionary.keys활용

for value in ssafy["classes"]["gj2"].values():
    print(value)
# 5. ssafy gj2의 강사와 매니저의 이름을 출력하세요
    # 예시) teacher2
    #       pro2

for key, value in ssafy["language"]["python"]["frameworks"].items():
    print(key,"는", value,"이다")
# 6. framework들의 이름과 설명을 다음과 같이 출력하세요
    # 예시)
    # flask는 micro이다.
    # django는 full-functioning이다.


print("오늘 당번은", random.choice(ssafy["classes"]["gj1"]["groups"]["살핌"]),"입니다")
# 7. 오늘 당번을 뽑기 위해 '살핌'조원중 1명을 랜덤으로 뽑아주세요
    # 예시)
    # 오늘 당번은 문동식입니다.
