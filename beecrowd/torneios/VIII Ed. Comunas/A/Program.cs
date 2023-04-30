/**
 * Telescópio
 * https://www.beecrowd.com.br/judge/pt/problems/view/2386
*/
using System;

int areaAberturaTelecopio = int.Parse(Console.ReadLine());
int numeroEstrelas = int.Parse(Console.ReadLine());
int numeroEstrelasPercebidas = 0;
const int FOTONS_NECESSARIOS = 40000000;
for (int i = 0; i < numeroEstrelas; i++)
{
    int fluxoFotons = int.Parse(Console.ReadLine());
    if (areaAberturaTelecopio*fluxoFotons >= FOTONS_NECESSARIOS)
        numeroEstrelasPercebidas ++;

}


Console.WriteLine(numeroEstrelasPercebidas);

