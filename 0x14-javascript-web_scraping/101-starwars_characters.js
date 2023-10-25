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

    const json_obj = JSON.parse(body);
    const character_list = json_obj.characters;

    function printCharacters(characters, index) {
        if (index >= characters.length) {
            return;
        }

        request(characters[index], (error, res, content) => {
            if (!error && res.statusCode === 200) {
                const char_obj = JSON.parse(content);
                console.log(char_obj.name);
                printCharacters(characters, index + 1);
            } else {
                console.error('Error fetching character details:', error);
            }
        });
    }

    printCharacters(character_list, 0);
});
