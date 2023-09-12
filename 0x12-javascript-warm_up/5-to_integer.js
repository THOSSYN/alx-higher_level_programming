#!/usr/bin/node
const args = process.argv[2];
const convArg = parseInt(args);

if (!isNaN(convArg)) {
  console.log(`My number: ${convArg}`);
} else {
  console.log('Not a number');
}
