#!/usr/bin/node
const arg = process.argv;
function add (a, b) {
  console.log(parseInt(arg[2]) + parseInt(arg[3]));
}
add(arg[2], arg[3]);
