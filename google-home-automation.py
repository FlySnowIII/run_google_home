# coding=utf-8
import os
import time
import requests
import pygame.mixer

def isInternetConncect():
    try:
        page = requests.get('https://www.google.co.jp').status_code
        return True

    except:
        return False

def playSuccessMp3():
    # mixerモジュールの初期化
    pygame.mixer.init()
    # 音楽ファイルの読み込み
    pygame.mixer.music.load("/home/pi/Documents/run_google_home/googlehomerun.mp3")
    # 音楽再生、および再生回数の設定(-1はループ再生)
    pygame.mixer.music.play(1)

    time.sleep(7)
    # 再生の終了
    pygame.mixer.music.stop()

def writeLog():
    f = open("/home/pi/Documents/run_google_home/log.log","a")
    localtime = time.asctime(time.localtime(time.time()))
    strLog = "---Start at:"+localtime+"------------\r\n"
    f.write(strLog)
    f.close()

while (isInternetConncect() == False):
    print("Error")
    time.sleep(5)
else:
    print("OK,Google Assistan Demo is Running...")
    writeLog()
    playSuccessMp3()
    os.system("google-assistant-demo")


# from gtts import gTTS
# tts = gTTS(text='Google Home is going on. Say Ok google to try it.'.decode('utf-8'), lang='en', slow=False)
# tts.save("googlehomerun.mp3")

print("Over")