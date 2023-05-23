#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];// Read the URL from the  command line arguments
const filePath = process.argv[3];// Read the file path from the command line

request.get(url, { encoding: 'utf-8' }, (err, response, body) => {
  if (err) {
    console.error(err);// Print the error object if an error occured during the request
  } else {
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);// Print the error object if an error occured while writing to the file
      }
    });
  }
});
