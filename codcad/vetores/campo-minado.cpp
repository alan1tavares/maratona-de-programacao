#include<bits/stdc++.h>
using namespace std;

int main(){
    int tamanhoDaEntrada, vetor[50];

    cin >> tamanhoDaEntrada;

    for (int i = 0; i < tamanhoDaEntrada; i++){
        cin >> vetor[i];
    }

    for(int i = 0; i < tamanhoDaEntrada; i++){
        int minasNosArredores = 0;
        minasNosArredores += vetor[i];
        if(i < tamanhoDaEntrada-1)
            minasNosArredores += vetor[i+1];
        if(i > 0)
            minasNosArredores += vetor[i-1];
        cout << minasNosArredores << "\n";
    }



    return 0;
}
