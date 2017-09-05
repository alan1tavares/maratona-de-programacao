#include<iostream>
using namespace std;
int main(){
    int t1, t2, t3;
    cin >> t1 >> t2 >> t3;
    if(t1 < t2 && t2 < t3)
        cout << 1<<"\n"<<2<<"\n"<<3<<"\n";
    else if (t1 < t3 && t3 < t2)
        cout << 1<<"\n"<<3<<"\n"<<2<<"\n";
    else if (t2 < t1 && t1 < t3)
        cout << 2<<"\n"<<1<<"\n"<<3<<"\n";
    else if (t2 < t3 && t3 < t1)
        cout << 2<<"\n"<<3<<"\n"<<1<<"\n";
    else if (t3 < t1 && t1 < t2)
        cout << 3<<"\n"<<1<<"\n"<<2<<"\n";
    else
        cout << 3<<"\n"<<2<<"\n"<<1<<"\n";
    return 0;
}
