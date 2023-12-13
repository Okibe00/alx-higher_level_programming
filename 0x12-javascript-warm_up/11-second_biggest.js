#!/usr/bin/node
const arg = process.argv;

function sBiggest (arr) {
  const len = arr.length;
  let b, s;
  if (len === 2 || len === 3) {
    console.log(0);
    return;
  }
  b = parseInt(arr[2]);
  for (let i = 2; i < len; i++) {
    if (parseInt(arr[i]) > b) {
      b = parseInt(arr[i]);
    }
  }
  s = 0;
  for (let i = 2; i < len; i++) {
    if (parseInt(arr[i]) !== b && parseInt(arr[i]) > s) {
      s = parseInt(arr[i]);
    }
  }
  console.log(s);
}
sBiggest(arg);
