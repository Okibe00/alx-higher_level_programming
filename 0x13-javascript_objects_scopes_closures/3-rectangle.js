#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return this;
    }
  }

  print () {
    let str = '';
    for (let i = 0; i < this.width; i++) {
      str += 'X';
    }

    for (let j = 0; j < this.height; j++) {
      console.log(str);
    }
  }
}
module.exports = Rectangle;
