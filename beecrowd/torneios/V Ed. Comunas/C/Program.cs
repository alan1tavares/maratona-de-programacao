/**
 * Decifra
 * https://www.beecrowd.com.br/judge/pt/problems/view/2464
*/

int asciiA = (int) 'a';
string alfabeto = Console.ReadLine();
string textoCriptografado = Console.ReadLine();

for (int i = 0; i < textoCriptografado.Length; i++)
{
    int posicaoDaLetraNoAlfabeto = alfabeto.IndexOf(textoCriptografado[i]);
    Console.Write((char) (posicaoDaLetraNoAlfabeto + asciiA));
}
Console.Write("\n");