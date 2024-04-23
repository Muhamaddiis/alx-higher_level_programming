#!/usr/bin/node
const fs = require('fs');
if (process.argv.length < 3) {
  console.error('Please provide a file path as an argument.');
  process.exit(1);
}

// The file path is the third element in the process.argv array
const filePath = process.argv[2];
fs.readFile(filePath, 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
  } else {
    console.log(data);
  }
});
