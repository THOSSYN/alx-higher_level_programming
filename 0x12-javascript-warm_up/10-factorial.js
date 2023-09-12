#!/usr/bin/node
const arg = parseInt(process.argv[2]);

function factorial(arg) {
  if (arg === 0) {
    return 1;
  } else if (isNaN(arg)) {
    return 1;
  } else {
    return arg * factorial(arg - 1);
  }
}

const res = factorial(arg);
console.log(res);
