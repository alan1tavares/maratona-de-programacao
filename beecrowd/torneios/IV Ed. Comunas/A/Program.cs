/**
 * Array Hash
 * https://www.beecrowd.com.br/judge/pt/problems/view/1257
 */

int asciiA = (int) 'A';

int n =  Convert.ToInt32(Console.ReadLine());
for (int i = 0; i < n; i++)
{
    int valorHash = 0;
    int l = Convert.ToInt32(Console.ReadLine());    
    for (int j = 0; j < l; j++)
    {
        string input = Console.ReadLine();
        for (int k = 0; k < input.Length; k++)
        {
            valorHash += ((int)input[k])-asciiA + j + k; 
        }
    }

    Console.WriteLine(valorHash);
}
