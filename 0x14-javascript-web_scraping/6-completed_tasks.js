#!/usr/bin/node
// a script that computes the number of tasks completed by user id

const request = require('request');

const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Request failed with status code ${response.statusCode}`);
    return;
  }

  const todos = JSON.parse(body);

  const completedByUser = {};

  todos.forEach(todo => {
    if (todo.completed) {
      if (completedByUser[todo.userId]) {
        completedByUser[todo.userId]++;
      } else {
        completedByUser[todo.userId] = 1;
      }
    }
  });

  const output = JSON.stringify(completedByUser, null, 2);
  console.log(output);
});
