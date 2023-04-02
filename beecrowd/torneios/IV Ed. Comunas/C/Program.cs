/**
 * Fila
 * https://www.beecrowd.com.br/judge/pt/problems/view/2460
 */
    using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
using System.Diagnostics;

var stopwatch = new Stopwatch();
stopwatch.Start();

Console.ReadLine();
string[] input = Console.ReadLine().Split();
Console.ReadLine();
string[] filaSaida = Console.ReadLine().Split();

HashSet<string> fila = new HashSet<string>(input);

fila.ExceptWith(filaSaida);

Console.WriteLine(string.Join(" ", fila));
stopwatch.Stop();
Console.WriteLine(stopwatch.Elapsed);