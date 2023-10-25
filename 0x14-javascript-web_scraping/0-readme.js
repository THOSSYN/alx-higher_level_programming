#!/usr/bin/node
// A script that reads from a file

const fs = require('fs');
const filepath = process.argv[2];

fs.readFile(filepath, 'utf8', (err, data) => {
        if (err) {
                console.error(err);
                return;
        }
        console.log(data);
});
