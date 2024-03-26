#!/usr/bin/node
const fs = require('node:fs');

const path = process.argv[2];
if (path) {
  fs.readFile(path, 'utf8', (error, data) => {
    if (error) {
      console.log(error);
      return;
    }
    console.log(data);
  });
}
