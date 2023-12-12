#!/usr/bin/node
const argv = process.argv;
const firstArg = parseInt(argv[2]);
if (!firstArg) {
  console.log('Not a number');
} else {
  console.log('My number: ' + firstArg);
}
