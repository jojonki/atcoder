#include<iostream>
using namespace std;

int main()
{
    int N;
    cin >> N;
    int a[N], b[N];
    int count = 100000, tmp, tmp_count;
    for(int i=0; i<N; i++) {
        cin >> tmp;
        tmp_count = 0;
        while(tmp % 2 == 0) {
            tmp /= 2;
            tmp_count++;
        }
        if (tmp_count < count) {
            count = tmp_count;
        }
    }
    cout << count << endl;
    
    return 0;
}