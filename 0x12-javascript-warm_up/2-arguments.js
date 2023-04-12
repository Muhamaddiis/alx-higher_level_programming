#!/usr/bin/node

let arg = procces.argv.slice(2);

if (arg.length === 0) {
    console.log('No argument');
} else if (arg.length === 1) {
    console.log("Argument found");
} else {
    console.log("Arguments found");
}