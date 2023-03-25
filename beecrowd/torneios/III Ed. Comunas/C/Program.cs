/*
* Problema C
* 2455 - Gangorra
**/

string[] s = Console.ReadLine().Split(' ');
int[] input = Array.ConvertAll(s, int.Parse);
int fact =  (input[2] * input[3]) - (input[0] * input[1]);
if (fact > 0) Console.WriteLine(1);
else if (fact < 0) Console.WriteLine(-1);
else Console.WriteLine(0);