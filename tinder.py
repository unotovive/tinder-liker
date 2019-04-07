import os
import time
import random
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
I=1
chro = webdriver.Chrome('./chromedriver')

#Tinder.comに飛ぶ
#loginは手動
chro.get("https://tinder.com/app/login")
#Tinder.comに手動でログインしたら、yキーを押して自動プログラム開始
#1秒ごとに、右キー（いいね）を入力、30000人まで行ったら、終了
key = input('Tinderのトップページが出たらyを押してください')
if key == "y":
    while I < 30000:
        I=I+1
        chro.find_element_by_tag_name("body").send_keys(Keys.RIGHT)
        time.sleep(1)
        print(I)
    else:
        print("30000人にいいねを付けました")
        chro.close()