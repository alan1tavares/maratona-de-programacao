#include<bits/stdc++.h>
using namespace std;
int main(){
    int totalDeC, qtdPaineis;
    char c;
    qtdPaineis = 0;
    cin >> totalDeC;
    while  (totalDeC--){
        cin >> c;
        if (c == 'P' or c == 'C')
            qtdPaineis += 2;
        else if (c == 'A')
            qtdPaineis++;
    }

    cout << qtdPaineis << "\n";


    return 0;
}
