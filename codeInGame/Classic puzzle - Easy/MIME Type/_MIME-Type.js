/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

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

    let match = FNAME.match(/\.[a-z]+/g);
    match = match ? match[match.length - 1]
        .toLowerCase()
        .replace('.', '') : '';

    console.error('-match:', match);
    console.error('-FNAME:', FNAME);

    const EXT = match;
    if (obj.hasOwnProperty(EXT)) {
        console.log(obj[EXT]);
    } else console.log('UNKNOWN');
}

// Write an action using console.log()
// To debug: console.error('Debug messages...');


// For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
//console.log(inputs);