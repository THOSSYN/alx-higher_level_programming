#!/bin/bash
# A script that sends a POST request with a json file
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
