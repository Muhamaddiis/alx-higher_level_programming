#!/usr/bin/node
const fs = require('fs');
const filepath = process.argv[2];
const data = 'python is cool';
fs.writeFile(filepath, data, 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
  } else {
    console.log('file written successfully');
  }
});
