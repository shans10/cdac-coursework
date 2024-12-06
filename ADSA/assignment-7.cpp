#include <iostream>
#include <vector>
using namespace std;

bool hasPairWithSum(const vector<int> &nums, int M)
{
    int left = 0, right = nums.size() - 1;

    while (left < right)
    {
        int sum = nums[left] + nums[right];
        if (sum == M)
        {
            cout << "Pair found: (" << nums[left] << ", " << nums[right] << ")" << endl;
            return true;
        }
        else if (sum < M)
        {
            right--; // Move the right pointer to a smaller value
        }
        else
        {
            left++; // Move the left pointer to a smaller value
        }
    }

    cout << "No pair found with sum " << M << endl;
    return false;
}

int main()
{
    vector<int> nums = {10, 7, 5, 3, 1}; // Sorted in descending order
    int M = 12;

    hasPairWithSum(nums, M);

    return 0;
}
