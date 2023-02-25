public class Solution {
    public int MissingNumber(int[] nums) {
        int res = 0;
        for(int i = 0; i <= nums.Length; i++){
            res = res + i ;
        }
        return res - nums.Sum();
    }
}