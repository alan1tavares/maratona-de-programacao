using System.Text.RegularExpressions;
using System.Collections.Generic;
/**
 * Frase Completa
 * https://www.beecrowd.com.br/judge/pt/problems/view/1551
 */

int n = Convert.ToInt32(Console.ReadLine());

for (int i = 0; i < n; i++)
{
    string input = Console.ReadLine();
    input = Regex.Replace(input, "\\s+|,", "");
    Dictionary<char, int> match = new Dictionary<char, int>();
    for (int j = 0; j < input.Length; j++)
    {
        match.TryAdd(input[j], 0);
        if (match.Count == 26) break;
    }

    if (match.Count == 26) Console.WriteLine("frase completa");
    else if (match.Count >= 13) Console.WriteLine("frase quase completa");
    else Console.WriteLine("frase mal elaborada");
}
