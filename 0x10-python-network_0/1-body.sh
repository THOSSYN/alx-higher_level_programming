#!/bin/bash
# A bash script that display the body of a response
if [ "$(curl -s -o /dev/null '%{http_status}' "$1")" -eq 200 ]; then curl "$1"; fi
