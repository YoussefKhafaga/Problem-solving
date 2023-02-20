public class Solution {
    public int SearchInsert(int[] nums, int target) {
        int low = 0;
        int high = nums.Length;
        int mid;
        while(low < high){
            mid = (low + high - 1) / 2;
            if(nums[mid] == target)
                return Array.IndexOf(nums, target);
            else if(target < nums[mid]){
                high = mid;
            }
            else{
                low = mid + 1;
            }
        }
        return high;
    }
}