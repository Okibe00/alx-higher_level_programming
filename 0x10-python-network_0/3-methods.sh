#!/bin/bash
# display method options on server
curl -IsX OPTIONS "$1" | grep Allow | sed  "s/Allow: //"
