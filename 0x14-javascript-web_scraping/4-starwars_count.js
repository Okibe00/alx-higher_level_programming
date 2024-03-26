#!/usr/bin/node
const rq = require('request');

const url = process.argv[2];
if (url) {
  rq(url, (error, response, body) => {
    if (error) {
      console.log(error);
    }

    let count = 0;
    const res = JSON.parse(response.body);
    const resArr = res.results;
    resArr.forEach(obj => {
      if (obj.characters.indexOf('https://swapi-api.alx-tools.com/api/people/18/') > -1) {
        count += 1;
      }
    });
    console.log(count);
  });
}
