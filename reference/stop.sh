#!/bin/bash
#find any running process and kill
pid=`ps -ef | grep "/usr/bin/python restful.py" | head -1 | awk {'print $2'}`
kill -9 $pid
