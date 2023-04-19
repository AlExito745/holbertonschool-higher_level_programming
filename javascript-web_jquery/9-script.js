#!/usr/bin/node
/* script that fetches an URL and displays the value of hello 
from that fetch in the HTML tag DIV#hello. */

$.getJSON('https://stefanbohacek.com/hellosalut/?lang=fr', 
  function (data) {
    $('DIV#hello').append(data.hello);
});
