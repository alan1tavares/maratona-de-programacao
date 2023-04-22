/**
 * Gerando Permutações Ordenadas Rapidamente
 * https://www.beecrowd.com.br/judge/pt/problems/view/1401
*/

using System.Collections.Generic;
using System.Linq;

int.TryParse(Console.ReadLine(), out int quantidadeCasos);

for (int i = 0; i < quantidadeCasos; i++)
{
    string input = Console.ReadLine();

    HashSet<string> result = new HashSet<string>();
    Permutacao(result, "", String.Concat(input.OrderBy(c => c)));

    Console.WriteLine(string.Join("\n", result));
    Console.WriteLine();
}

static void Permutacao(HashSet<string> permutacaoGerada, string permutacaoAtual,
    string elementosAPermutar)
{
    if (elementosAPermutar != "")
    {
        for (int i = 0; i < elementosAPermutar.Length; i++)
        {
            string proximaPermutacao = permutacaoAtual + elementosAPermutar[i];
            string elementosRestantes = elementosAPermutar.Remove(i, 1);
            Permutacao(permutacaoGerada, proximaPermutacao, elementosRestantes);
        }
    } else
        permutacaoGerada.Add(permutacaoAtual);
}
