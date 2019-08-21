#include <iostream>
#include <vector>
using namespace std;

int main() { 
    int N, M;
    cin >> N >> M;
    vector<bool> issafe;
    issafe.assign(N+1, true);
    for (int i=1; i<M+1; i++) {
        int a;
        cin >> a;
        issafe[a] = false;
    }

    vector<int> dp;
    dp.assign(N+1, 0);

    dp[0] = 1;
    if (issafe[1]) dp[1] = 1;


    for (int i=2; i<=N; i++) {
        if (issafe[i-1]) dp[i] += dp[i-1];
        if (issafe[i-2]) dp[i] += dp[i-2];
        dp[i] %= 1000000007;
    }

    cout << dp[N] << endl;
    
    return 0;
}