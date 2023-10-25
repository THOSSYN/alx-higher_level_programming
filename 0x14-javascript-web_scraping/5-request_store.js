#!/usr/bin/node
// A script that stores response in a file

const urlEndpoint = process.argv[2];
const filePath = process.argv[3];
const fs = require('fs');
const request = require('request');

request(urlEndpoint, function (err, r, body) {
        fs.writeFile(filePath, body, 'utf8', (err) => {
                if (err) {
                        console.error(err);
                }
        });
});
