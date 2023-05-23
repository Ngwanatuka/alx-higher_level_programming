#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];// Read the file path from the command line
const content = process.argv[3];// Read the string to write from the command line

fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);// Print the error object if an error occure while writing
  }
});
