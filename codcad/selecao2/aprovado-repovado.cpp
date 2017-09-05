#include<bits/stdc++.h>
using namespace std;
int main(){
    int nota1, nota2, media;
    cin >> nota1 >> nota2;
    media = (nota1+nota2)/2;

    if(media >= 7)
        cout << "Aprovado";
    else if (media < 7 and media >= 4)
        cout << "Recuperacao";
    else
        cout << "Reprovado";
    return 0;
}

