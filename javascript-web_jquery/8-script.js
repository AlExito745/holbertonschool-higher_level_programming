#!/usr/bin/node
// script that fetches and lists the title for all movies by using this URL.

$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json',
  function (data) {
    $.each(data.movies, function (index, movie) {
      $('UL#list_movies').append('<li>' + movie.title + '<li/>');
    });
  });
