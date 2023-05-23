#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, { json: true }, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }

  const taskComplete = body.reduce((acc, todo) => {
    if (todo.completed) {
      acc[todo.userId] = (acc[todo.userId] || 0) + 1;
    }
    return acc;
  }, {});

  console.log(taskComplete);
});
