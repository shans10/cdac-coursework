/*
    Direct Postfix to Prefix and Vice-Versa Conversion
*/

#include <iostream>
#include <stack>
#include <string>
#include <algorithm>

using namespace std;

// Convert Postfix to Prefix
string postfixToPrefix(const string &postfix)
{
    stack<string> st;
    for (char c : postfix)
    {
        if (isalnum(c))
        {
            st.push(string(1, c));
        }
        else
        {
            string operand2 = st.top();
            st.pop();
            string operand1 = st.top();
            st.pop();
            string prefix = c + operand1 + operand2;
            st.push(prefix);
        }
    }
    return st.top();
}

// Convert Prefix to Postfix
string prefixToPostfix(const string &prefix)
{
    stack<string> st;
    for (int i = prefix.size() - 1; i >= 0; --i)
    {
        char c = prefix[i];
        if (isalnum(c))
        {
            st.push(string(1, c));
        }
        else
        {
            string operand1 = st.top();
            st.pop();
            string operand2 = st.top();
            st.pop();
            string postfix = operand1 + operand2 + c;
            st.push(postfix);
        }
    }
    return st.top();
}

// Main function
int main()
{
    string postfix = "ab+c*";
    string prefix = "*+abc";

    cout << "Postfix to Prefix: " << postfixToPrefix(postfix) << endl;
    cout << "Prefix to Postfix: " << prefixToPostfix(prefix) << endl;

    return 0;
}
