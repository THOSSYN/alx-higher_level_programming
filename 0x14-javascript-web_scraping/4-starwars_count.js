#!/usr/bin/node
// A script that prints movie IDs

const request = require('request');
const urlEndpoint = process.argv[2];

request(urlEndpoint, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const jsonObj = JSON.parse(body);
    const list = jsonObj.results;
    const listSize = jsonObj.results.length;
    let count = 0;
    const characterId = 'https://swapi-api.alx-tools.com/api/people/19/';
    for (let i = 0; i < listSize; i++) {
      if (list[i].characters.includes(characterId)) count++;
    }
    console.log(count);
  }
});
