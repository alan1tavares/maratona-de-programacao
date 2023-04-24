/**
 * LED
 * https://www.beecrowd.com.br/judge/pt/problems/view/1168
 */
using System;
using System.Linq;
using System.Collections.Generic;

int n  = int.Parse(Console.ReadLine());
List<List<int>> quadrado = new List<List<int>>();
Dictionary<int, List<int>> somaLinhas = new Dictionary<int, List<int>>();
for (int i = 0; i < n; i++)
{
    List<int> linha = Array.ConvertAll(Console.ReadLine().Split(), int.Parse).ToList();
    quadrado.Add(linha);
    int sum = linha.Sum();
    if (!somaLinhas.ContainsKey(sum))
    {
        somaLinhas.Add(sum, new List<int>());
    }
    somaLinhas[sum].Add(i);
}

int[] soma = somaLinhas.Keys.ToArray();
int indiceErrado = 0;
int somaQuadro = 0;

if (somaLinhas[soma[0]].Count == 1)
{
    somaQuadro = soma[1];
    indiceErrado = somaLinhas[soma[0]][0];
} else
{
    somaQuadro = soma[0];
    indiceErrado = somaLinhas[soma[1]][0];
}

for (int j = 0; j < n; j++)
{
    int sum = 0;
    int i = 0;
    for (i = 0; i < n; i++)
    {
        sum += quadrado[i][j];
    }
    if (somaQuadro != sum)
    {
        int numerTrocado = quadrado[indiceErrado][j];
        int numeroOriginal = numerTrocado + somaQuadro - sum;

        Console.WriteLine(numeroOriginal + " " + numerTrocado);
        break;
    }
}
