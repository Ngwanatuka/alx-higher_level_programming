#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);// Print the error object if the error occure
  } else {
    console.log(data);// Print the content of the file
  }
});
