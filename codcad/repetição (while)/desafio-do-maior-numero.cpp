#include<bits/stdc++.h>
using namespace std;

int main(){
    int n, maior;
    cin >> n;
    maior = n;
    while (n!=0){
        if (n > maior)
            maior = n;
        cin >> n;
    }

    cout << maior << "\n";


    return 0;
}
