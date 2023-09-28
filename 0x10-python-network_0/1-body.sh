#!/bin/bash
# A bash script that display the body of a response
if [ "$(curl -s -o /dev/null -w '{http_code}' "$1")" -eq 200 ]; then curl -s "$1"; fi
