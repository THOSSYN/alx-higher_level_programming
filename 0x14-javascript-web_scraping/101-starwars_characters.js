#!/usr/bin/node
// A script that prints all characters of a Star Wars movie

const id = process.argv[2];
const urlEndpoint = `https://swapi-api.alx-tools.com/api/films/${id}/`;
const request = require('request');

request(urlEndpoint, (err, r, body) => {
  if (err) {
    console.error('Error:', err);
    return;
  }

  const jsonObj = JSON.parse(body);
  const characterList = jsonObj.characters;

  function printCharacters (characters, index) {
    if (index >= characters.length) {
      return;
    }

    request(characters[index], (error, res, content) => {
      if (!error && res.statusCode === 200) {
        const charObj = JSON.parse(content);
        console.log(charObj.name);
        printCharacters(characters, index + 1);
      } else {
        console.error('Error fetching character details:', error);
      }
    });
  }

  printCharacters(characterList, 0);
});
