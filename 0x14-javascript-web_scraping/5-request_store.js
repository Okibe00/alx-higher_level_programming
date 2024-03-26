#!/usr/bin/node
const fs = require('node:fs');
const rq = require('request');
const url = process.argv[2];
const filePath = process.argv[3];
if (url) {
  rq(url, (error, response, body) => {
    if (error) {
      console.log(error);
    }
    if (body) {
      fs.writeFile(filePath, body, 'utf8', (error, data) => {
        if (error) {
          console.log(error);
        }
      });
    }
    // console.log(data);
    /*      fs.writeFile(filePath, data, 'utf8', (error, data) => {
        if (error) {
          console.log(error);
        }
      }); */
  });
}
