#!/usr/bin/node
const arg = process.argv;
function fact (n) {
  if (n === 1 || isNaN(n)) {
    return (1);
  }
  return n * fact(n - 1);
}

const factorial = fact(parseInt(arg[2]));
console.log(factorial);
