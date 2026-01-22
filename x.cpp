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
        string s;
        cin>>s;
        vector<int>suf(n+1,0);
        int cur=0,idx=-1,first=0,second=0;
        for(int i=n-1;i>=0;i--){
            if(s[i]=='('){
                cur++;
            }
            suf[i]=cur;
        }
        int cnt=-1;
        for(int i=0;i<n-1;i++){
            if(s[i]==')'&&s[i+1]=='('&&suf[i+2]){
                cnt=n-2;;
                break;
            }
        }
        cout<<cnt<<'\n';

    }
    return 0;
}