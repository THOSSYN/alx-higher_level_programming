#!/usr/bin/node
// A script that prints the title of a movie

const request = require('request');
const filmId = process.argv[2];
const requestUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

request(requestUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const jsonObj = JSON.parse(body);
    console.log(jsonObj.title);
  }
});
