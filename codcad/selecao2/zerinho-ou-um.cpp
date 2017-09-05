#include<bits/stdc++.h>
using namespace std;

int main(){
    int alice, beto, clara;
    cin >> alice >> beto >> clara;

    if(alice != beto and alice != clara)
        cout << "A";
    else if (beto != alice and beto != clara)
        cout << "B";
    else if (clara != beto and clara != alice)
        cout << "C";
    else cout << "*";

    return 0;
}
