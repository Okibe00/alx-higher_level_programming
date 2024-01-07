#!/bin/bash
# add variable to request header
curl -s -H "X-School-User-Id: 98" "$1"
