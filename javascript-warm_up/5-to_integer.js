#!/usr/bin/node
// script that converted to an integer the first argument.

if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(process.argv[2]));
}
