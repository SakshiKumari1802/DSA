class Solution {
public:
    bool check(vector<int>& nums) {
        int count = 0;
        int n = nums.size();
        
        for (int i = 0; i < n; i++) {
            // Check if the current element is greater than the next element
            // Using % n handles the wrap-around from the last element to the first
            if (nums[i] > nums[(i + 1) % n]) {
                count++;
            }
            
            // If we find more than one drop point, it can't be a rotated sorted array
            if (count > 1) {
                return false;
            }
        }
        
        return true;
    }
};