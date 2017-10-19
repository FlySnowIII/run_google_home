#!/bin/bash

#ps -ef |grep "google-home-automation" | grep -v grep | awk '{print $2}'|xargs kill -9
#ps -ef |grep "google-assistant-demo"  | grep -v grep | awk '{print $2}'|xargs kill -9

function runGoogleAssistant(){
        cd /home/pi
        source /home/pi/env/bin/activate
        python ~/Documents/run_google_home/google-home-automation.py &
}

appname="google-assistant-demo"
pid=`ps -ef|grep $appname |grep -v grep|wc -l`

#echo $pid

#$pid<=0
if [ $pid -le 0 ]
then
        runGoogleAssistant
        echo "Message: Run Google Assistant Demo..."
else
        echo "Warning: Google Assistant Demo is running!"
fi

exit 0