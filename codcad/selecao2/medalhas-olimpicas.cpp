#include<bits/stdc++.h>
using namespace std;
int main(){
    int ao, ap, ab, bo, bp, bb;
    cin >> ao >> ap >> ab >> bo >> bp >> bb;

    if(ao > bo)
        cout << "A";
    else if( ao == bo){
        if(ap > bp)
            cout << "A";
        else if (ap == bp){
            if (ab > bb)
                cout << "A";
            else
                cout << "B";
        } else
            cout << "B";
    } else
        cout << "B";

    return 0;
}
