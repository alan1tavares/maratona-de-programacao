#include<iostream>

using namespace std;

int main(){
    int l1, a1, l2, a2;
    cin >> l1 >> a1 >> l2 >> a2;
    if((l1*a1) == (l2*a2))
        cout << "Empate";
    else if ((l1*a1) > (l2*a2))
        cout << "Primeiro";
    else
        cout << "Segundo";
    return 0;
}
