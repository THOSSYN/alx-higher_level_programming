#!/bin/bash
# A script that sends a POST request with parameters
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
