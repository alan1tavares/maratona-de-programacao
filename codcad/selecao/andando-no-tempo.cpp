#include<bits/stdc++.h>
using namespace std;
int main(){
    int a,b,c,ab,ac,bc;
    cin >> a>>b>>c;
    ab = abs(a-b);
    ac = abs(a-c);
    bc = abs(b-c);
    if (a==0 or b==0 or c==0)
        cout << "S";
    else if (ab==0 or ac==0 or bc==0)
        cout << "S";
    else if ((ab-c)==0 or (ac-b)==0 or (bc-a)==0)
        cout << "S";
    else
        cout << "N";

    return 0;
}
