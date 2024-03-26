#!/usr/bin/node
const rq = require('request');

const url = process.argv[2];
if (url) {
  rq(url, (error, response, body) => {
    if (error) {
      console.log(error);
    }
    console.log(`code: ${response.statusCode}`);
  });
}
