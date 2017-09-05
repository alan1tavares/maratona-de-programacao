int_x = int(input())
int_z = int(input())
while int_z <= int_x:
	int_z = int(input())
soma = int_x
int_count = 1
while soma < int_z:
	int_x += 1
	soma += int_x
	int_count += 1
print(int_count)