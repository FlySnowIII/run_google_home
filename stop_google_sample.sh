ps -ef |grep "google-home-automation" | grep -v grep | awk '{print $2}'|xargs kill -9
ps -ef |grep "google-assistant-demo"  | grep -v grep | awk '{print $2}'|xargs kill -9
echo "Message:Google Assistant Demo is closed!"