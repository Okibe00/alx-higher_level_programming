#!/usr/bin/node
const fs = require('node:fs');

const path = process.argv[2];
const text = process.argv[3];
if (path) {
  fs.writeFile(path, text, 'utf8', (error, data) => {
    if (error) {
      console.log(error);
    }
  });
}
