#!/usr/bin/node
const rq = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
if (url) {
  rq(url, (error, response, body) => {
    if (error) {
      console.log(error);
    }
    console.log(JSON.parse(response.body).title);
  });
}
