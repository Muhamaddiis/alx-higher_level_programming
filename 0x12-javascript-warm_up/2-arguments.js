let args = procces.argv;

if (args.length === 0) {
    console.log('No argument');
} else if (args.length === 1) {
    console.log("Argument found");
} else {
    console.log("Arguments found");
}