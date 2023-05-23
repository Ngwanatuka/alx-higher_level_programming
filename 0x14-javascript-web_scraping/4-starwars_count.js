#!/usr/bin/node

const request = require('request');
const id = '18';
const url = process.argv[2];
let count = 0;

request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    data.results.forEach(function (film) {
      film.characters.forEach(function (character) {
        if (character.includes(id)) {
          count += 1;
        }
      });
    });

    console.log(count);
  }
});
