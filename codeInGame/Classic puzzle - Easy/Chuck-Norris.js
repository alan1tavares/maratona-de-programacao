/*
Soulution
    Djoums 
*/

const input = 'CC';
let output = '';

console.error('Debug\n  ->C - ', 'C'.charCodeAt().toString(2));


output = input
    .split('')
    .map(c => '0'.concat(c.charCodeAt().toString(2)).slice(-7))
    .join('')
    .match(/(.)\1*/g)
    .map(c => (c['0'] == '1' ? '0 ' : '00 ') + '0'.repeat(c.length))
    .join(' ');
    
console.log('Input:\n', ' ->', input);
console.log('Output:\n', ' ->', output ? output : 'empty');