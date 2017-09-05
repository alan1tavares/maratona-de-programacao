#include<bits/stdc++.h>
using namespace std;

int main(){
    int n, qtdR, minimo;
    cin >> n;
    minimo = INT_MAX;

    while (n--){
        cin >> qtdR;
        if (qtdR < minimo)
            minimo = qtdR;
    }

    cout << minimo << "\n";


    return 0;
}
