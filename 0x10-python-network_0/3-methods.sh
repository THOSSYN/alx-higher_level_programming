#!/bin/bash
# A scripts that shows all the methods a web accepts
curl -sI -X OPTIONS "$1" | grep -i Allow | awk '{print substr($0,8)}' 
