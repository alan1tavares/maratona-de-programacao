/**
 * Árvore Binária de Busca
 * https://www.beecrowd.com.br/judge/pt/problems/view/1195
*/
using System;

int c = int.Parse(Console.ReadLine());
for (int i = 0; i < c; i++)
{
    string n = Console.ReadLine();
    int[] listaNo = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
    No noRaiz = new No(listaNo[0]);
    foreach (int item in listaNo)
        noRaiz.Add(item);

    Console.WriteLine($"Case {i+1}:");
    Console.WriteLine($"Pre.: {noRaiz.GetPreOrdem().Trim()}");
    Console.WriteLine($"In..: {noRaiz.GetInOrdem().Trim()}");
    Console.WriteLine($"Post: {noRaiz.GetPosOrdem().Trim()}\n");
}

class No
{
    No _esquerdo;
    No _direito;
    int _valor;

    public No(int valor) => _valor = valor;
    public int Valor { get => _valor; }
    public No Esquerdo { get => _esquerdo; }
    public No Direito { get => _direito; }

    public void Add(int input)
    {
        if (input < _valor)
        {
            if (_esquerdo == null)
                _esquerdo = new No(input);
            else
                _esquerdo.Add(input);
        } else if (input > _valor)
        {
            if (_direito == null)
                _direito = new No(input);
            else
                _direito.Add(input);
        }
    }

    public string GetPreOrdem() => GetPreOrdem(this);

    private string GetPreOrdem(No no)
    {
        if (no == null)
            return "";
        string result = " " + no.Valor;
        result += GetPreOrdem(no.Esquerdo);
        result += GetPreOrdem(no.Direito);
        return result;
    }

    public string GetInOrdem() => GetInOrdem(this);

    private string GetInOrdem(No no)
    {
        if (no == null) return "";
        string result = GetInOrdem(no.Esquerdo);
        result += no.Valor + " ";
        result += GetInOrdem(no.Direito);
        return result;
    }

    public string GetPosOrdem() => GetPosOrdem(this);

    private string GetPosOrdem(No no)
    {
        if (no == null) return "";
        string result = GetPosOrdem(no.Esquerdo);
        result += GetPosOrdem(no.Direito);
        result += no.Valor + " ";
        return result;
    }
}