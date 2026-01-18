#include <bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin>>n;
        int one=0,zero=0;
        for(int i=0;i<n;i++){
            int x;
            cin>>x;
            if(x==1)one++;
            else if(x==0)zero++;
        }
        bool f=false;
        if(zero==1||(zero>1&&one))f=true;
        cout<<((f)?"YES":"NO")<<'\n';
    }
    return 0;
}