#!/usr/bin/node

const { dict } = require('./101-data');

// Initialize an empty object to store the new dictionary
const newDict = {};

// Loop through the keys and values of the original dictionary
for (const userId in dict) {
    const occurrences = dict[userId];

    // If the number of occurrences is not a key in the new dictionary, initialize it with an empty array
    if (!newDict[occurrences]) {
        newDict[occurrences] = [];
    }

    // Push the user ID to the list corresponding to the number of occurrences
    newDict[occurrences].push(userId);
}

// Print the new dictionary
console.log(newDict);
