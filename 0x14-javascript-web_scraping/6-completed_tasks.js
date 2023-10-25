#!/usr/bin/node
// A script that computes the number of task completed

const urlEndpoint = process.argv[2];
const request = require('request');

request(urlEndpoint, (err, r, body) => {
        obj = JSON.parse(body);
        //console.log(obj);
        todo_dict = {};
        let count = 0;
        for (const attr of obj) {
                const id = attr.userId;
                //todo_dict[id] = id;
                if (!todo_dict[id]) {
                        todo_dict[id] = 0;
                }
                if (attr.completed === true) {
                        todo_dict[id]++;
                }
        }
        console.log(todo_dict);
});
