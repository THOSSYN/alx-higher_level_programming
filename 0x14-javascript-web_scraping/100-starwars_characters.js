#!/usr/bin/node
// A script that prints all characters of a star wars

const id = process.argv[2];
const urlEndpoint = `https://swapi-api.alx-tools.com/api/films/${id}/`;
const request = require('request');

request(urlEndpoint, (err, r, body) => {
        const json_obj = JSON.parse(body);
        const character_list = json_obj.characters

        for (const character of character_list) {
                request(character, (error, res, content) => {
                        const char_obj = JSON.parse(content);
                        console.log(char_obj.name);
                });
        }
});
