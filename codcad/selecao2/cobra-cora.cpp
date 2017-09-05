#include<bits/stdc++.h>
using namespace std;

int main(){
    int a,s,d,f;
    cin >> a>>s>>d>>f;

    if (a==d)
        cout << "V";
    else if (s==f)
        cout << "V";
    else
        cout << "F";

    return 0;
}
