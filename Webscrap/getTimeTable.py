'''
encoding: UTF-8
title: getTimeTable
project: Data Structures
'''

import requests
import pandas as pd
from bs4 import BeautifulSoup
import json

def getTimeTableHTML():
    #request headers
    headerlogin = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Origin": "http://students.ksa.hs.kr",
        "Referer": "http://students.ksa.hs.kr/scmanager/stuweb/index.jsp",
        "Upgrade-Insecure-Requests": "1",
        "user-agent" : "Mozilla//5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
    }

    headermain = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Referer": "http://students.ksa.hs.kr/scmanager/stuweb/loginProc.jsp",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
    }

    headerclass = {
        "Referer": "http://students.ksa.hs.kr/scmanager/stuweb/main.jsp",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
    }

    #get login credential
    with open('C://Users//hieut//OneDrive//Desktop//login.json', 'r') as f:
        loginForm = json.load(f)

    URL = "http://students.ksa.hs.kr/"
    indexURL = "http://students.ksa.hs.kr/scmanager/stuweb/index.jsp"
    loginURL = "http://students.ksa.hs.kr/scmanager/stuweb/loginProc.jsp"
    mainURL = "http://students.ksa.hs.kr/scmanager/stuweb/kor/main.jsp"
    classURL = "http://students.ksa.hs.kr/scmanager/stuweb/kor/sukang/state.jsp"

    # request for the timetable page
    try:
        with requests.Session() as s:

            s.get(indexURL)
            s.post(loginURL, headers=headerlogin, data=loginForm)
            s.get(mainURL, headers=headermain)
            r = s.get(classURL, headers=headerclass)

            return r

    except Exception as e:
        print("failed /n" + str(e))
        return None


def convertDataFrame(htmlbin):
    # extract the dataframe timetable from the page
    soup = BeautifulSoup(htmlbin.content, 'lxml')
    table = soup.find('table', {"width": "100%", "class": "board_view"})
    trList = table.find_all('tr')

    l = []
    for tr in trList:
        td = tr.find_all('td')
        row = [tr.text for tr in td]
        l.append(row)

    df = pd.DataFrame(l, columns = [1,2,3,4,5,6])

    return df

    # turn dataframe into excel file
    # df.to_excel(r'.//test.xlsx')


