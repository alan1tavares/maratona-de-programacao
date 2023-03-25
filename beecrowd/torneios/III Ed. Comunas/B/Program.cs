/*
* Problema B
* Língua do P
**/

string input = Console.ReadLine();
input = input.Replace("pp","&");
input = input.Replace("p","");
input = input.Replace("&","p");
Console.WriteLine(input);