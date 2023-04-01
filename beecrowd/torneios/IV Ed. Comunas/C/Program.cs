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

Dictionary<string, int> elementosQueSairam = new Dictionary<string, int>(100000);
for (int i = 0; i < filaSaida.Length; i++)
{
    elementosQueSairam.Add(filaSaida[i], 1);
}

string saida = "";
for (int i = 0; i < input.Length; i++)
{
    if(!elementosQueSairam.ContainsKey(input[i]))
    {
        saida += input[i];
        if (i != input.Length - 1)
            saida += " ";     
    }
}


Console.WriteLine(saida);
stopwatch.Stop();
Console.WriteLine(stopwatch.Elapsed);