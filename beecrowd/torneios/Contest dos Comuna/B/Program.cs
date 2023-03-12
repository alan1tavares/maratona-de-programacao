/**
 * Problema B - Conversão de Tempo
 * https://www.beecrowd.com.br/judge/pt/problems/view/1019
 */

int x = Convert.ToInt32(Console.ReadLine());

int seg = x % 60;
int min = x / 60;
int h = min / 60;
min = min % 60;


Console.WriteLine($"{h}:{min}:{seg}");

