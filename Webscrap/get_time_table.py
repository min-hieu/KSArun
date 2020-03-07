import requests
from bs4 import BeautifulSoup
import json

headers = {
    'user-agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}

with open('C://Users//hieut//OneDrive//Desktop//login.json', 'r') as f:
    loginForm = json.load(f)


with requests.Session() as s:
    url = "http://students.ksa.hs.kr/scmanager/stuweb/index.jsp"
    r = s.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
