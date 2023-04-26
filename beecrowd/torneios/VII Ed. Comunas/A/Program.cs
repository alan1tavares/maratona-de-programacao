/**
 * Acampamento de Férias
 * https://www.beecrowd.com.br/judge/pt/problems/view/1167
 */
using System.Collections.Generic;

while (true)
{
    int n = int.Parse(Console.ReadLine());
    if (n == 0) return;
    Circulo circulo = new Circulo();
    for (int i = 0; i < n; i++)
    {
        string[] input = Console.ReadLine().Split();
        circulo.Add(new Pessoa
        {
            Nome = input[0],
            Ficha = int.Parse(input[1])
        });
    }

    circulo.StartGame();
    Console.WriteLine("Vencedor(a): " + circulo.Winner().Nome);
}

public class Pessoa
{
    public string Nome { get; set; }
    public int Ficha { get; set; }
}

public class Circulo
{
    public int ficha { get; set; }
    private LinkedList<Pessoa> _listaPessoa;

    public Circulo()
    {
        _listaPessoa = new LinkedList<Pessoa>();
    }

    public void Add(Pessoa pessoa)
    {
        _listaPessoa.AddLast(pessoa);
    }

    public void StartGame()
    {
        int count = 0;
        var no = _listaPessoa.First;
        int ficha = no.Value.Ficha;
        bool praTras = ficha % 2 == 0;
        while (_listaPessoa.Count != 1)
        {
            if (count != ficha)
            {
                if (praTras) no = Previous(no);
                else no = Next(no);
                count += 1;
            }

            if (count >= ficha)
            {
                ficha = no.Value.Ficha;
                praTras = ficha % 2 == 0;
                var nextNo = praTras ?
                    Previous(no) : Next(no);
                _listaPessoa.Remove(no);
                no = nextNo;
                if (ficha > _listaPessoa.Count)
                {
                    ficha = ficha % _listaPessoa.Count;
                    ficha  = ficha == 0 ? _listaPessoa.Count : ficha;
                }
                count = 1;
            }
        }
    }

    public LinkedListNode<Pessoa> Next(LinkedListNode<Pessoa> no)
    {
        return no.Next == null ? _listaPessoa.First : no.Next;
    }

    public LinkedListNode<Pessoa> Previous(LinkedListNode<Pessoa> no)
    {
        return no.Previous == null ? _listaPessoa.Last : no.Previous;
    }

    public Pessoa Winner()
    {
        return _listaPessoa.First.Value;
    }
}