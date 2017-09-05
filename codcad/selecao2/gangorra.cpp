#include<bits/stdc++.h>
using namespace std;

int main(){
    int p1,c1, p2, c2, esquerdo, direito;
    cin >> p1 >> c1 >> p2 >> c2;
    esquerdo = p1*c1;
    direito = p2*c2;
    if (esquerdo == direito)
        cout << "0";
    else if (esquerdo > direito)
        cout << -1;
    else
        cout << 1;


    return 0;
}
