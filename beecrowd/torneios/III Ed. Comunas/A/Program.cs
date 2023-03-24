using System.Collections.Generic;

/*
* Problema A
* 1069 - Diamantes e Areia
**/


int n = Convert.ToInt32(Console.ReadLine());

for (int i = 0; i < n; i++)
{
    string diamantes = Console.ReadLine();
    Console.WriteLine(GetQuantidadeDiamantes(diamantes));
}



static int GetQuantidadeDiamantes(string diamantes)
{
    int quantidadeDiamantes = 0;
    Stack<char> minerando = new Stack<char>();

    for (int i = 0; i < diamantes.Length; i++)
    {
        if (diamantes[i] == '<' || diamantes[i] == '>')
        {
            if (minerando.Count > 0 && minerando.Peek() == '<' && diamantes[i] == '>')
            {
                minerando.Pop();
                quantidadeDiamantes++;
            }
            else
                minerando.Push(diamantes[i]);
        }
    }

    return quantidadeDiamantes;
}



// Console.WriteLine(quantidadeDiamantes);
