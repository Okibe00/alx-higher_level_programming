#!/bin/bash
# post json data to server 
curl --json @"$2" "$1" 
