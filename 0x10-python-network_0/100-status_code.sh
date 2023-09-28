#!/bin/bash
# A script that sends a request and receives only the status code
curl -s "$1" -o /dev/null -w '%{http_code}'
