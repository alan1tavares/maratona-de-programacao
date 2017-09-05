#include<bits/stdc++.h>
using namespace std;
int main(){

    int maiorNurmero, p, q, result;
    char c;
    cin >> maiorNurmero >> p >> c >> q;
    if(c == '*')
        result = p*q;
    else
        result = p+q;
    if(result > maiorNurmero)
        cout << "OVERFLOW";
    else
        cout << "OK";


    return 0;
}
