#!/bin/bash
# A bash script that display the body of a response
url="$1"; response=$(curl -s -o /dev/null -w "%{http_code}" "$url"); [ "$response" -eq 200 ] && curl -s "$url"
