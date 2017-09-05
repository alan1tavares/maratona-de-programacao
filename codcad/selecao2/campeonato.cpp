#include<bits/stdc++.h>
using namespace std;
int main(){
    int cV, cE, cS, fV, fE, fS;
    cin >> cV>> cE>> cS>> fV>> fE>> fS;
    cV = (cV*3) + cE;
    fV = (fV*3) + fE;

    if (cV>fV)
        cout << "C";
    else if (cV==fV){
        if (cS > fS)
            cout << "C";
        else if (cS == fS)
            cout << "=";
        else
            cout << "F";
    } else
        cout << "F";

    return 0;
}
