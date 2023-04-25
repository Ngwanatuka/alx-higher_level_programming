#!/usr/bin/node
// a scipt that reads of a file and prints it to the console

const fs = require('fs');

const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  console.log(data);
});
