/**
 * Fila
 * https://www.beecrowd.com.br/judge/pt/problems/view/2460
 */
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

Console.ReadLine();
string[] input = Console.ReadLine().Split(' ');
Console.ReadLine();
string[] filaSaida = Console.ReadLine().Split(' ');

Dictionary<int, int> elementosQueSairam = new Dictionary<int, int>(100000);
for (int i = 0; i < filaSaida.Length; i++)
{
    elementosQueSairam.Add(Convert.ToInt32(filaSaida[i]), 1);
}

string saida = "";
for (int i = 0; i < input.Length; i++)
{
    if(!elementosQueSairam.ContainsKey(Convert.ToInt32(input[i])))
    {
        saida += input[i];
        if (i != input.Length - 1)
            saida += " ";     
    }
}

Console.WriteLine(saida);

