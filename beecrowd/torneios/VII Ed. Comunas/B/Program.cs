/**
 * LED
 * https://www.beecrowd.com.br/judge/pt/problems/view/1168
 */

int n = int.Parse(Console.ReadLine());
int[] led = {6, 2, 5, 5, 4, 5, 6, 3, 7, 6};
for (int i = 0; i < n; i++)
{
    int quantidadeLed = 0;
    string numeros = Console.ReadLine();
    for (int j = 0; j < numeros.Length; j++)
    {
        quantidadeLed += led[int.Parse(numeros.Substring(j,1))];
    }
    Console.WriteLine(quantidadeLed + " leds");
}