#!/usr/bin/node
const square = require('./5-square');
class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      let str = '';
      for (let i = 0; i < this.width; i++) {
        str += c;
      }
      for (let j = 0; j < this.height; j++) {
        console.log(str);
      }
    } else {
      super.print();
    }
  }
}
module.exports = Square;
