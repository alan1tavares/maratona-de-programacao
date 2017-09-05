    #include<bits/stdc++.h>
    using namespace std;

    int main(){
        int h1, m1, h2, m2;
        cin >> h1 >> m1 >> h2 >> m2;

        while ((h1+m1+h2+m2) != 0) {
            h1 = h1*60 + m1;
            h2 = h2*60 + m2;
            if (h2 <= h1)
                h2 += (24*60);

            cout << h2-h1 << "\n";
            cin >> h1 >> m1 >> h2 >> m2;
        }

        return 0;
    }
