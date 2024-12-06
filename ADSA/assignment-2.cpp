/*
    Multiplication and Addition of Polynomials
*/

#include <iostream>
#include <vector>
using namespace std;

// Polynomial addition
vector<int> addPolynomials(const vector<int> &poly1, const vector<int> &poly2)
{
    int n = max(poly1.size(), poly2.size());
    vector<int> result(n, 0);

    for (int i = 0; i < poly1.size(); ++i)
        result[i] += poly1[i];
    for (int i = 0; i < poly2.size(); ++i)
        result[i] += poly2[i];

    return result;
}

// Polynomial multiplication
vector<int> multiplyPolynomials(const vector<int> &poly1, const vector<int> &poly2)
{
    vector<int> result(poly1.size() + poly2.size() - 1, 0);

    for (int i = 0; i < poly1.size(); ++i)
    {
        for (int j = 0; j < poly2.size(); ++j)
        {
            result[i + j] += poly1[i] * poly2[j];
        }
    }

    return result;
}

// Print polynomial
void printPolynomial(const vector<int> &poly)
{
    for (int i = poly.size() - 1; i >= 0; --i)
    {
        if (poly[i] != 0)
        {
            cout << poly[i] << "x^" << i;
            if (i > 0)
                cout << " + ";
        }
    }
    cout << endl;
}

// Main function
int main()
{
    vector<int> poly1 = {3, 2, 1}; // 3 + 2x + x^2
    vector<int> poly2 = {1, 2};    // 1 + 2x

    cout << "Addition of polynomials: ";
    printPolynomial(addPolynomials(poly1, poly2));

    cout << "Multiplication of polynomials: ";
    printPolynomial(multiplyPolynomials(poly1, poly2));

    return 0;
}
