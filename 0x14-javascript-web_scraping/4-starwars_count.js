#!/usr/bin/node
// a script that prints the number of movies where the character "Wedge Antilles" is present

const request = require('request');
const url = process.argv[2];
let count = 0;

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const data = JSON.parse(body);
  count = data.results.filter(film => film.characters.some(char => char.includes('18'))).length;
  console.log(count);
});
