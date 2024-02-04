#!/bin/bash
# post json data to server 
curl -d --json "@$2" "$1" 
