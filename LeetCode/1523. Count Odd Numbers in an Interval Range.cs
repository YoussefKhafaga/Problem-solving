public class Solution {
    public int CountOdds(int low, int high) {
        if (low % 2 != 0 && high % 2 != 0)
            return ((high - low + 1)/2)+1;
        return (high - low + 1)/2;
    }
}