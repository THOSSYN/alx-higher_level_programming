#!/usr/bin/node
// A script that displays the status code of a request

const request = require('request');
const urlRequest = process.argv[2];

request(urlRequest, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  }
  console.log('code: ', response.statusCode);
});
