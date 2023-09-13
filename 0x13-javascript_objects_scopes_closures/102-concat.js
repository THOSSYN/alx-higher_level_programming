#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 5) {
  console.log('Insufficient argument');
  process.exit(1);
}

const sourceFilePath1 = process.argv[2];
const sourceFilePath2 = process.argv[3];
const destinFilePath = process.argv[4];

fs.readFile(sourceFilePath1, 'utf8', (err, data1) => {
  if (err) {
    console.log(`Error src file 1: ${err}`);
    process.exit(1);
  }
  fs.readFile(sourceFilePath2, 'utf8', (err, data2) => {
    if (err) {
      console.log(`Error src file 2: ${err}`);
      process.exit(1);
    }
    const AllContent = data1 + data2;

    fs.writeFile(destinFilePath, AllContent, 'utf8', (err) => {
      if (err) {
        console.log(`Error writing to dest file: ${err}`);
        process.exit(1);
      }
    });
  });
});
