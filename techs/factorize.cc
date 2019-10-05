#include <iostream>
#include <vector>
using namespace std;
typedef long long ll;


vector<pair<ll, int>> factorize(ll n) {
    vector<pair<ll, int>> res;
    res.emplace_back(1, 1);
    for(ll i=2; i*i<=n; i++) {
        if(n%i) continue;
        res.emplace_back(i, 0);
        while(n%i == 0) {
            res.back().second++;
            n /= i;
        }
    }
    if(n>1) {
        res.emplace_back(n, 1);
    }

    return res;
}

void print_factorize(vector<pair<ll, int>> f) {
    for(auto a: f) {
        cout << a.first << "^" << a.second << " ";
    }
    cout << endl;
}

int main() {
    print_factorize(factorize(12));
    print_factorize(factorize(1));
    print_factorize(factorize(1));

    return 0;
}