#!/usr/bin/node
// A script that prints all characters of a star wars

const id = process.argv[2];
const urlEndpoint = `https://swapi-api.alx-tools.com/api/films/${id}/`;
const request = require('request');

request(urlEndpoint, (err, r, body) => {
  if (!err && r.statusCode === 200) {
    const jsonObj = JSON.parse(body);
    const characterList = jsonObj.characters;

    for (const character of characterList) {
      request(character, (error, res, content) => {
        if (!error && res.statusCode === 200) {
          const charObj = JSON.parse(content);
          console.log(charObj.name);
        } else {
          console.error(error);
        }
      });
    }
  } else {
    console.error(err);
  }
});
