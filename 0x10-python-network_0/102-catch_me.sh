#!/bin/bash
# A script that cause the server to respond with "You got me"
curl -s 0.0.0.0:5000/catch_me -o response.txt

grep -o "You got me!" response.txt
rm -f response.txt
