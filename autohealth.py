import requests
import datetime
def health_auto_sign():
    date = datetime.datetime.today().strftime("%Y/%m/%d")
    number = ["10807058","10902038","11009848","11009083","10907042","10807055","11001065","11103806"]
    name = ["周昊勳","羅哲琛","林聖斌","邱寶萱","王伯文","王柏鈞","吳品燁","林健合"]
    mail = ["Howard_Chou@wistron.com","Alex_Lo@wistron.com","Jason_Lin@wistron.com","Rena_Chiu@wistron.com","Ron_Wang@wistron.com","Royce_Wang@wistron.com","Ray_PY_Wu@wistron.com","Parts_Lin@wistron.com"]
    comway = ["1","1","2","2","1","1","1","3"]
    #print(date)
    for i in range(len(number)):
        session = requests.Session()
        session.post('https://familyweb.wistron.com/whrs/login_act.aspx',data={'userpass': number[i]})
        #print(session.cookies)
        url = 'https://familyweb.wistron.com/whrs/temperature_addnew_act.aspx'
        data = {
        "email": [mail[i]],
        "site": "WHC",
        "empname": name[i],
        "survey": "0",
        "empid": number[i],
        "eventid": "1",
        "measure_date": date,
        "symptom": "1",
        "vaccine_date": "",
        "vaccine_brand": "0",
        "commute_way": comway[i],
        "tour": "0",
        "spot": "0",
        "homedate": "",
        "trip": "0",
        "area": "0",
        "backdate": "",
        "travel": "1",
        "country": "3",
        "countryname": "",
        "region": "",
        "finishdate": "",
        "notice": "1",
        "notice_home": "1",
        "family": "2",
        "relation1": "",
        "country1": "",
        "city1": "",
        "backdate1": "2020/1/1",
        "backdate2": "2020/1/1",
        "backdate3": "2020/1/1",
        "bevent": "0",
        }
        r = requests.post(url, data=data,cookies=session.cookies)
        #print(r.text)
health_auto_sign()