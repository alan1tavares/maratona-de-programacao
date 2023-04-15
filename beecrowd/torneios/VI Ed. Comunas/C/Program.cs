/**
 * Fechadura
 * https://www.beecrowd.com.br/judge/pt/problems/view/2449
*/
using System;

int solucao = int.Parse(Console.ReadLine().Split()[1]);
int[] pinos = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
int quantidadeMovimentos = 0;

for (int i = 0; i < pinos.Length; i++)
{
    if (pinos[i] == solucao)
        continue;
    if (pinos[i] > solucao)
    {
        int diferenca = pinos[i] - solucao;
        pinos[i+1] -= diferenca;
        quantidadeMovimentos += diferenca;
    }
    else
    {
        int diferenca = solucao - pinos[i];
        pinos[i+1] += diferenca;
        quantidadeMovimentos += diferenca;
    }
}
Console.WriteLine(quantidadeMovimentos);