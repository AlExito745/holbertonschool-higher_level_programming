#!/usr/bin/node
/* script that prints the title of a Star Wars movie
where the episode number matches a given integer. */

const movID = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movID;
const req = require('request');
req(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
