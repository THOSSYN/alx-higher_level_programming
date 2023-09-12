#!/usr/bin/node
const args = process.argv[2];
const convArgs = parseInt(args);

if (!isNaN(convArgs)) {
  for (let i = 0; i < convArgs; i++) {
    let row = '';
    for (let j = 0; j < convArgs; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
