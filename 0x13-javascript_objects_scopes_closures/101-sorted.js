#!/usr/bin/node
const data = require('./101-data');

const newDict = {};
const keys = Object.keys(data.dict);

for (const key of keys) {
  const frequency = data.dict[key];
  if (!newDict[frequency]) {
    newDict[frequency] = [];
  }
  newDict[frequency].push(key);
}

console.log(newDict);
