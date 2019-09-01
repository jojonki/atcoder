typedef long long ll;

ll gcd(ll A, ll B) {
    ll rem;
    if(A<B) {
        ll tmp = A;
        A = B;
        B = tmp;
    }
    rem = A % B;
    if (rem == 0) {
        return B;
    }

    return gcd(B, rem);

}
