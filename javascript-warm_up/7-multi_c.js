#!/usr/bin/node
// script that prints "n" times "C is fun".

const text = 'C is fun';

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log(text);
  }
}
