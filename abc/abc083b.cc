#include<iostream>
#include <cmath>
using namespace std;

int main()
{
    int N, A, B, total = 0;
    cin >> N >> A >> B;

    /* algo 1
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
    */

    // algo 2
    for (int i=1; i<=N; i++) {
        int sum = 0;
        int tmp = i;
        while(true) {
            sum += tmp % 10;
            tmp /= 10;
            if (tmp == 0) break;
        }
        if (sum >= A && sum <= B) {
            total += i;
        }

    }

    cout << total << endl;

    return 0;
}