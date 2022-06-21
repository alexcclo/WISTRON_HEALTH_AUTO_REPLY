import datetime
import logging
import requests
import datetime

import azure.functions as func

user_data = user_data = [
    {
        "id": "10902038",
        "name": "羅哲琛",
        "mail": "Alex_Lo@wistron.com",
        "come_way": ["5","2","2","2","2","2","5"]
    },
    {
        "id": "10807058",
        "name": "周昊勳",
        "mail": "Howard_Chou@wistron.com",
        "come_way": ["5","1","1","1","1","1","5"]
    },
    {
        "id": "11009848",
        "name": "林聖斌",
        "mail": "Jason_Lin@wistron.com",
        "come_way": ["5","2","2","2","2","2","5"]
    },
    # {
    #     "id": "11009083",
    #     "name": "邱寶萱",
    #     "mail": "Rena_Chiu@wistron.com",
    #     "come_way": ["5","2","2","2","2","2","5"]
    # },
    {
        "id": "10907042",
        "name": "王伯文",
        "mail": "Ron_Wang@wistron.com",
        "come_way": ["5","1","1","1","1","1","5"]
    },
    {
        "id": "10807055",
        "name": "王柏鈞",
        "mail": "Royce_Wang@wistron.com",
        "come_way": ["5","3","3","3","3","3","5"]
    },
    {
        "id": "11001065",
        "name": "吳品燁",
        "mail": "Ray_PY_Wu@wistron.com",
        "come_way": ["5","5","5","5","5","1","5"]
    },
    {
        "id": "11103806",
        "name": "林健合",
        "mail": "Parts_Lin@wistron.com",
        "come_way": ["5","3","3","3","3","3","5"]
    },
    {
        "id": "11102034",
        "name": "劉建廷",
        "mail": "Tim_Liou@wistron.com",
        "come_way": ["5","3","3","3","3","3","5"]
    },
    {
        "id": "11102826",
        "name": "蕭正洺",
        "mail": "Jacky_Hsiao@wistron.com",
        "come_way": ["5","2","2","2","2","2","5"]
    }
    
]

data = {
    "bformdata": "1",
    "email": "Alex_Lo@wistron.com",
    "site": "WHC",
    "empname": "羅哲琛",
    "survey": "0",
    "empid": "10902038",
    "eventid": "1",
    "measure_date": "2022/5/18",
    "symptom": "1",
    "vaccine_date":"",
    "vaccine_brand": "0",
    "commute_way": "1",
    "is_confirmed": "1",
    "tour": "1",
    "spot": "0",
    "homedate":"", 
    "trip": "1",
    "area": "0",
    "backdate": "",
    "travel": "1",
    "country": "3",
    "countryname": "",
    "region": "",
    "finishdate": "",
    "notice": "1",
    "isolate_way": "0",
    "isolate_reason": "0",
    "startdate": "",
    "enddate": "",
    "notice_home": "1",
    "isolate_way_home": "0",
    "isolate_reason_home": "0",
    "startdate_home": "0",
    "enddate_home": "0",
    "family": "0",
    "relation1": "0",
    "country1": "0",
    "city1": "0",
    "backdate1": "2020/1/1",
    "backdate2": "2020/1/1",
    "backdate3": "2020/1/1",
    "bevent": "0"
}

wfh = ["2022/05/19","2022/05/20","2022/05/26","2022/05/27","2022/05/28","2022/05/29","2022/05/30","2022/05/31","2022/06/01","2022/06/09","2022/06/10","2022/06/11","2022/06/12","2022/06/13","2022/06/14","2022/06/15"]

def health_auto_sign(payload):
    session = requests.Session()
    session.post('https://familyweb.wistron.com/whrs/login_act.aspx',data={'userpass': payload["empid"]})
    url = 'https://familyweb.wistron.com/whrs/temperature_addnew_act.aspx'
    data = payload
    r = requests.post(url, data=data,cookies=session.cookies)
    logging.info(r.text)

def run_auto_sign():
    for i in user_data:
        date = datetime.datetime.today().strftime("%Y/%m/%d")
        week = int(datetime.datetime.today().strftime("%w"))
        data["email"] = i["mail"]
        data["empname"] = i["name"]
        data["empid"] = i["id"]
        data["commute_way"] = i["come_way"][week]
        data["measure_date"] = date
        if(date in wfh and i["name"] == "邱寶萱"):
            data["commute_way"] = '5'
        health_auto_sign(data)

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    run_auto_sign()
    logging.info('Python timer trigger function ran at %s', utc_timestamp)
