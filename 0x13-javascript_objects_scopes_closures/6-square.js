#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }
  
  charPrint(char) {
    if (char === undefined) {
      char = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      let row = '';
      for (let j = 0; j < this.size; j++) {
        row += char;
      }
      console.log(row);
    }
  }
}
module.exports = Square;
