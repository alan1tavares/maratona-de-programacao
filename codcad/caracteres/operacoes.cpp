#include<bits/stdc++.h>
using namespace std;
int main(){
    char c;
    double d1, d2;
    cin >> c;
    cin >> d1 >> d2;
    if(c == 'M')
        d1 *= d2;
    else
        d1 /= d2;

    cout.precision(2);
    cout.setf(ios::fixed);

    cout << d1 << "\n";


    return 0;
}
