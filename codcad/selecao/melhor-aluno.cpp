#include<iostream>
using namespace std;
int main(){
    double pedro, paulo;
    cin >> pedro >> paulo;
    if(pedro < paulo or pedro == paulo)
        cout << "Pedro\n";
    else
        cout << "Paulo\n";
    return 0;
}
