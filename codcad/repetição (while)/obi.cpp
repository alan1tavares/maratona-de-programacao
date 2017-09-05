#include<bits/stdc++.h>
using namespace std;

int main(){
    int numeroCompeidores, minimoPontos, fase1, fase2, passaram;
    cin >> numeroCompeidores >> minimoPontos;
    passaram = 0;
    while(numeroCompeidores--){
        cin >> fase1 >> fase2;
        if((fase1+fase2) >= minimoPontos)
            passaram++;
    }
    cout << passaram << "\n";

    return 0;
}
