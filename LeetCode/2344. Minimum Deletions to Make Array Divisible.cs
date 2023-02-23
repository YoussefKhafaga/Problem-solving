public class Solution {
    public int euclidgcd(int a, int b){
            if(b == 0)
                return a;
            return euclidgcd(b, a%b);
        }
    public int MinOperations(int[] nums, int[] numsDivide) {
        int gcd = numsDivide[0];
        int deletions = 0;
        for(int j = 1; j < numsDivide.Length; j++){
            gcd = euclidgcd(gcd, numsDivide[j]);
        }

        int i = 0;
        int len = nums.Length;
        Array.Sort(nums);
        while(i < nums.Length)
        {

            if(gcd % nums[i] != 0){
                int length = nums.Length;
                nums = nums.Where(val => val != nums[i]).ToArray();
                deletions += length - nums.Length;
                i = 0;
                continue;
                }
            break;
        }
        if(deletions == len)
                return -1;
        return deletions;
       }
}