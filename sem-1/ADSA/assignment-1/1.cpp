/*
    Infix to Prefix and Postfix Conversion (and vice-versa)
*/

#include <iostream>
#include <stack>
#include <string>
#include <algorithm>

using namespace std;

// Function to check precedence of operators
int precedence(char op)
{
    if (op == '+' || op == '-')
        return 1;
    if (op == '*' || op == '/')
        return 2;
    if (op == '^')
        return 3;
    return 0;
}

// Function to check if the character is an operator
bool isOperator(char c)
{
    return c == '+' || c == '-' || c == '*' || c == '/' || c == '^';
}

// Function to convert infix to postfix
string infixToPostfix(const string &infix)
{
    stack<char> operators;
    string postfix;

    for (char c : infix)
    {
        if (isalnum(c))
        {
            postfix += c; // Operand
        }
        else if (c == '(')
        {
            operators.push(c);
        }
        else if (c == ')')
        {
            while (!operators.empty() && operators.top() != '(')
            {
                postfix += operators.top();
                operators.pop();
            }
            operators.pop(); // Remove '('
        }
        else if (isOperator(c))
        {
            while (!operators.empty() && precedence(operators.top()) >= precedence(c))
            {
                postfix += operators.top();
                operators.pop();
            }
            operators.push(c);
        }
    }

    while (!operators.empty())
    {
        postfix += operators.top();
        operators.pop();
    }

    return postfix;
}

// Function to convert infix to prefix
string infixToPrefix(const string &infix)
{
    string reversedInfix = infix;
    reverse(reversedInfix.begin(), reversedInfix.end());

    for (char &c : reversedInfix)
    {
        if (c == '(')
            c = ')';
        else if (c == ')')
            c = '(';
    }

    string postfix = infixToPostfix(reversedInfix);
    reverse(postfix.begin(), postfix.end());
    return postfix;
}

// Main function
int main()
{
    string infix;
    cout << "Enter an infix expression: ";
    cin >> infix;

    string postfix = infixToPostfix(infix);
    string prefix = infixToPrefix(infix);

    cout << "Postfix Expression: " << postfix << endl;
    cout << "Prefix Expression: " << prefix << endl;

    return 0;
}
