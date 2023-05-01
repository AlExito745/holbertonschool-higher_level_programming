#!/usr/bin/node
// script that computes the number of tasks completed by user id.

const url = process.argv[2];
const file = process.argv[3];
const req = require('request');
const fs = require('fs');
req(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(file, body, 'utf-8', (error) => {
      if (error) console.log(error);
    });
  }
});
