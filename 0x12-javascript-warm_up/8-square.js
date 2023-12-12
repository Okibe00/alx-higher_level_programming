#!/usr/bin/node
const args = process.argv;
const size = parseInt(args[2]);
let str = '';
if (!size) {
  console.log('Missing size');
} else {
  for (let j = 0; j < size; j++) {
    str += 'X';
  }
  for (let i = 0; i < size; i++) {
    console.log(str);
  }
}
