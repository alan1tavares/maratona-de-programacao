/**
 * Carteiro
 * https://www.beecrowd.com.br/judge/pt/problems/view/2448
*/
using System;
using System.Collections.Generic;

string quantidadeEntrada = Console.ReadLine();
string[] inputCasas = Console.ReadLine().Split();
string ondeOCarteiroEsta = inputCasas[0];
Dictionary<string, int> casas = new Dictionary<string, int>();

for (int i = 0; i < inputCasas.Length; i++)
    casas.Add(inputCasas[i], i + 1);

string[] mapaEntrega = Console.ReadLine().Split();
int passsos = 0;

for (int i = 0; i < mapaEntrega.Length; i++)
{
    passsos += Math.Abs(casas[mapaEntrega[i]] - casas[ondeOCarteiroEsta]);
    ondeOCarteiroEsta = mapaEntrega[i];    
}

Console.WriteLine(passsos);
