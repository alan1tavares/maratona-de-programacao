#include<bits/stdc++.h>
using namespace std;

int main(){
    int n, t, tempoAnterior, tempoConsumo, tempoInicial;
    tempoAnterior = tempoConsumo = tempoInicial = 0;
    cin >> n;
    while (n--){
        cin >> t;
        if (t >= tempoAnterior){
            tempoConsumo += tempoAnterior - tempoInicial;
            tempoInicial = t;
            tempoAnterior = t+10;
        } else
            tempoAnterior = t+10;

    }
    tempoConsumo += tempoAnterior - tempoInicial;
    cout << tempoConsumo;
    return 0;
}
