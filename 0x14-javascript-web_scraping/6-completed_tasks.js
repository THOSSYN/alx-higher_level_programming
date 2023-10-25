#!/usr/bin/node
// A script that computes the number of task completed

const urlEndpoint = process.argv[2];
const request = require('request');

request(urlEndpoint, (err, r, body) => {
  if (!err && r.statusCode === 200) {
    const obj = JSON.parse(body);
    const todoDict = {};
    for (const attr of obj) {
      const id = attr.userId;
      if (!todoDict[id]) {
        todoDict[id] = 0;
      }
      if (attr.completed === true) {
        todoDict[id]++;
      }
    }
    console.log(todoDict);
  } else {
    console.error(err);
  }
});
