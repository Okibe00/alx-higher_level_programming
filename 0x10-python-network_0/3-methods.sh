#!/bin/bash
# display method options on server
curl -IsX OPTIONS "$1" | grep Allow | cut -f 2 -d ":"
