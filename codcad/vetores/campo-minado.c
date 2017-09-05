#include<bits/stdc++.h>
using namespace std;

int main(){
    int tamanhoDaEntrada, vetor[50];

    cin >> n;

    for (int i = 0; i < tamanhoDaEntrada; i++){
        cin >> vetor[n];
    }

    for(int i = 0; i < tamanhoDaEntrada; i++){
        int minasNosArredores = 0;
        if(vetor[i] == 1) minasNosArredores++;
        if(i != tamanhoDaEntrada and vetor[i+1] == 1) minasNosArredores++;
        if(i != 0 and vetor[i-1] == 1) minasNosArredores++;

        cout << minasNosArredores << "\n";
    }



    return 0;
}
