#!/usr/bin/node
const listData = require('./100-data');

const NewList = listData.list.map((num, index) => {
  return num * index;
});

console.log(listData.list);
console.log(NewList);
