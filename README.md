# run_google_home
Auto run google-assistant-sample on Raspberry Pi 3 

0.下記のリンクに従い、音声起動できるGoogle Assistant DemoをRaspberry Piにインストールしてください。 

https://www.novaspirit.com/2017/05/23/voice-activated-google-assistant-raspberry-pi/  

1.当プロジェクトを/home/pi/Documentの下にCloneしてください。 

cd /home/pi/Documents  

git clone https://github.com/FlySnowIII/run_google_home.git 

2.ファイル「/home/pi/.bashrc」の最後に下記のソースコードを追加してください。 

bash /home/pi/Documents/run_google_home/start_google_sample.sh
