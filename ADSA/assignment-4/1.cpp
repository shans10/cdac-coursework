/*
    Divide-and-Conquer Algorithms
*/

// Algorithm 1: Binary Exponentiation

#include <iostream>
using namespace std;

long long power(long long base, int exp)
{
    if (exp == 0)
        return 1;
    long long half = power(base, exp / 2);
    return (exp % 2 == 0) ? half * half : base * half * half;
}

int main()
{
    cout << "2^10 = " << power(2, 10) << endl;
    return 0;
}
