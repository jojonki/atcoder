#include <iostream>
#include <vector>
using namespace std;

inline void print() { cout << endl; }
template <class Head, class... Tail> inline void print(Head&& head, Tail&&... tail) {cout << head; if (sizeof...(tail) != 0) cout << " "; print(forward<Tail>(tail)...);}
template <class T> inline void print(vector<T>& vec) { for (auto& a : vec) {cout << a; if (&a != &vec.back()) cout << " "; } cout << endl;}
template <class T> inline void print(vector<vector<T>>& df) { for (auto& vec : df) { print(vec); }}

int main() {
    int a = 1;
    print("Test");
    print(a, 3.14, "Hello");
    print();

    vector<int> arr{1, 2, 3, 2};
    vector<string> str_arr{"Hello", "World"};
    print(arr);
    print(str_arr);
    print();

    vector<vector<int>> table{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    print(table);
}