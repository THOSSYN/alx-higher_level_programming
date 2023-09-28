#!/bin/bash
# A scripts that shows all the methods a web accepts
curl -sI -X OPTIONS http://example.com/ | grep -i Allow | awk '{print substr($0,8)}' 
