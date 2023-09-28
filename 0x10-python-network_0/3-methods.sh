#!/bin/bash
# A scripts that shows all the methods a web accepts
curl -i -X OPTIONS http://example.com/ | grep -i Allow | cut -d ":" -f 2 
