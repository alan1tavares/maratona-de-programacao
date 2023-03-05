/**
 * Problema D - Substituição em Vetor 
 * https://www.beecrowd.com.br/judge/pt/problems/view/1172
 * */

int[] vec = new int[10];
for (int i = 0; i < 10; i ++)
{
	int input = Convert.ToInt32(Console.ReadLine());
	vec[i] = input > 0 ? input : 1;
}

for(int i = 0; i < vec.Length; i++) Console.WriteLine($"X[{i}] = {vec[i]}");
