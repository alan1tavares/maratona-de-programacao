#include<bits/stdc++.h>
using namespace std;

int main() {
    int nDias, saldo, movimentacao, menorSaldo;
    cin >> nDias >> saldo;
    menorSaldo = saldo;

    while (nDias--){
        cin >> movimentacao;
        saldo += movimentacao;
        if (saldo < menorSaldo)
            menorSaldo = saldo;
    }
    cout << menorSaldo << "\n";


    return 0;
}
