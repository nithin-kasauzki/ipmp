#include <iostream>
using namespace std;

int main()
{
    int a[] = {1, 2, 3, 2, 3, 1, 3};
    int n = sizeof(a) / sizeof(a[0]);
    int hash[n];
    for (int i = 0; i < n; i++)
    {
        hash[i] = 0;
    }
    for (int i = 0; i < n; i++)
    {
        hash[a[i]]++;
    }
    for (int i = 0; i < n; i++)
    {
        if (hash[i] % 2 != 0)
            cout << i;
        break;
    }
}