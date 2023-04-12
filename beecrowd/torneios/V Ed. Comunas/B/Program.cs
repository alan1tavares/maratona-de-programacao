/**
 * Matriz Escada
 * https://www.beecrowd.com.br/judge/pt/problems/view/2450
*/
using System;

string[] input = Console.ReadLine().Split();
int n = Convert.ToInt32(input[0]);
int m = Convert.ToInt32(input[1]);
int indiceColunaMaisAEsquerda = -1;
int somatorioLinhaAnterior = 1;

for (int i = 0; i < n; i++)
{
    int[] linhaMatrix = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
    
    int somatorioLinha = 0;
    for (int j = 0; j < m; j++)
    {
        int elemento = linhaMatrix[j];
        somatorioLinha += elemento;
        if (elemento != 0  && j > indiceColunaMaisAEsquerda)
        {
            indiceColunaMaisAEsquerda = j;
            break;
        } else if (j <= indiceColunaMaisAEsquerda)
        {
            if (elemento != 0)
            {
                Console.WriteLine("N");
                return;
            }
        }
    }
    if (somatorioLinhaAnterior == 0 && somatorioLinha > 0 )
    {
       Console.WriteLine("N");
        return; 
    }
    somatorioLinhaAnterior = somatorioLinha;
}
Console.WriteLine("S");
