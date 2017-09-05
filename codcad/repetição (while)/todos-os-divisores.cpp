#include<bits/stdc++.h>
using namespace std;

int main(){
    int x, aux;
    bool f;
    cin >> x;
    aux = 1;
    f = false;
    while (aux <= x){
        if (f == true)
            cout << " ";
        f = false;
        if(x%aux == 0){
            cout << aux;
            f = true;
        }
        aux++;
    }
    cout << "\n";
    return 0;
}
