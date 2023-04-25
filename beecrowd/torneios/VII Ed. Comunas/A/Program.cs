/**
 * Acampamento de Férias
 * https://www.beecrowd.com.br/judge/pt/problems/view/1167
 */
using System.Collections.Generic;

while (true)
{
    int n = int.Parse(Console.ReadLine());
    if (n == 0) break;
    LinkedList<Pessoa> circulo = new LinkedList<Pessoa>();
    for (int i = 0; i < n; i++)
    {
        string[] input = Console.ReadLine().Split();
        circulo.AddLast(new Pessoa
        {
            Nome = input[0],
            Ficha = int.Parse(input[1])
        });
    }

    var no = circulo.First.Next;
    int ficha = no.Value.Ficha;
    int count = 1;
    while(circulo.Count != 1)
    {
        if (count == ficha)
        {
            ficha = no.Value.Ficha;
            var nextNo = ficha % 2 == 0 ? no.Previous : no.Next;
            count = 1;
            circulo.Remove(no);
            no = nextNo;
        }

        no = (ficha % 2 == 0) ? no.Previous : no.Next;
        count += 1;
    }

    Console.WriteLine("Vencendor(a): " + no.Value.Nome);

}

public record Pessoa
{
    public string Nome {get;set;}
    public int Ficha {get;set;}
}