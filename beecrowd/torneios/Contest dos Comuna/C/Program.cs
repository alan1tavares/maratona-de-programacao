/**
 * Problema C - Flores Florescem da França
 * https://www.beecrowd.com.br/judge/pt/problems/view/1140 
 * */

while (true)
{
	string input = Console.ReadLine();
	if (input == "*") return;
	string [] words = input.Split(' ');
	char firstLetter = input[0];

	string result = "Y";
	foreach(string word in words)
	{
		if (!((word[0] == Char.ToLower(firstLetter)) || (word[0] == Char.ToUpper(firstLetter))))
			
		{
			result = "N";
			break;
		}
	}
	Console.WriteLine(result);
}


