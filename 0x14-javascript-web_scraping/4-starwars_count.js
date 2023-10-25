#!/usr/bin/node
// A script that prints movie IDs

const request = require('request');
const urlEndpoint = process.argv[2];

request(urlEndpoint, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const jsonObj = JSON.parse(body);
    const charactersUrl = jsonObj.results[0].characters[15];

    request(charactersUrl, function (err, r, body) {
      if (!err && r.statusCode === 200) {
        const charactersObj = JSON.parse(body);
        const movieList = charactersObj.films;
        const count = movieList.length;

        let i = 0;
        while (i < count) {
          i++;
        }
        console.log(i);
      } else {
        console.error('Error fetching character details:', err);
      }
    });
  } else {
    console.error('Error fetching film details:', error);
  }
});
