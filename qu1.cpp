#include <iostream>
#include <vector>
using namespace std;
#include <cmath>

int absDiff(vector<vector<int>> &arr)
{
    int n;
    int sum1 = 0, sum2 = 0;
    n = arr.size();
    for (int i = 0; i < n; i++)
    {
        sum1 += arr[i][i];
        sum2 += arr[i][n - 1 - i];
    }
    return abs(sum2 - sum1);
}

int main()
{
    vector<vector<int>> arr = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}};

    cout << absDiff(arr) << endl;
    return 0;
}