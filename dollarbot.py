#임포트--------------------------------------
from bs4 import BeautifulSoup
import requests
import os

import telepot
#변수 선언--------------------------------------
url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%ED%99%98%EC%9C%A8'

#token = ""
token = '2133101939:AAHNkHF24eQbPnvTRKV26tQvkHs_Lk9DCWE'
mc = "1924408195"
bot = telepot.Bot(token)
is_send = 0
flag = 11600#1160
#구동부--------------------------------------


while 1:
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    wd_site = soup.select_one('#_cs_foreigninfo > div > div.api_cs_wrap > div > div.c_rate > div.rate_bx > div.rate_spot._rate_spot > div.rate_tlt > h3 > a > span.spt_con.dw > strong')
    wd_txt = wd_site.text.replace(",","")
    wd_float = float(wd_txt)
    wd = int(wd_float) # 실제 원달러 환율 값
        
    bot.sendMessage(mc,'test')
        

    if(wd<flag and is_send==0):
        #if(wd<=flag):
        
        saying = '환율이'+str(flag)+'이하로 떨어짐. 환전 기회'
        bot.sendMessage(mc,saying)
        is_send = 1



 