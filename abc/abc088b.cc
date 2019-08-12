#include<iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<int> a;
    while(N--) {
        int val;
        cin >> val;
        a.push_back(val);
    }

    sort(a.begin(), a.end(), greater<int>());

    int a_score = 0;
    int sign = 1;
    for (int i=0; i<a.size(); i++) {
        a_score += a[i] * sign;
        sign *= (-1);
    }

    cout << a_score << endl;

    return 0;
}