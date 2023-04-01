/**
 * Fila
 * https://www.beecrowd.com.br/judge/pt/problems/view/2460
 */
using System.Collections.Generic;
using System.Linq;

Console.ReadLine();
string[] input = Console.ReadLine().Split(' ');
HashSet<string> fila = new HashSet<string>(input);
Console.ReadLine();
fila.ExceptWith(Console.ReadLine().Split(' '));
string saida = "";
foreach (string item in fila)
{
    saida += item + " ";
}
Console.WriteLine(saida.Remove(saida.Length-1));

