/**
* Salário
* https://www.beecrowd.com.br/judge/pt/problems/view/1008
**/

string funcionario = Console.ReadLine();
double horasTrabalhadas = Convert.ToDouble(Console.ReadLine());
double salarioPorHora = Convert.ToDouble(Console.ReadLine());
double salario = horasTrabalhadas * salarioPorHora;

Console.WriteLine($"NUMBER = {funcionario}");
Console.WriteLine("SALARY = U$ " + salario.ToString("0.00"));
