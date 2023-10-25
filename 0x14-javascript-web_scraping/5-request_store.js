#!/usr/bin/node
// A script that stores response in a file

const urlEndpoint = process.argv[2];
const filePath = process.argv[3];
const fs = require('fs');
const request = require('request');

request(urlEndpoint, function (err, r, body) {
  if (!err && r.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf8', (error) => {
      if (error) {
        console.error(error);
      }
    });
  } else {
    console.error(err);
  }
});
