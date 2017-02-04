#find any running process and kill
pid=`ps -ef | grep "/usr/bin/python app.py" | head -1 | awk {'print $2'}`
kill -9 $pid
sleep 5
#start up flask
/usr/bin/python app.py 
