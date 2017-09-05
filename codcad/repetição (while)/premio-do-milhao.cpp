#include<bits/stdc++.h>
using namespace std;

int main(){
    int nDias, nAcessos, chegouLa, diasNecessarios;
    cin >> nDias;
    diasNecessarios = 0;
    chegouLa = 0;
    while (chegouLa < pow(10,6)){
        cin >> nAcessos;
        diasNecessarios += 1;
        chegouLa += nAcessos;
    }

    cout << diasNecessarios << "\n";


    return 0;
}
