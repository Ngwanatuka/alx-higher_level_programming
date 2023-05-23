#!/usr/bin/node

const request = require('request');

const url = process.argv[2];// Read the URl from the command line arguments

request.get(url, (err, response) => {
  if (err) {
    console.error(err);// Print the error object if an error occured during the request
  } else {
    console.log('code:', response.statusCode);// Print the status code
  }
});
