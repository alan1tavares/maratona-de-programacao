#include<bits/stdc++.h>
using namespace std;

int main(){
    int p, n, f;
    cin >> p >> n;

    while (n--){
        cin >> f;
        p += f;
        if (p > 100)
            p = 100;
        if (p < 0)
            p = 0;
    }

    cout <<p<<"\n";
    return 0;
}
