#include<iostream>
#include <cmath>
using namespace std;

int main()
{
    int N, A, B, total = 0;
    cin >> N >> A >> B;

    for (int i=1; i<=N; i++) {
        string ns = to_string(i);
        int sum = 0;
        for (int j=0; j<ns.length(); j++) {
            sum += (ns[j] - '0'); // char -> int hack
        }
        if (sum >= A && sum <= B) {
            total += i;
        }
    }

    cout << total << endl;

    return 0;
}