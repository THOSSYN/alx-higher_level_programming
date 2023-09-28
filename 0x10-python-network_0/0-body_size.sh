#!/bin/bash
# A bash script that displays the header Content-Length
curl "$1" -sI | grep -i 'Content-Length' | awk '{print $2}'
