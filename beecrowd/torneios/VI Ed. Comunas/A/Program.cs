/**
 * Árvore Binária de Busca
 * https://www.beecrowd.com.br/judge/pt/problems/view/1195
*/
using System;
using System.Text;

int c = int.Parse(Console.ReadLine());
StringBuilder result = new StringBuilder (500000);
for (int i = 0; i < c; i++)
{
    string n = Console.ReadLine();
    int[] listaNo = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
    No noRaiz = new No(listaNo[0]);
    foreach (int item in listaNo)
        noRaiz.Add(item);

    Console.WriteLine($"Case {i+1}:");
    result.Clear();
    Console.WriteLine($"Pre.:{noRaiz.GetPreOrdem(result)}");
    result.Clear();
    Console.WriteLine($"In..:{noRaiz.GetInOrdem(result)}");
    result.Clear();
    Console.WriteLine($"Post:{noRaiz.GetPosOrdem(result)}\n");
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

    public string GetPreOrdem(StringBuilder result){
        GetPreOrdem(this, result);
        return result.ToString();
    }

    private void GetPreOrdem(No no, StringBuilder result)
    {
        if (no == null) return;
        result.Append(" " + no.Valor);
        GetPreOrdem(no.Esquerdo, result);
        GetPreOrdem(no.Direito, result);
    }

    public string GetInOrdem(StringBuilder result)
    {
        GetInOrdem(this, result);
        return result.ToString();
    }

    private void GetInOrdem(No no, StringBuilder result)
    {
        if (no == null) return;
        GetInOrdem(no.Esquerdo, result);
        result.Append(" " + no.Valor);
        GetInOrdem(no.Direito, result);
    }

    public string GetPosOrdem(StringBuilder result)
    {
        GetPosOrdem(this, result);
        return result.ToString();
    }

    private void GetPosOrdem(No no, StringBuilder result)
    {
        if (no == null) return;
        GetPosOrdem(no.Esquerdo, result);
        GetPosOrdem(no.Direito, result);
        result.Append(" " + no.Valor);
    }
}