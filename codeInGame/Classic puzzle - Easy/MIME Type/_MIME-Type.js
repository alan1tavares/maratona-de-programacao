/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
const { EOL } = require('os');

let input = '';
let lines = [];
const readline = function () {
    return lines.shift();
}

process.stdin.on('data', c => input += c);
process.stdin.on('end', () => {
    lines = input.split(EOL);

    const N = parseInt(readline()); // Number of elements which make up the association table.
    const Q = parseInt(readline()); // Number Q of file names to be analyzed.
    const obj = {};

    for (let i = 0; i < N; i++) {
        var inputs = readline().split(' ');
        const EXT = inputs[0].toLowerCase(); // file extension
        const MT = inputs[1]; // MIME type.

        obj[EXT] = MT;
    }
    for (let i = 0; i < Q; i++) {
        const FNAME = readline().toLowerCase(); // One file name per line.

        // let match = FNAME.match(/\.([a-z]|[0-9])+/g);
        let match = FNAME.split('.');
        match = match.length > 1 ? match[match.length - 1]
            .toLowerCase() : '';
            // .slice(1) : '';

        const EXT = match;
        if (obj.hasOwnProperty(EXT)) {
            console.log(obj[EXT]);
        } else console.log('UNKNOWN');
    }

});
// Write an action using console.log()
// To debug: console.error('Debug messages...');


// For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
//console.log(inputs);