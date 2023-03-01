public class Solution {
    public int SingleNonDuplicate(int[] nums) {
        int low = 0, high = nums.Length-1, mid;
        while(low < high)
        {
            mid = (low + high) / 2;
            if(mid % 2 == 1)
                mid --;
            if(nums[mid] != nums[mid+1])
                high = mid;
            else
                low = mid + 2;
        }
        return nums[low];
    }
}