#!/usr/bin/node
// a script that gets the contents of a webpage and stores in a file

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filepath = process.argv[3];

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  fs.writeFile(filepath, body, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
