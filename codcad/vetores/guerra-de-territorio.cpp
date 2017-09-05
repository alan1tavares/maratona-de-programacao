#include<bits/stdc++.h>
using namespace std;

int main(){
    int n, somaTotal, somaAtual;
    somaTotal = somaAtual = 0;

    cin >> n;

    int v[n];

    for(int i = 0; i < n; i++){
        cin >> v[i];
        somaTotal += v[i];
    }

    int i;
    int metadeSomaTotal = somaTotal/2;
    for(i = 0; i < n; i++){
        somaAtual += v[i];
        if(somaAtual == metadeSomaTotal)
            break;

    }

    cout << (i+1) << "\n";

    return 0;
}
