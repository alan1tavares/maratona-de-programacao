#include<bits/stdc++.h>
using namespace std;

int main(){
    int n, v, cont, sequencia, maiorSequencia;
    cin >> n >> v;
    sequencia = v;
    cont = 1;
    maiorSequencia = 0;

    for (int i=1; i<n; i++){
        cin >> v;
        if (v==sequencia)
            cont++;
        else{
            if (cont > maiorSequencia)
                maiorSequencia = cont;
            cont = 1;
            sequencia = v;
        }
    }

    if (cont > maiorSequencia)
        cout << cont << "\n";
    else
        cout << maiorSequencia << "\n";



    return 0;
}
