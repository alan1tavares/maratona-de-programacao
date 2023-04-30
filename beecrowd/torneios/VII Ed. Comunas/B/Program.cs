/**
 * LED
 * https://www.beecrowd.com.br/judge/pt/problems/view/1168
 */

int n = int.Parse(Console.ReadLine());
int[] led = {6, 2, 5, 5, 4, 5, 6, 3, 7, 6};
for (int i = 0; i < n; i++)
{
    int quantidadeLed = 0;
    int[] numeros = Array.ConvertAll(Console.ReadLine().Split(""), int.Parse);
    for (int j = 0; j < numeros.Length; j++)
    {
        quantidadeLed += led[numeros[j]];
    }
    Console.WriteLine(quantidadeLed + " leds");
}