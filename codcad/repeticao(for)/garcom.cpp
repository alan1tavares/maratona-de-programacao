#include<bits/stdc++.h>
using namespace std;

int main(){
    int latas, copos, nBandejas, coposQuebrados;
    coposQuebrados = 0;
    cin >> nBandejas;
    while (nBandejas--){
        cin >> latas >> copos;
        if(latas > copos) {
            coposQuebrados+=copos;
        }
    }
    cout << coposQuebrados << "\n";


    return 0;
}
