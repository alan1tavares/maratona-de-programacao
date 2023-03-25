/*
* Problema B
* Língua do P
**/
string input = Console.ReadLine()+'.';
string output = "";
for (int i = 0; i < input.Length; i++)
{
    if (input[i] != 'p')
        output += input[i];
    else if (input[i+1] == 'p')
    {
        output += 'p';
        i++;
    }
}

Console.WriteLine(output.Remove(output.Length-1));