#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
    console.log("Usage: ./102-concat.js <file1> <file2> <destination>");
    process.exit(1);
}

const [, , file1, file2, destination] = process.argv;

const content1 = fs.readFileSync(file1, 'utf8');
const content2 = fs.readFileSync(file2, 'utf8');

const concatenatedContent = content1 + content2;

fs.writeFileSync(destination, concatenatedContent);

console.log(`Files ${file1} and ${file2} concatenated to ${destination}`);
