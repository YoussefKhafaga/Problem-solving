public class Solution {
    public int HammingWeight(uint n) {
        int result = 0;
        while(n > 0)
        {
            // And every integer with integer - 1 to get the integer with the one bits
            // remainig only
            n = n & (n-1);
            result ++;
            
        }
        return result;
    }
}